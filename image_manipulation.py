import cv2
import random

img = cv2.imread('MyProject/Profile Photo.jpg', 1)

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(1, 255), random.randint(1, 255), random.randint(1,255)]

img = cv2.resize(img, (200, 200))
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

