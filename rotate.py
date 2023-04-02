import cv2
import numpy as np

# Đọc ảnh gốc
img = cv2.imread(r'D:\Nhap\mat_pj\cho.jpg')

# Thiết lập kích thước ảnh mới
height, width = img.shape[:2]
new_height, new_width = height, width

# Ma trận Affine cho phép phép biến đổi affine tổng quát
# ở đây chúng ta sẽ thực hiện phép biến đổi tổng quát bằng cách kết hợp
# các phép biến đổi đơn giản: translation, scaling, rotation
# (tăng kích thước ảnh lên 2 lần, xoay 45 độ và di chuyển 50 pixel sang trái và 100 pixel lên trên)
M = np.float32([[2, 0, -50], [0, 2, -100]])
theta = 45
s = 1.0

# Lấy ma trận quay
R = cv2.getRotationMatrix2D((width / 2, height / 2), theta, s)

# Tạo ma trận Affine cho phép scaling và rotation
M_affine = np.zeros((2, 3))
M_affine[:, :2] = R[:, :2]
M_affine[:, 2] = M[:, 2]

# Tạo ma trận Affine cho phép translation
M_translation = np.float32([[1, 0, 50], [0, 1, 100]])

# Áp dụng phép biến đổi affine
transformed_img = cv2.warpAffine(img, M_affine, (new_width, new_height))
transformed_img = cv2.warpAffine(transformed_img, M_translation, (new_width, new_height))

# Hiển thị ảnh gốc và ảnh đã biến đổi
cv2.imshow('Original Image', img)
cv2.imshow('Transformed Image', transformed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
