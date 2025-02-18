import cv2
from os import walk
import random

FOLDER=""
TEST=
TRAIN=
VALIDATE=

filenames = next(walk(FOLDER), (None, None, []))[2]
names=[]
for i in filenames:
    names.append(i.split("_")[0]+i.split("_")[1])


for i in range(len(filenames)):
    random.randint(0,2)
    