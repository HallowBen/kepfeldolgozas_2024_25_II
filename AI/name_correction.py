import os
import csv

#Subfolder:
# random_bg
# no_bg
# default

FOLDER="./dataset/default/"
TRAIN_NAME = next(os.walk(FOLDER+"/TRAIN/"), (None, None, []))[2]
TEST_NAME = next(os.walk(FOLDER+"/TEST/"), (None, None, []))[2]
VALIDATE_NAME = next(os.walk(FOLDER+"/VALIDATE/"), (None, None, []))[2]

data_short_TRAIN=[]
data_short_TEST=[]
data_short_VALIDATE=[]


# for name in TRAIN_NAME:
#     os.rename(FOLDER+"/TRAIN/"+name,FOLDER+"/TRAIN/"+name.split('.')[0]+"."+name.split('.')[1])
# for name in TEST_NAME:
#     os.rename(FOLDER+"/TEST/"+name,FOLDER+"/TEST/"+name.split('.')[0]+"."+name.split('.')[1])
for name in VALIDATE_NAME:
    os.rename(FOLDER+"/VALIDATE/"+name,FOLDER+"/VALIDATE/"+name.split('.')[0]+"."+name.split('.')[1])