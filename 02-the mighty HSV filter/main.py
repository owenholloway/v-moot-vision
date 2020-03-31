#this is the library we are using (opencv)
import cv2
#numpy is a pretty neat library for working with maths stuff without knowing maths
import numpy as np
import alglib.hsv_filter as hsv_filter


#some debugging stuff
print (cv2.__version__)
print ("starting vision")

#open up the first (0) camera attached, if you have more than one you might need to change this
cap = cv2.VideoCapture(0)
cap.set(3,1080)
cap.set(4,720)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # do _stuff_ to the captured frame
    mask = hsv_filter.hsv_mask(frame)

    fitlered_frame = cv2.bitwise_and(frame, frame, mask=mask)

    # Show the frame that we have captured
    cv2.imshow('Captured Video', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Mask', fitlered_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
