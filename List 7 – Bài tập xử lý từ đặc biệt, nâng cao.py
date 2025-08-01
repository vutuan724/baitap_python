# List 7 – Bài tập xử lý từ đặc biệt, nâng cao tư duy chuỗi

# 📘 Bài 1 – Lọc từ là chữ, viết hoa
chuoi = "python 123 ai code"
ds = []  # Danh sách chứa các từ hợp lệ
for tu in chuoi.split():  # Duyệt từng từ
    if tu.isalpha():  # Nếu từ toàn là chữ
        tu_moi = tu.upper()  # Viết hoa
        ds.append(tu_moi)  # Thêm vào danh sách
print(ds)  # 👉 ["PYTHON", "AI", "CODE"]


# 📘 Bài 2 – Lọc và đảo ngược từ là chữ cái
chuoi = "python 123 ai code"
ds = []  # Danh sách kết quả
for tu in chuoi.split():  # Duyệt từng từ
    if tu.isalpha():  # Nếu từ toàn là chữ
        tu_moi = tu[::-1]  # Đảo ngược từ
        ds.append(tu_moi.upper())  # Viết hoa và thêm vào danh sách
print(ds)  # 👉 ["NOHTYP", "IA", "EDOC"]


# 📘 Bài 3 – Phân loại từ: chữ, số, mixed
chuoi = "python 123 abc123 78dog cat"   # Gán chuỗi đầu vào
ds = []                                 # List kết quả
for tu in chuoi.split():                # Duyệt từng từ trong chuỗi
    if tu.isalpha():                    # Nếu chỉ toàn chữ cái
        tu = "WORD"
    elif tu.isdigit():                  # Nếu chỉ toàn số
        tu = "NUM"
    else:                               # Nếu còn lại (có thể vừa số vừa chữ)
        if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):
            tu = "MIXED"                # Nếu có cả chữ và số
    ds.append(tu)                       # Thêm kết quả vào list
print(ds)                               # 👉 ["WORD", "NUM", "MIXED", "MIXED", "WORD"]


# 📘 Bài 4 – Lấy các từ MIXED (vừa chữ vừa số)
chuoi = "python 123 ai abc123 dog78 55abc code"
ds = []
for tu in chuoi.split():  # Duyệt từng từ
    if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):  # Nếu là MIXED
        ds.append(tu)
print(ds)  # 👉 ['abc123', 'dog78', '55abc']


# 📘 Bài 5 – Lấy số nguyên từ các từ là số
chuoi = "python 123 ai abc123 dog78 55abc 2025 code"
ds = []
for tu in chuoi.split():  # Duyệt từng từ
    if tu.isdigit():  # Nếu toàn số
        tu_moi = int(tu)  # Chuyển sang kiểu số nguyên
        ds.append(tu_moi)
print(ds)  # 👉 [123, 2025]


# 📘 Bài 6 – Đảo ngược các từ MIXED
chuoi = "python 123 ai abc123 dog78 55abc code"
ds = []
for tu in chuoi.split():
    if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):
        tu_moi = tu[::-1]  # Đảo ngược từ
        ds.append(tu_moi)
print(ds)  # 👉 ['321cba', '87god', 'cba55']


# 📘 Bài 7 – Đếm từng loại từ: chữ, số, mixed
chuoi = "python 123 ai abc123 dog78 55abc code"
dem = {"WORD": 0, "NUM": 0, "MIXED": 0}  # Biến đếm cho từng loại từ
for tu in chuoi.split():
    if tu.isalpha():
        dem["WORD"] += 1
    elif tu.isdigit():
        dem["NUM"] += 1
    elif any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):
        dem["MIXED"] += 1
print("WORD:", dem["WORD"])
print("NUM:", dem["NUM"])
print("MIXED:", dem["MIXED"])


# 📘 Bài 8 – Trích ký tự cuối của từ loại MIXED
chuoi = "hoc123 456 ai abc123 def456xyz ghi 2023dog"
ds = []  # Danh sách để lưu ký tự cuối của các từ loại MIXED
for tu in chuoi.split():
    if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):
        ds.append(tu[-1])   # Lấy ký tự cuối
kq = "".join(ds)  # Nối lại thành chuỗi kết quả
print(kq)  # 👉 "3zgd"


# 📘 Bài 9 – Trích ký tự đầu từ loại có chữ + ký tự đặc biệt (ko có số)
chuoi = "hoc!123 abc@ def$ ghi123 @code abc#"
ds = []
for tu in chuoi.split():
    co_chu = any(c.isalpha() for c in tu)          # Có chữ
    ko_so = not any(c.isdigit() for c in tu)       # Không có số
    co_db = any(not c.isalnum() for c in tu)       # Có ký tự đặc biệt
    if co_chu and co_db and ko_so:
        ds.append(tu[0])                           # Lấy ký tự đầu tiên
kq = "".join(ds)
print(kq)  # 👉 "ad@a"
