import numpy as np

# Tạo ma trận A kích thước 4x3
A = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9], [4, 8, 12]])

# Phân tích ma trận A bằng SVD
U, S, VT = np.linalg.svd(A)

# Giảm rank của ma trận A từ 3 xuống 2 bằng cách loại bỏ thành phần chính thứ ba
A_new = U[:, :2] @ np.diag(S[:2]) @ VT[:2, :]

# In ra ma trận A mới
print("Ma trận A mới:")
print(A_new)