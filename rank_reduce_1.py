import cv2
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import sys

# Đọc ảnh vào
img = cv2.imread('D:\\Nhap\\mat_pj\\hot-girl_9.jpg')

# Chuyển đổi ảnh thành ma trận numpy
img_np = np.array(img)
print(sys.getsizeof(img_np))
# Khởi tạo đối tượng PCA với số lượng thành phần chính là 50
pca = PCA(n_components=1)

# Trích xuất các thành phần chính của ma trận ảnh
img_pca = pca.fit_transform(img_np.reshape(-1,3))
print(sys.getsizeof(img_pca))
print(img_pca.shape)

# Giảm số chiều của ma trận ảnh
img_pca = pca.inverse_transform(img_pca).astype(np.uint8)



# Reshape lại chiều của img_pca
img_pca = img_pca.reshape(img_np.shape)

# Hiển thị ảnh gốc
plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# Hiển thị ảnh đã được giảm số chiều
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(img_pca, cv2.COLOR_BGR2RGB))

# Hiển thị plot
plt.show()