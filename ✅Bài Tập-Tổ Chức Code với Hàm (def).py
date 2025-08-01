# =====================================================================================
# BÀI TẬP: TỔ CHỨC CODE VỚI HÀM (DEF) - HỆ THỐNG QUẢN LÝ SẢN PHẨM ĐƠN GIẢN
# =====================================================================================

# --- PHẦN 1: ĐỊNH NGHĨA HÀM NHẬP TÊN SẢN PHẨM ---
def ten_san_pham():
    ten = input("Nhập tên SP (Nhập 'n' để dừng): ")
    if ten.lower() == "n":
        return None
    ten = ten.strip()
    ten_chuan = ten.split()
    ten = " ".join(ten_chuan)
    ten = ten.title()
    return ten

# --- PHẦN 2: ĐỊNH NGHĨA HÀM NHẬP GIÁ SẢN PHẨM ---
def lay_gia_sp():
    while True:
        gia = input("Nhập giá SP : ")
        try:
            gia = float(gia)
            if gia <= 0:
                print("Yêu cầu nhập giá là số dương.")
                continue
            else:
                break
        except ValueError:
            print("Giá không hợp lệ. Vui lòng nhập giá là số.")
    return gia

# --- PHẦN 3: ĐỊNH NGHĨA HÀM NHẬP SỐ LƯỢNG SẢN PHẨM ---
def lay_sl_sp():
    while True:
        so_luong = input("Nhập số lượng SP : ")
        try:
            so_luong = float(so_luong)
            if so_luong <= 0:
                print("Yêu cầu nhập số lượng là số dương.")
                continue
            else:
                break
        except ValueError:
            print("Số lượng không hợp lệ. Vui lòng nhập số lượng là số.")
    return so_luong

# --- PHẦN 4: ĐỊNH NGHĨA HÀM GOM THÔNG TIN SẢN PHẨM MỚI ---
def nhap_sp_moi():
    ten = ten_san_pham()
    if ten is None:
        return None
    gia = lay_gia_sp()
    so_luong = lay_sl_sp()
    sp_dict = {
        "ten_hang": ten,
        "gia_hang": gia,
        "so_luong_hang": so_luong
    }
    return sp_dict

# --- PHẦN 5: ĐỊNH NGHĨA HÀM HIỂN THỊ DANH SÁCH SẢN PHẨM ---
# (Phần này chúng ta đang làm và đã hoàn thành việc lấy các biến)
def hien_thi_ds_sp(danh_sach):
    if not danh_sach:
        print("Danh sách sản phẩm trống.")
        return
    for item in danh_sach:
        ten_sp = item["ten_hang"]
        gia_sp = item["gia_hang"]
        so_sp = item["so_luong_hang"]
        # Dòng print() sẽ được đặt ở đây để hiển thị từng sản phẩm
        print(f"Tên sản phẩm là: {ten_sp}, giá của SP là: {gia_sp}, và số lượng SP là: {so_sp}")

#=====> phần 6 :Sửa sản phẩm
def sua_san_pham(danh_sach_sp):
    sp_can_sua = input("Bạn muốn sửa sản phẩm nào hoặc dừng nhấn n: ")
    if sp_can_sua == "n":
        return
                                                                                 # Bước 2: Tìm sản phẩm trong danh sách
                                                                                 # Cần một biến để lưu sản phẩm tìm thấy và một cờ hiệu
    tim_thay_sp = None                                                           # Ban đầu chưa tìm thấy sản phẩm nào
    for item in danh_sach_sp:
        if sp_can_sua == item["ten_hang"]: 
            tim_thay_sp = item                                                    # Lưu lại dictionary sản phẩm tìm thấy
            break 
    if not tim_thay_sp :
        print("ko tìm thấy sản phẩm cần sửa") 
        return                                                                   # Thoát vòng lặp ngay khi tìm thấy sản phẩm đầu tiên             
    if tim_thay_sp:
        thong_tin_sua = input("bạn muốn sửa thông in gì trong {sp_can_sua} : ")
        if thong_tin_sua.lower() == 'n':
            return
        if thong_tin_sua == "ten_hang":
            ten_moi = input("nhập tên mới cần sửa :")
            tim_thay_sp["ten_hang"] = ten_moi
            print("đã sửa xong tên")
        elif thong_tin_sua == "gia_hang":
            gia_moi = float(input("Nhập giá cần sửa: "))
            tim_thay_sp["gia_hang"]= gia_moi
            print("đã sửa xong giá")
        elif thong_tin_sua == "so_luong_hang":
            so_luong_moi = float(input("nhập số lượng muốn sửa: "))
            tim_thay_sp["so_luong_hang"]= so_luong_moi
            print("đã sửa xong số lượng")    
print("sản phẩm đã dc sửa xong")   
    
# =====================================================================================
# PHẦN CHÍNH CỦA CHƯƠNG TRÌNH - NƠI CHƯƠNG TRÌNH BẮT ĐẦU THỰC THI
# =====================================================================================

ds_sp = [] # Danh sách rỗng để lưu trữ các sản phẩm
print("--- Bắt đầu nhập liệu sản phẩm mới ---")
print("Để dừng nhập sản phẩm, hãy gõ 'n' khi được yêu cầu nhập tên sản phẩm.")

while True:
    sp_moi = nhap_sp_moi()
    if sp_moi is None:
        print("Dừng nhập liệu.")
        break
    ds_sp.append(sp_moi)
    print(f"Đã thêm sản phẩm '{sp_moi['ten_hang']}'.")
    print("------------------------------------")

# --- GỌI HÀM HIỂN THỊ DANH SÁCH SẢN PHẨM SAU KHI ĐÃ NHẬP XONG ---
print("\n--- DANH SÁCH SẢN PHẨM ĐÃ NHẬP ---")
hien_thi_ds_sp(ds_sp) # <--- Dòng này sẽ gọi hàm hiển thị
print("--- KẾT THÚC DANH SÁCH ---")

# =====================================================================================
# KẾT THÚC CHƯƠNG TRÌNH
# =====================================================================================