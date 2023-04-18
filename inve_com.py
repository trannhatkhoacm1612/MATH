import numpy as np

def transpose_matrix(matrix):
    # Lấy số hàng và số cột của ma trận
    row, col = len(matrix), len(matrix[0])
    # Khởi tạo ma trận kết quả với số hàng và số cột đảo ngược
    transpose = [[0 for j in range(row)] for i in range(col)]
    # Duyệt qua từng phần tử của ma trận và đổi chỗ vị trí
    for i in range(row):
        for j in range(col):
            transpose[j][i] = matrix[i][j]
    return transpose

def inverse_matrix(A):
    # Lấy số hàng và số cột của ma trận
    n = len(A)
    # Tính định thức của ma trận A
    det = np.linalg.det(A)
    # Kiểm tra xem ma trận có thể nghịch đảo hay không
    if det == 0:
        return None
    # Tính ma trận đồng nhất adj(A)
    adj = np.adjugate_matrix(A)
    # Tính nghịch đảo của định thức
    inv_det = 1.0 / det
    # Tính ma trận nghịch đảo A⁻¹
    inverse = [[adj[i][j] * inv_det for j in range(n)] for i in range(n)]
    return inverse
