import os
import csv

#Subfolder:
# random_bg
# no_bg
# default

FOLDER="./dataset/no_bg/"
TRAIN_NAME = next(os.walk(FOLDER+"/TRAIN/"), (None, None, []))[2]
TEST_NAME = next(os.walk(FOLDER+"/TEST/"), (None, None, []))[2]
VALIDATE_NAME = next(os.walk(FOLDER+"/VALIDATE/"), (None, None, []))[2]

def categorize(name: str):
    tmp=name.split("_")[1].split(".")[0]
    cat=""
    if tmp=='01':
        cat="0" #toward
    elif tmp>'01' and tmp<'05':
        cat="1" #toward left
    elif tmp=='05':
        cat="2" #left
    elif tmp>'05' and tmp<'09':
        cat='3' #bickering left
    elif tmp=='09':
        cat='4' #bickering
    elif tmp>'09' and tmp<'13':
        cat='5' #bickering right
    elif tmp=='13':
        cat='6' #right
    else:
        cat='7' #toward right
    print(name+"\t"+tmp+"\t"+cat)
    return cat

data_short_TRAIN=[]
data_short_TEST=[]
data_short_VALIDATE=[]


for name in TRAIN_NAME:
    data_short_TRAIN.append([name, categorize(name)])
for name in TEST_NAME:
    data_short_TEST.append([name, categorize(name)])
for name in VALIDATE_NAME:
    data_short_VALIDATE.append([name, categorize(name)])

with open(FOLDER+"labels/TRAIN.csv",'w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data_short_TRAIN)
    
with open(FOLDER+"labels/TEST.csv",'w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data_short_TEST)
    
with open(FOLDER+"labels/VALIDATE.csv",'w',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data_short_VALIDATE)