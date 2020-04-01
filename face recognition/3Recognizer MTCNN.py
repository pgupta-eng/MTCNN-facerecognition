import cv2 as cv
import numpy as np
from mtcnn.mtcnn import MTCNN
detector = MTCNN()

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('Trainer/trainer.yml')

cascadePath = 'C:\PYTHON 3.7\haarcascades\haarcascade_frontalface_default.xml'
faceCascade = cv.CascadeClassifier(cascadePath)

cam = cv.VideoCapture('c:\sample12.mp4')

font = cv.FONT_HERSHEY_SIMPLEX

while(True):
    __, frame = cam.read()
    result = detector.detect_faces(frame)
    if result != []:
        for person in result:
            bounding_box = person['box']
            keypoints = person['keypoints']
    
            cv.rectangle(frame,
                          (bounding_box[0], bounding_box[1]),
                          (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                          (0,155,255),
                          2)
            gray=cv.cvtColor(frame[bounding_box[1]:bounding_box[1] + bounding_box[3],bounding_box[0]:bounding_box[0] + bounding_box[2]], cv.COLOR_BGR2GRAY)
            Id, conf = recognizer.predict(gray)
            print(Id, conf)
            if(conf<60):
                if(Id==1):
                    Id='Jay'
                elif(Id==2):
                    Id='Rudra'
            else:
                Id='Unknown'

            cv.putText(frame,str(Id),(bounding_box[0], bounding_box[1]),font,2,(0,0,255),2)
            cv.imshow('frame',frame)
    if(cv.waitKey(10)==ord('q')):
        break
cam.release()
cv.destroyAllWindows()
