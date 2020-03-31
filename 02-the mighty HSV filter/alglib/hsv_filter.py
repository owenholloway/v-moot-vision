#this is the library we are using (opencv)
import cv2
#numpy is a pretty neat library for working with maths stuff without knowing maths
import numpy as np

def hsv_mask(frame):

    lower=np.array([18, 35, 137], np.uint8)

    upper=np.array([46, 222, 253], np.uint8)

    colour_space = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(colour_space, lower, upper)

    return mask
