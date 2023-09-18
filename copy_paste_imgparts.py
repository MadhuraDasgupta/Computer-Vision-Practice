import cv2

img = cv2.imread('MyProject/Profile Photo.jpg', 1)

tag = img[200:250, 100:150]
img[10:60, 50:100]=tag

img=cv2.resize(img, (200, 200))
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
