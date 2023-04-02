import cv2
import numpy as np

img = cv2.imread(r'D:\Nhap\mat_pj\hot-girl_9.jpg')
print(img.shape)
rows, cols, _ = img.shape
alpha = 1

phi = 30.0
sin_phi = np.sin(phi)
cos_phi = np.cos(phi)
M = np.float32([[cos_phi, -sin_phi, 0], [sin_phi, cos_phi, 0], [0, 0, 1]]) # matrix transformation

img_output = np.zeros_like(img)
print(img_output)
for i in range(rows):
    for j in range(cols):
        x, y, _ = np.dot(M, [j, i, 1])
        if x >= 0 and y >= 0 and x < cols and y < rows: # fill output : mất pixel 
            img_output[i, j] = img[int(y), int(x)]


cv2.imshow('Input Image', img)
cv2.imshow('Output Image', img_output)
cv2.waitKey(0)
cv2.destroyAllWindows()
