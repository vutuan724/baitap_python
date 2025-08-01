# Tên file: bai_tap_ham_moi.py

# ĐỊNH NGHĨA HÀM
def lay_ten_san_pham():
    # Hỏi người dùng nhập tên
    ten = input("Nhập tên SP (gõ 'n' để dừng): ")
    
    # KIỂM TRA ĐIỀU KIỆN DỪNG
    if ten.lower() == "n":
        return None # Trả về None nếu người dùng muốn dừng nhập
    
    return ten # Trả về tên đã nhập nếu không phải 'n'

# GỌI HÀM VÀ SỬ DỤNG KẾT QUẢ
print("--- CHƯƠNG TRÌNH BẮT ĐẦU ---")

ten_sp = lay_ten_san_pham() # Gọi hàm và lưu kết quả vào biến 'ten_sp'

if ten_sp is None: # Kiểm tra nếu hàm trả về None
    print("Bạn đã chọn dừng nhập liệu.")
else:
    print(f"Bạn vừa nhập tên sản phẩm: {ten_sp}")

print("--- CHƯƠNG TRÌNH KẾT THÚC ---")