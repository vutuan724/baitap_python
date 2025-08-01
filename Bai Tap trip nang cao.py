"""🔶 Bài tập: Làm sạch danh sách chuỗi nhập vào
📝 Đề bài:
Người dùng nhập vào một chuỗi gồm nhiều từ, cách nhau bằng dấu phẩy, nhưng có thể dư khoảng trắng ở mỗi từ.

▶️ Yêu cầu:

Tách chuỗi thành danh sách các từ.

Dùng .strip() để xoá khoảng trắng ở đầu/cuối từng từ."""

#  ✅ Mã hoàn chỉnh có chú thích:

print("Bài .strip() nâng cao – Làm sạch danh sách từ")

chuoi = "  táo , chuối  ,  cam , nho "

# Bước 1: Tách chuỗi thành danh sách tạm thời, có thể vẫn còn khoảng trắng
ds_tu = chuoi.split(",")

# Bước 2: Tạo danh sách mới, lưu các từ đã được .strip()
ds_sach = []

for tu in ds_tu:
    tu_sach = tu.strip()       # Xoá khoảng trắng đầu/cuối
    ds_sach.append(tu_sach)    # Thêm vào danh sách kết quả

# Bước 3: In danh sách sạch
print(ds_sach)
