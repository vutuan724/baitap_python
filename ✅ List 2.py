""" 
📘 TÓM TÁT HÀM VÀ CÚ PHÁP (List 2)

| Hàm / Cú pháp     | Tác dụng chính                             | Ví dụ cú pháp                            | Ghi nhớ nhanh                            |
|-------------------|--------------------------------------------|------------------------------------------|------------------------------------------|
| `.strip()`        | Xoá khoảng trắng ở đầu và cuối chuỗi       | `s.strip()`                              | Dọn chuỗi sạch ở đầu/cuối                |
| `.replace(a, b)`  | Thay tất cả `a` thành `b` trong chuỗi       | `s.replace(",", "-")`                  | Thay ký tự nhanh                         |
| `.split()`        | Tách chuỗi thành danh sách phần tử         | `s.split()`                              | Tách theo khoảng trắng                   |
| `.capitalize()`   | Viết hoa chữ cái đầu của chuỗi             | `ten.capitalize()`                       | Viết hoa 1 chữ đầu                       |
| `.join(ds)`       | Nối list thành chuỗi, chen ký tự giữa      | " ".join(ds)                            | Ghép danh sách thành chuỗi               |
| `list.append(x)`  | Thêm phần tử `x` vào danh sách              | `ds.append(i)`                           | Thêm phần tử vào cuối list               |
| `ds[:-1]`         | Lấy tất cả phần tử trừ phần tử cuối        |                                          | Dùng để lấy họ và tên đệm                |
| `ds[-1]`          | Lấy phần tử cuối danh sách (ví dụ: tên)    |                                          | Luôn là phần tử cuối                     |
"""

# 🦩 Bài 10.1: Viết hoa tên người dùng
print("\nBài 10.1: Viết hoa tên người dùng")
chuoi = input("Nhập tên dạng thường, cách nhau bằng dấu _: ")

# Bước 1: Xoá khoảng trắng ở đầu và cuối chuỗi
chuoi = chuoi.strip()

# Bước 2: Thay dấu gạch dưới bằng khoảng trắng
chuoi = chuoi.replace("_", " ")

# Bước 3: Tách chuỗi thành danh sách các từ
chuoi_dachia = chuoi.split()

# Bước 4: Viết hoa chữ cái đầu mỗi từ
hoa_danh_sach = []
for tu in chuoi_dachia:
    tu_hoa = tu.capitalize()        # Viết hoa chữ đầu
    hoa_danh_sach.append(tu_hoa)    # Thêm vào danh sách
    # hoa_danh_sach.append(tu.capitalize())  # Viết gọn nếu đã quen

# Bước 5: Ghép danh sách thành chuỗi hoàn chỉnh
ket_qua = " ".join(hoa_danh_sach)
print("Tên đã chuẩn hoá:", ket_qua)

# 🔍 Bài 10.2: Tách họ - tên đệm - tên
print("\nBài 10.2: Tách họ - tên đệm - tên")
chuoi = input("Nhập lại họ tên: ")

# Bước 1: Làm sạch chuỗi
chuoi = chuoi.strip()
chuoi = chuoi.replace("_", " ")

# Bước 2: Tách chuỗi thành danh sách từ
danh_sach = chuoi.split()

# Bước 3: Viết hoa từng từ
hoa_danh_sach = []
for tu in danh_sach:
    tu_hoa = tu.capitalize()            # Viết hoa chữ đầu
    hoa_danh_sach.append(tu_hoa)        # Thêm vào danh sách
    # hoa_danh_sach.append(tu.capitalize())  # Viết gọn nếu đã quen

# Bước 4: Tách họ và tên đệm, tên riêng
ho_va_dem = " ".join(hoa_danh_sach[:-1])  # Lấy tất cả trừ phần cuối
ten = hoa_danh_sach[-1]                   # Lấy phần tử cuối (tên)
print("Họ và tên đệm:", ho_va_dem)
print("Tên:", ten)

# 🔪 Bài 10.3: Đếm số từ trong tên
print("\nBài 10.3: Đếm số từ trong tên")
chuoi = input("Nhập họ tên: ")

# Bước 1: Làm sạch và chuẩn hóa
chuoi = chuoi.strip()
chuoi = chuoi.replace("_", " ")
danh_sach = chuoi.split()

# Bước 2: Viết hoa từng từ
hoa_danh_sach = []
for tu in danh_sach:
    tu_hoa = tu.capitalize()
    hoa_danh_sach.append(tu_hoa)

# Bước 3: Đếm số phần tử trong danh sách
so_tu = len(hoa_danh_sach)
print("Số từ trong tên:", so_tu)

# 💡 Bài 10.4: Tạo username từ tên
print("\nBài 10.4: Tạo username từ tên")
chuoi = input("Nhập họ tên: ")

# Bước 1: Làm sạch và chuẩn hoá chuỗi
chuoi = chuoi.strip()
chuoi = chuoi.replace("_", " ")
danh_sach = chuoi.split()

# Bước 2: Viết hoa chữ cái đầu mỗi từ
hoa_danh_sach = []
for tu in danh_sach:
    tu_hoa = tu.capitalize()
    hoa_danh_sach.append(tu_hoa)

# Bước 3: Tạo username
ho = hoa_danh_sach[0].lower()      # Lấy họ và chuyển thành chữ thường
ten = hoa_danh_sach[-1].lower()    # Lấy tên và chuyển thành chữ thường
username = ho + "." + ten + "@gmail.com"
print("Username gợi ý:", username)

# 🔄 Bài 10.5: In từng từ đã viết hoa
print("\nBài 10.5: In từng từ đã viết hoa")
chuoi = input("Nhập họ tên: ")

# Bước 1: Làm sạch và chuẩn hóa chuỗi
chuoi = chuoi.strip()
chuoi = chuoi.replace("_", " ")
danh_sach = chuoi.split()

# Bước 2: Viết hoa từng từ
hoa_danh_sach = []
for tu in danh_sach:
    tu_hoa = tu.capitalize()           # Viết hoa chữ đầu mỗi từ
    hoa_danh_sach.append(tu_hoa)       # Thêm vào danh sách
    # hoa_danh_sach.append(tu.capitalize())  # Viết gọn nếu quen

# Bước 3: In từng từ
for tu in hoa_danh_sach:
    print(tu)
