import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))
cucumber=cv2.VideoCapture(0)
time.sleep(2)
bg=0

for i in range(60):
    ret,bg=cucumber.read()

bg=np.flip(bg,axis=1)

while(cucumber.isOpened()):
    ret,img=cucumber.read()
    if not ret:
        break
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,120,50])
    upper_red=np.array([10,255,255])
    mask_1=cv2.inRange(hsv,lower_red,upper_red)

    lower_red=np.array([170,120,70])
    upper_red=np.array([180,255,255])
    mask_2=cv2.inRange(hsv,lower_red,upper_red)
    
    mask_1=mask_1+mask_2
    cv2.imshow("mask_1",mask_1)
cucumber.release()
cv2.destroyAllWindows()