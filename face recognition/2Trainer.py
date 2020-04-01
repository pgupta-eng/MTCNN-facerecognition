import cv2 as cv
import os
import numpy as np
from PIL import Image

recognizer = cv.face.LBPHFaceRecognizer_create()
detector = cv.CascadeClassifier('c:\PYTHON 3.7\haarcascades\haarcascade_frontalface_default.xml')

def getImagesAndLables(path):
    imagePaths=[os.path.join(path, f) for f in os.listdir(path)]
    faceSamples=[]
    Ids=[]
    for imagePath in imagePaths:

        if(os.path.split(imagePath)[-1].split('.')[-1]!='jpg'):
            continue
        
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage, 'uint8')
        '''
        print(imageNp)
        cv.imshow('image',imageNp)
        cv.waitKey(1)'''
        Id=int(os.path.split(imagePath)[-1].split('.')[1])
        faceSamples.append(imageNp)
        Ids.append(Id)
        '''
        print(Id)
        faces=detector.detectMultiScale(imageNp)
        print(faces)
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+h])
            Ids.append(Id)
    print(faceSamples,Ids)'''
    return faceSamples,Ids


faces,Ids = getImagesAndLables('Dataset')
recognizer.train(faces, np.array(Ids))
recognizer.save('Trainer/trainer.yml')
