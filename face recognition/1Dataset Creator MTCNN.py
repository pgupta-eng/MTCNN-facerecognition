import cv2
import numpy as np
from mtcnn.mtcnn import MTCNN
detector = MTCNN()

cap = cv2.VideoCapture('c:/sample10.mp4')

id=input('Enter Your ID: ')
sampleNo=0

while(1):
    __, frame = cap.read()
    result = detector.detect_faces(frame)
    if result != []:
        for person in result:
            bounding_box = person['box']
            
            sampleNo=sampleNo+1
            cv2.imwrite('Dataset/User.'+str(id)+'.'+str(sampleNo)+'.jpg',frame[bounding_box[1]:bounding_box[1] + bounding_box[3],bounding_box[0]:bounding_box[0] + bounding_box[2]])
            cv2.rectangle(frame,
                              (bounding_box[0], bounding_box[1]),
                              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                              (0,155,255),2)
            
        cv2.imshow('frame',frame)
        if((cv2.waitKey(1)==ord('q'))):
            break
cam.release()
cv2.destroyAllWindows
