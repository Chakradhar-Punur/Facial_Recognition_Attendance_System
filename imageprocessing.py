import cv2;
import face_recognition;
import numpy as np;
import os;
from datetime import datetime
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

cap=cv2.VideoCapture(0)
while True:
    success,img=cap.read()
    imgs=cv2.resize(img,(0,0),None,0.25,0.25)
    imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
    
    
    facescurframe=face_recognition.face_locations(imgs)
    encodingscurframe=face_recognition.face_encodings(imgs,facescurframe)
    
    for encodeface,faceloc in zip(encodingscurframe,facescurframe):
        matches=face_recognition.compare_faces(encodelistknown,encodeface)
        facedistance=face_recognition(encodelistknown,encodeface) 
        matchindex=np.argmin(facedistance)
        
        if matches[matchindex]:
            name=classnames[matchindex]
           # print(name)
            y1,x2,y2,x1=faceloc
            y1,x2,y2,x1=y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
            cv2.rectangle(img,(x1,y1-35),(x2,y2),(255,0,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
            markattendance(name)
            
    cv2.imshow('Webcam',img)
    cv2.waitkey(1)
    
    
    
                          

