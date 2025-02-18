import cv2
from os import walk


filenames = next(walk("../images/train/"), (None, None, []))[2]
names=[]
for i in filenames:
    names.append(i.split(".")[0])

for i in range(len(filenames)):
    img = cv2.imread('../images/train/'+names[i]+'.jpg')
    mask = cv2.imread('../images/new_masks/'+names[i]+'_mask.jpg', 0)
    masked_img = cv2.bitwise_and(img,img,mask = mask)

    cv2.imwrite('../masked_img/'+names[i]+'_masked.jpg',img=masked_img)