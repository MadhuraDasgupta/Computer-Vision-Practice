import numpy as np
import cv2

# initializing the the videoCapture object cap
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # empty canvas
    image = np.zeros(frame.shape, np.uint8)
    
    # frame in 4 quadrants of the empty canvas image
    #image[:height//2, :width//2] = smaller_frame
    #image[height//2:, :width//2] = smaller_frame
    #image[:height//2, width//2:] = smaller_frame
    #image[height//2:, width//2:] = smaller_frame
    
    # first and third quadrants rotated
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

