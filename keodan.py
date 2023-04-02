import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"D:\Nhap\mat_pj\hot-girl_9.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
m,n,_ = img.shape
print(m)
print(n)
# 3 by 3 matrix as it is required for the OpenCV library, don't worry about the details of it for now.
phi = 30.0
sin_phi = np.sin(phi)
cos_phi = np.cos(phi)
M = np.float32([[cos_phi, -sin_phi, 0], [sin_phi, cos_phi, 0], [0, 0, 1]])
image_rotated_sheared = cv2.warpPerspective(img, M, (int(n), int(m)))
plt.imshow(image_rotated_sheared)
plt.show()