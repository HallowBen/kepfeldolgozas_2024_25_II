import cv2
import os
import random
import csv

#Subfolder:
# random_bg
# no_bg
# default

FOLDER="../used_sets/default/"

DEST="../f_dataset/"+FOLDER.split('/')[2]+"/"
os.makedirs(DEST)
os.makedirs(DEST+"TEST")
os.makedirs(DEST+"TRAIN")
os.makedirs(DEST+"VALIDATE")

TEST_RATE=0.6
TRAIN_RATE=0.2
VALIDATE_RATE=0.2

filenames = next(os.walk(FOLDER), (None, None, []))[2]
names=[]
for i in filenames:
    names.append(i.split("_")[0]+"_"+i.split("_")[1])

TEST=TEST_RATE*len(filenames)
TRAIN=TRAIN_RATE*len(filenames)
VALIDATE=VALIDATE_RATE*len(filenames)

def train_test_validate():
    global TEST, TRAIN, VALIDATE
    ttv_type=""
    while ttv_type=="":
        ttv=random.randint(0,2)
        if ttv==0 and TEST!=0:
            ttv_type="TEST"
            TEST=-1
        elif ttv==1 and TRAIN!=0:
            ttv_type="TRAIN"
            TRAIN=-1
        elif VALIDATE!=0:
            ttv_type="VALIDATE"
            VALIDATE=-1
    return ttv_type

def manipulate(img: cv2.typing.MatLike):
    mantype=random.random()
    if mantype<0.3:
        tmp=cv2.blur(img,(10,10))
        tmp=cv2.resize(tmp,(479,320))
    elif mantype<0.7:
        tmp=cv2.resize(img,(479,320))
        tmp=cv2.blur(tmp,(20,20))
    else:
        tmp=cv2.resize(img,(479,320))
    return tmp

def categorize(name: str):
    tmp=name.split('_')[1]
    cat=""
    if tmp=='01':
        cat="t" #toward
    elif tmp>'01' and tmp<'05':
        cat="tl" #toward left
    elif tmp=='05':
        cat="l" #left
    elif tmp>'05' and tmp<'09':
        cat='bl' #bickering left
    elif tmp=='09':
        cat='b' #bickering
    elif tmp>'09' and tmp<'13':
        cat='br' #bickering right
    elif tmp=='13':
        cat='r' #right
    else:
        cat='tr' #toward right
    
    return cat


if TEST+TRAIN+VALIDATE != len(filenames):
    TRAIN+=len(filenames)-(TEST+TRAIN+VALIDATE)

data_long=[
    ["SET","PLACE","CATEGORY"],
]

data_short_TRAIN=[]
data_short_TEST=[]
data_short_VALIDATE=[]

for i in range(len(filenames)):
    ttv_type=train_test_validate()
    img=cv2.imread(FOLDER+filenames[i])
    new_img=manipulate(img)
    dst=DEST+ttv_type+"/"+names[i]+".jpg"
    category=categorize(names[i])
    
    data_long.append([ttv_type,dst,category])
    
    if ttv_type=="TEST":
        data_short_TEST.append([category])
    elif ttv_type=="TRAIN":
        data_short_TRAIN.append([category])
    else:
        data_short_TRAIN.append([category])
    
    cv2.imwrite(dst,img=new_img)
    # cv2.imshow("img",new_img)
    # cv2.waitKey(0)
    # cv2.imshow("img",img)
    # cv2.waitKey(0)
    # print(dst)
os.makedirs(DEST+"labels")

with open(DEST+"labels/long.csv",'w+',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data_long)
    
with open(DEST+"labels/TRAIN.csv",'w+',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data_short_TRAIN)
    
with open(DEST+"labels/TEST.csv",'w+',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data_short_TEST)
    
with open(DEST+"labels/VALIDATE.csv",'w+',newline='') as file:
    writer=csv.writer(file)
    writer.writerows(data_short_VALIDATE)