import numpy as np

def row_echelon_form_0(A):
    """
    Chuyển ma trận A về dạng ma trận bậc thang
    """
    # Khởi tạo ma trận bậc thang
    B = np.copy(A).astype(float)
    rows, cols = B.shape
    pivot_row = 0
    
    # Duyệt qua từng cột của ma trận
    for j in range(cols):
        # Tìm phần tử khác không đầu tiên của cột j trong các hàng từ pivot_row đến hàng cuối cùng
        pivot = 0
        for i in range(pivot_row, rows):
            if B[i, j] != 0:
                pivot = B[i, j]
                break
        
        # Nếu không tìm thấy phần tử khác không đầu tiên của cột j, bỏ qua cột này
        if pivot == 0:
            continue
        
        # Chia hàng chứa phần tử khác không đầu tiên của cột j cho phần tử đó
        B[pivot_row, :] = B[pivot_row, :] / pivot
        
        # Loại bỏ các phần tử khác không trong cột j của các hàng khác
        for i in range(pivot_row + 1, rows):
            factor = B[i, j] / B[pivot_row, j]
            B[i, :] = B[i, :] - B[i,j] * B[pivot_row, :]
        
        # Tăng pivot_row lên 1 để xử lý hàng tiếp theo
        pivot_row += 1
    
    return B
