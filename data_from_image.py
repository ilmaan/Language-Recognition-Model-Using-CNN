import cv2
import numpy as np
import os



IMG_SIZE=96


tp, rg, bt, lf = 100, 150, 400, 450

esc='**'

a=''

dataset_folder=input('Enter Folder Name : ')

try:
    os.mkdir(dataset_folder)
except:
    print('Containing folder is having same name ')

cam = cv2.VideoCapture(0)

while(True):

    a=input(' enter name of label or ** to exit : ')

    if a==esc:
        break

    label_dir=str(dataset_folder)+'/'+str(a)
    print(label_dir)

    try:
        os.mkdir(label_dir)
    except Exception as e:
        print('Exception Occoured',e)

    i=0

    while(True):
        (t, frame) = cam.read()

        

        frame = cv2.flip(frame, 1)

        
        roi = frame[tp:bt, rg:lf]
        gray_scale = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        gray_scale = cv2.GaussianBlur(gray_scale, (7, 7), 0)

        gray_scale = cv2.resize(gray_scale, (IMG_SIZE,IMG_SIZE))

        cv2.imwrite("%s/%s/%d.jpg"%(dataset_folder,a,i),gray_scale)
        i+=1
        print(i)
        if i>300:
            break

        cv2.rectangle(frame, (lf, tp), (rg, bt), (0,255,0), 2)

        cv2.imshow("Video Feed 1", gray_scale)

        cv2.imshow("Video Feed", frame)
        # observe the keyprss by the user
        keyprss = cv2.waitKey(1)

        if keyprss == 27:
            break

cam.release()
cv2.destroyAllWindows()
