# this is the library we are using (opencv)
import cv2
# numpy is a pretty neat library for working with maths stuff
# without knowing maths
import numpy as np

# lets do this in a function


def hsv_mask(frame):

    # the 'translation' from Red Green Blue to Hue Saturation Value
    colour_space = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # the lower bound of colours we want to pass
    #                 H   S    V
    lower = np.array([18, 35, 137], np.uint8)

    # the upper bound of colours we want to pass
    #                 H    S    V
    upper = np.array([46, 222, 253], np.uint8)

    # produces a mask that is only of the colours we have chosen
    mask = cv2.inRange(colour_space, lower, upper)

    return mask
