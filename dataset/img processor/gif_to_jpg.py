import os
from PIL import Image

filenames = next(os.walk("../images/train_masks/"), (None, None, []))[2]
names=[]
for i in filenames:
    names.append(i.split(".")[0])
        
os.makedirs("../images/new_masks")        


for i in range(len(filenames)):
    img=Image.open("../images/train_masks/"+filenames[i]).convert('RGB')
    # print(img)
    img.save("../images/new_masks/"+names[i]+".jpg")