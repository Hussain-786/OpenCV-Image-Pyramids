import cv2

img = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)
pyrdown = cv2.pyrUp(gp[1])
cv2.imshow('pyrdown', pyrdown)
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)
cv2.imshow('original image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()