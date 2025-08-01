"""
📘 TÓM TẮT HÀM VÀ CÚ PHÁP (ôn tập nhanh)

| Hàm / Cú pháp     | Tác dụng chính                             | Ví dụ cú pháp                           | Ghi nhớ nhanh                             |
|-------------------|--------------------------------------------|-----------------------------------------|-------------------------------------------|
| `.strip()`        | Xoá khoảng trắng ở đầu và cuối chuỗi       | `chuoi.strip()`                         | Dọn sạch chuỗi đầu/cuối                   |
| `.replace(a, b)`  | Thay thế tất cả `a` bằng `b` trong chuỗi    | `chuoi.replace(",", "-")`               | Đổi dấu hoặc ký tự nhanh                   |
| `.append(x)`      | Thêm `x` vào **cuối danh sách**             | `ds.append(kytu)`                       | Dùng với list, không phải chuỗi           |
| `.join(ds)`       | Nối danh sách `ds` thành chuỗi, chèn dấu    | `"-".join(ds)`                          | Chỉ dùng với danh sách, không dùng với str|
| `.capitalize()`   | Viết hoa chữ cái đầu của chuỗi              | `ten.capitalize()`                      | Chỉ viết hoa chữ cái đầu tiên              |
| `.split()`        | Tách chuỗi thành danh sách các phần tử      | `chuoi.split()`                         | Tách theo dấu cách (mặc định)              |
"""

# 🔁 Bài Tập Luyện Tập – Phần 1: List + Chuỗi (nâng cao dần)

# ▶️ Bài 6.1: Lọc chữ thường và nối bằng dấu cách
print("Bài 6.1: Lọc chữ in thường, nối bằng dấu cách")
chuoi = input("Nhập chuỗi: ")
ds = []
for ky_tu in chuoi:
    if ky_tu.islower():
        ds.append(ky_tu)
ket_qua = " ".join(ds)
print(ket_qua)

# ▶️ Bài 6.2: Lọc chữ HOA và nối bằng dấu gạch ngang
print("\nBài 6.2: Lọc chữ in HOA, nối bằng dấu -")
chuoi = input("Nhập chuỗi: ")
ds = []
for ky_tu in chuoi:
    if ky_tu.isupper():
        ds.append(ky_tu)
ket_qua = "-".join(ds)
print(ket_qua)

# ▶️ Bài 6.3: Thay thế tất cả dấu phẩy bằng dấu chấm phẩy
print("\nBài 6.3: Thay dấu , bằng dấu ;")
chuoi = input("Nhập chuỗi có dấu phẩy: ")
ket_qua = chuoi.replace(",", ";")
print(ket_qua)

# 🔐 Bài Tập Ôn Phần 2: .strip()

# ▶️ Bài 7.1: Xoá khoảng trắng đầu và cuối chuỗi
print("\nBài 7.1: .strip() loại bỏ khoảng trắng")
chuoi = input("Nhập chuỗi: ")
chuoi_moi = chuoi.strip()
print(chuoi_moi)

# ▶️ Bài 7.2: Kết hợp .strip() và .replace()
print("\nBài 7.2: .strip() kết hợp .replace()")
chuoi = input("Nhập chuỗi: ")
chuoi = chuoi.strip()
ket_qua = chuoi.replace(",", "-")
print(ket_qua)

# ▶️ Bài 7.3: .strip() rồi .replace(), làm từng bước
print("\nBài 7.3: .strip() rồi .replace(), làm từng bước")
chuoi = input("Nhập chuỗi: ")
chuoi_moi = chuoi.strip()
ket_qua = chuoi_moi.replace(",", "-")
print(ket_qua)

# 🔁 Bài 8.1: Thay thế nhiều dấu khác nhau
print("\nBài 8.1: Thay dấu , và . trong chuỗi")
chuoi = input("Nhập chuỗi: ")
ket_qua = chuoi.replace(",", "-").replace(".", ":")
print(ket_qua)

# 🆕 Bài 9.1: Làm sạch tên, viết hoa, tách họ - tên đệm - tên
print("\nBài 9.1: Xử lý tên người dùng")

# Bước 1: Chuỗi đầu vào có khoảng trắng và dấu _
chuoi = "   nguyen_thi_thu_trang   "

# Bước 2: Xoá khoảng trắng ở đầu và cuối chuỗi
chuoi_mot = chuoi.strip()

# Bước 3: Thay dấu _ bằng dấu cách
chuoi_hai = chuoi_mot.replace("_", " ")

# Bước 4: Tách chuỗi thành danh sách từ
chuoi_ba = chuoi_hai.split()

# Bước 5: Viết hoa chữ cái đầu mỗi từ
chuoi_hoa = []
for i in chuoi_ba:
    chuoi_hoa.append(i.capitalize())

# Bước 6: Tách họ và tên
ho_va_dem = " ".join(chuoi_hoa[:-1])
ten = chuoi_hoa[-1]

# Bước 7: In kết quả
print("Họ và tên đệm:", ho_va_dem)
print("Tên:", ten)
