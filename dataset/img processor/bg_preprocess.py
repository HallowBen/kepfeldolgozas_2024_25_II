import cv2
from os import walk

WIDTH= 1918
HEIGHT= 1280
    
bgs = next(walk("../bg/"), (None, None, []))[2]
names=[]
for i in bgs:
    names.append(i.split(".")[0])

for i in range(len(bgs)):
    img=cv2.imread("../bg/"+bgs[i])
    # cv2.imshow('img',img)
    # cv2.waitKey(0)
    new_img=cv2.resize(img, (WIDTH, HEIGHT),interpolation = cv2.INTER_CUBIC)
    cv2.imwrite("../bg/"+names[i]+"_new.jpg", img=new_img)