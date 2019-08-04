import cv2
import numpy as np

def nothing(x):
    pass

#trackbar
cv2.namedWindow("trackbar")
cv2.createTrackbar("L-H","trackbar",0,360,nothing)
cv2.createTrackbar("L-S","trackbar",0,255,nothing)
cv2.createTrackbar("L-V","trackbar",0,255,nothing)
cv2.createTrackbar("U-H","trackbar",179,360,nothing)
cv2.createTrackbar("U-S","trackbar",255,255,nothing)
cv2.createTrackbar("U-V","trackbar",255,255,nothing)


cap=cv2.VideoCapture(0)
back=cv2.imread('background.jpg')

while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    l_h=cv2.getTrackbarPos("L-H","trackbar")
    l_s=cv2.getTrackbarPos("L-S","trackbar")
    l_v=cv2.getTrackbarPos("L-V","trackbar")
    h_h=cv2.getTrackbarPos("U-H","trackbar")
    h_s=cv2.getTrackbarPos("U-S","trackbar")
    h_v=cv2.getTrackbarPos("U-V","trackbar")

    low=np.array([l_h,l_s,l_v])
    high=np.array([h_h,h_s,h_v])
#    low=np.array([0,118,180])
#    high=np.array([20,255,255])
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
