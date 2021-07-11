import cv2
import numpy as np
import os

cap =cv2.VideoCapture(0)

while True:
    retrieve, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    