import cv2
import numpy as np

cap=cv2.VideoCapture(0)
back=cv2.imread('background.jpg')

while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    low=np.array([0,118,180])
    high=np.array([20,255,255])
    mask=cv2.inRange(hsv,low,high)
    print(mask)
    mask_inv=cv2.bitwise_not(mask)
    
    result=cv2.bitwise_and(back,back,mask=mask)
    result_inv=cv2.bitwise_and(frame,frame,mask=mask_inv)
    invisible=result+result_inv
    
    cv2.imshow('inv',invisible)
        
    blur=cv2.GaussianBlur(mask,(15,15),0)

    if cv2.waitKey(1)==27:#press esc to exit
        break;

cap.release()
cv2.destroyAllWindows()
