from PIL import Image
import numpy as np

# Đọc ảnh
image = Image.open('D:\\Nhap\\mat_pj\\cho.jpg')

# Chuyển đổi ảnh thành mảng numpy
img_array = np.array(image)
print(img_array)
print(img_array.shape)
# Lấy giá trị trung bình của từng pixel trên kênh màu
gray_img_array = np.mean(img_array, axis=2, dtype=np.uint8)
print(gray_img_array)
# Chuyển đổi lại mảng numpy thành đối tượng image
gray_image = Image.fromarray(gray_img_array)

# Xuất ra ảnh đã được giảm số chiều
gray_image.show()


