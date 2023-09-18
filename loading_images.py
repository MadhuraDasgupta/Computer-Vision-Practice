import cv2

img = cv2.imread('MyProject/Profile Photo.jpg', 0)
img = cv2.resize(img, (200, 200))
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('new_image.jpg', img)
#img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
