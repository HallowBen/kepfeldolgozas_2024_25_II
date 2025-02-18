import cv2
from os import walk
import random
import numpy as np

filenames = next(walk("../masked_img/"), (None, None, []))[2]
names=[]
for i in filenames:
    names.append(i.split(".")[0])
    
bgs_list = next(walk("../bg/"), (None, None, []))[2]
bgs=[]
for i in bgs_list:
    if "_new.jpg" in i:
       bgs.append(i) 
# bg=cv2.imread("../bg/"+bgs[4])

# cv2.imshow('bg',bg)
# cv2.waitKey(0)
for i in range(len(filenames)):
    img = cv2.imread('../masked_img/'+names[i]+'.jpg')
    bg= cv2.imread('../bg/'+bgs[random.randint(0,2)])
    car = cv2.resize(img,(1438,960))
    gray = cv2.cvtColor(car, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)
    x_offset = (bg.shape[1] - car.shape[1]) // 2
    y_offset = bg.shape[0] - car.shape[0] - 100
    
    mask_inv = cv2.bitwise_not(mask)
    roi = bg[y_offset:y_offset + car.shape[0], x_offset:x_offset + car.shape[1]]
    bg_roi = cv2.bitwise_and(roi, roi, mask=mask_inv)
    car_fg = cv2.bitwise_and(car, car, mask=mask)
    dst = cv2.add(bg_roi, car_fg)
    bg[y_offset:y_offset + car.shape[0], x_offset:x_offset + car.shape[1]] = dst
    
    # cv2.imshow(filenames[i],bg)
    # cv2.waitKey(0)
    
    # mask = cv2.imread('../bg/'+bgs[random.randint(0,2)])
    # masked_img=np.uint8(img*0.8+mask*0.1)
    # # masked_img = cv2.addWeighted(img,0.8,mask,0.1,0.4)
    cv2.imwrite('../used_sets/random_bg/'+names[i]+'_bg_changed.jpg',img=bg)