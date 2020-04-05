# this is the library we are using (opencv)
import cv2
import alglib.hsv_filter as hsv_filter


# some debugging stuff
print(cv2.__version__)
print("starting vision")

# open up the first (0) camera attached, if you have more than one you might
# need to change this
cap = cv2.VideoCapture(0)
cap.set(3, 1080)
cap.set(4, 720)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # do _stuff_ to the captured frame
    mask = hsv_filter.hsv_mask(frame)

    # look for the largest contour in the image
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    # apply the filter to the frame
    fitlered_frame = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2, 2)

    # show the frame that we have captured
    cv2.imshow('Captured Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break