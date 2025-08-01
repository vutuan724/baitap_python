# (Đầu file của bạn, nơi bạn định nghĩa các hàm khác nếu có)
# Ví dụ:
# def them_san_pham(...):
#     pass
# ==== ĐỊNH NGHĨA HÀM SUA_SAN_PHAM CỦA BẠN (KHÔNG THAY ĐỔI) ====
def sua_san_pham(danh_sach_sp):
    while True:
        sp_can_sua = input("Bạn muốn sửa sản phẩm nào hoặc dừng nhấn n: ")
        if sp_can_sua.lower() == "n": 
            return
        sp_can_sua = sp_can_sua.strip()
        ten_chuan =  sp_can_sua.split()
        sp_can_sua = " ".join(ten_chuan)
        sp_can_sua = sp_can_sua.lower()
        tim_thay_sp = None
        for item in danh_sach_sp:
            if sp_can_sua == item["ten_hang"].lower(): 
                tim_thay_sp = item
                break            
        if tim_thay_sp:
            print(f"Đã tìm thấy sản phẩm '{tim_thay_sp['ten_hang']}'.")
            break # Thoát vòng lặp while True để chuyển sang bước sửa sản phẩm
        else:
            print(f"Không tìm thấy sản phẩm có tên '{sp_can_sua}'. Vui lòng nhập lại.")
            
    if tim_thay_sp:
        thong_tin_sua = input(f"Bạn muốn sửa thông tin gì của sản phẩm '{sp_can_sua}' (ten_hang, gia_hang, so_luong_hang) hoặc dừng nhấn n: ")
        if thong_tin_sua.lower() == 'n':
            return       
        if thong_tin_sua == "ten_hang":
            ten_moi = input("Nhập tên mới cần sửa: ")
            ten_moi = ten_moi.strip()
            ten_chuan =  ten_moi.split()
            ten_moi = " ".join(ten_chuan)
            ten_moi = ten_moi.lower()
            tim_thay_sp["ten_hang"] = ten_moi
            print(f"Đã sửa tên sản phẩm thành '{ten_moi}'.") 

        elif thong_tin_sua == "gia_hang":
            while True:
                try:
                    gia_moi = float(input("Nhập giá cần sửa: "))
                    if gia_moi <= 0 :
                        print("Giá phải là số lớn hơn 0. Vui lòng nhập lại.")
                        continue
                    break
                except ValueError:
                    print("Lỗi: Vui lòng nhập một số hợp lệ.")

            tim_thay_sp["gia_hang"]= gia_moi
            print(f"Đã sửa giá sản phẩm thành '{gia_moi}'.")
        elif thong_tin_sua == "so_luong_hang":
            while True:
                try:
                    so_luong_moi = float(input("Nhập số lượng muốn sửa: "))
                    if so_luong_moi <= 0:
                        print("Số lượng phải là số lớn hơn 0. Vui lòng nhập lại.")
                        continue
                    break # nếu giá >0 thì thoát vòng lập
                except ValueError:
                    print("Lỗi: Vui lòng nhập một số hợp lệ.")
            tim_thay_sp["so_luong_hang"]= so_luong_moi
            print(f"Đã sửa số lượng sản phẩm thành '{so_luong_moi}'.")

            
# ==== KẾT THÚC ĐỊNH NGHĨA HÀM SUA_SAN_PHAM ====


# ============ KHỐI KIỂM TRA HÀM SUA_SAN_PHAM (kiem_tra_ham_sua_sp) ============

print("\n===== BẮT ĐẦU KIỂM TRA HÀM SỬA SẢN PHẨM =====")

# Tạo dữ liệu test mẫu
danh_sach_sp_kiem_tra = [
    {"ten_hang": "Ao So Mi", "gia_hang": 250000, "so_luong_hang": 10},
    {"ten_hang": "Quan Jean", "gia_hang": 450000, "so_luong_hang": 5},
    {"ten_hang": "Giay The Thao", "gia_hang": 700000, "so_luong_hang": 3}
]

print("\n--- DANH SÁCH SẢN PHẨM TRƯỚC KHI GỌI SỬA ---")
for sp in danh_sach_sp_kiem_tra:
    print(sp)
print("-" * 30)

# Gọi hàm sua_san_pham với dữ liệu test
print("\n>>> ĐANG CHẠY CHỨC NĂNG SỬA SẢN PHẨM (TEST) <<<")
sua_san_pham(danh_sach_sp_kiem_tra) # Đây là cách bạn gọi hàm để test

print("\n--- DANH SÁCH SẢN PHẨM SAU KHI GỌI SỬA ---")
for sp in danh_sach_sp_kiem_tra:
    print(sp)
print("-" * 30)

print("\n===== KẾT THÚC KIỂM TRA HÀM SỬA SẢN PHẨM =====")

# (Phần code chương trình chính của bạn, ví dụ: menu chọn chức năng)
# if __name__ == "__main__":
#     # Một danh sách sản phẩm thật để chạy chương trình chính
#     danh_sach_san_pham_chinh = [] 
#     # ... các lựa chọn menu chính gọi các hàm khác ...