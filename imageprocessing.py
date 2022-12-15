import cv2;
import face_recognition;
import numpy as np;
import os;
from datetime import datetime
import pickle



def findencodings(images):
    encodinglist=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodinglist.append(encode)
    return encodinglist




def markattendance(name):
    f=open("attendance.csv","r+")
    mydatalist=f.readlines()
    namelist=[]
    
    for line in mydatalist:
        entry=line.split(',')
        namelist.append(entry[0])
    if name not in namelist:
        now=datetime.now()
        
        f.writelines(f'\n{name},{now}')        
        
        
path="attendence_dataset"
images=[]
classnames=[]
mylist=os.listdir(path)
#print(mylist)

for cls in mylist:
    curimg=cv2.imread(f'{path}/{cls}')
    images.append(curimg)
    classnames.append(os.path.splitext(cls)[0])
    
#print(classnames)
encodelistknown=findencodings(images)



print(len(encodelistknown))
print('encoding complete')

encodeFile = open('encodePickle', 'ab')
pickle.dump(encodelistknown, encodeFile)
encodeFile.close()







    
    
    
                          

