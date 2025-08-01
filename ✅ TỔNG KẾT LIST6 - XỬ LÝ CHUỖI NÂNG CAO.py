# ===============================
# ✅ TỔNG KẾT LIST6 - XỬ LÝ CHUỖI NÂNG CAO
# FULL CHÚ THÍCH TỪNG DÒNG (1–12)
# ===============================

# --- Bài 1 ---
# Viết hoa chữ cái đầu mỗi từ
chuoi = "python ai model"                # Gán chuỗi đầu vào
kq = []                                 # Tạo list rỗng để chứa kết quả
for tu in chuoi.split():                # Duyệt từng từ trong chuỗi (split trả về list từ)
    kq.append(tu.capitalize())          # capitalize: Viết hoa chữ đầu của mỗi từ, phần còn lại thường, rồi thêm vào kq
print(kq)                               # ['Python', 'Ai', 'Model']

# --- Bài 2 ---
# Lấy chữ cái đầu mỗi từ, ghép thành chuỗi, viết hoa
chuoi = "Nguyen Van Quang"              # Gán chuỗi đầu vào
kq = []                                 # List chứa chữ đầu mỗi từ
for tu in chuoi.split():                # Duyệt từng từ
    kq.append(tu[0].upper())            # Lấy ký tự đầu (chỉ số 0), viết hoa, thêm vào list
print("".join(kq))                      # join: Nối các ký tự đầu thành chuỗi NVQ

# --- Bài 3 ---
# Viết tắt tên đệm, giữ họ và tên
chuoi = "Pham Thi Minh Khoa"            # Chuỗi họ tên
ds = chuoi.split()                      # split() tách thành list: ['Pham', 'Thi', 'Minh', 'Khoa']
ho = ds[0]                              # Họ là phần tử đầu tiên
dem = ds[1:-1]                          # Tên đệm: các phần tử từ thứ 2 đến áp chót
ten = ds[-1]                            # Tên là phần tử cuối
dem_viettat = " ".join(d[0].upper() + "." for d in dem) # Viết tắt mỗi tên đệm: lấy ký tự đầu, viết hoa, thêm dấu chấm, ghép lại bằng dấu cách
print(f"{ho} {dem_viettat} {ten}")      # In kết quả dùng f-string: Pham T. M. Khoa

# --- Bài 4 ---
# Viết tắt toàn bộ bằng chữ cái đầu, cách nhau dấu chấm
chuoi = "Cộng hòa xã hội chủ nghĩa"     # Chuỗi đầu vào
kq = ".".join(word[0].upper() for word in chuoi.split()) # Duyệt từng từ, lấy ký tự đầu viết hoa, ghép bằng dấu chấm
print(kq)                               # In ra: C.H.X.H.C.N

# --- Bài 5 ---
# Viết hoa đầu từ + ' - ' + chữ cuối viết hoa
chuoi = "python ai model"               # Chuỗi đầu vào
kq = []                                 # List kết quả
for tu in chuoi.split():                # Duyệt từng từ
    tu_moi = tu.capitalize() + " - " + tu[-1].upper() # capitalize đầu, thêm " - ", thêm chữ cuối viết hoa
    kq.append(tu_moi)                   # Thêm vào list
print(kq)                               # ['Python - N', 'Ai - I', 'Model - L']

# --- Bài 6 ---
# Thay tất cả nguyên âm bằng dấu "*"
chuoi = "python ai model"               # Chuỗi đầu vào
nguyen_am = "aeiouyăâêôơưáàảãạ"         # Khai báo chuỗi chứa tất cả nguyên âm tiếng Việt
kq = []                                 # List kết quả
for tu in chuoi.split():                # Duyệt từng từ
    tu_moi = ""                         # Biến chứa từ đã xử lý
    for ch in tu:                       # Duyệt từng ký tự trong từ
        if ch.lower() in nguyen_am:     # Kiểm tra ký tự (dù hoa hay thường) có phải nguyên âm không
            tu_moi += "*"               # Nếu phải, thêm * vào tu_moi
        else:
            tu_moi += ch                # Không phải nguyên âm, giữ nguyên ký tự
    kq.append(tu_moi)                   # Thêm từ đã xử lý vào list
print(kq)                               # ['pyth*n', '*', 'm*d*l']

# --- Bài 7 ---
# Giữ chữ đầu/cuối (hoa), giữa là "*"
chuoi = "Python Model AI"               # Chuỗi đầu vào
kq = []                                 # List kết quả
for tu in chuoi.split():                # Duyệt từng từ
    if len(tu) == 1:                    # Nếu chỉ có 1 ký tự
        tu_moi = tu.upper()             # Viết hoa luôn
    elif len(tu) == 2:                  # Nếu từ có 2 ký tự
        tu_moi = tu[0].upper() + "*" + tu[1].upper() # Đầu, *, cuối đều viết hoa
    else:
        tu_moi = tu[0].upper() + "*" * (len(tu) - 2) + tu[-1].upper() # Đầu hoa, giữa là *, cuối hoa
    kq.append(tu_moi)                   # Thêm vào list
print(kq)                               # ['P****N', 'M***L', 'A*I']

# --- Bài 8 (chỉnh lại đúng, full chú thích) ---
# Viết hoa toàn bộ từ trừ ký tự cuối viết thường
chuoi = "lập trình chăm chỉ"            # Gán chuỗi đầu vào
kq = []                                # Tạo list rỗng để chứa kết quả
for tu in chuoi.split():               # Duyệt từng từ trong chuỗi (split trả về list từ)
    if len(tu) == 1:                   # Nếu từ chỉ có 1 ký tự
        tu_moi = tu.lower()            # Viết thường (không có phần đầu để viết hoa)
    else:
        dau = tu[:-1].upper()          # Lấy toàn bộ ký tự trừ ký tự cuối, viết hoa (upper)
        cuoi = tu[-1].lower()          # Lấy ký tự cuối, viết thường (lower)
        tu_moi = dau + cuoi            # Ghép lại thành từ đã xử lý
    kq.append(tu_moi)                  # Thêm vào list kết quả
print(kq)                              # ['LẬp', 'TRÌNh', 'CHĂm', 'CHỉ']

# --- Bài 9 (full chú thích từng dòng) ---
# Viết hoa ký tự đầu/cuối, giữa là *
chuoi = "luyện tập python hay"          # Gán chuỗi đầu vào
kq = []                                # Tạo list rỗng để chứa kết quả
for tu in chuoi.split():               # Duyệt từng từ
    if len(tu) == 1:                   # Nếu từ chỉ có 1 ký tự
        tu_moi = tu.upper()            # Viết hoa ký tự đó
    elif len(tu) == 2:                 # Nếu từ có 2 ký tự
        dau = tu[0].upper()            # Ký tự đầu viết hoa
        cuoi = tu[1].upper()           # Ký tự cuối viết hoa
        tu_moi = dau + "*" + cuoi      # Ghép: đầu + * + cuối
    else:                              # Nếu từ có từ 3 ký tự trở lên
        dau = tu[0].upper()            # Ký tự đầu viết hoa
        giua = "*" * (len(tu) - 2)     # Số dấu * bằng số ký tự giữa (len-2)
        cuoi = tu[-1].upper()          # Ký tự cuối viết hoa
        tu_moi = dau + giua + cuoi     # Ghép lại: đầu + giữa + cuối
    kq.append(tu_moi)                  # Thêm vào list kết quả
print(kq)                              # ['L***N', 'T*P', 'P****N', 'H*Y']

# --- Bài 10 (full chú thích từng dòng) ---
# Thay ký tự đầu và cuối bằng "*", giữ phần giữa
chuoi = "code python hay quá"           # Chuỗi đầu vào
kq = []                                # Tạo list rỗng chứa kết quả
for tu in chuoi.split():                # Duyệt từng từ
    if len(tu) == 2:                    # Nếu từ chỉ có 2 ký tự
        tu_moi = "**"                   # Thay luôn bằng hai dấu *
    elif len(tu) == 1:                  # Nếu từ chỉ có 1 ký tự
        tu_moi = "*"                    # Thay bằng một dấu *
    else:                               # Nếu từ có từ 3 ký tự trở lên
        giua = tu[1:-1]                 # Lấy phần giữa (từ thứ 2 đến trước cuối)
        tu_moi = "*" + giua + "*"       # Ghép: * + giữa + *
    kq.append(tu_moi)                   # Thêm vào list kết quả
print(kq)                               # ['*od*', '*ytho*', '*a*', '*u*']

# --- Bài 11 (full chú thích từng dòng) ---
# Thay ký tự cuối bằng "*", giữ nguyên phần còn lại
chuoi = "python code vui"               # Chuỗi đầu vào
kq = []                                # Tạo list rỗng chứa kết quả
for tu in chuoi.split():                # Duyệt từng từ
    if len(tu) == 1:                    # Nếu chỉ có 1 ký tự
        tu_moi = "*"                    # Thay bằng *
    else:
        dau = tu[:-1]                   # Lấy toàn bộ trừ ký tự cuối
        tu_moi = dau + "*"              # Ghép phần đầu + *
    kq.append(tu_moi)                   # Thêm vào list kết quả
print(kq)                               # ['pytho*', 'cod*', 'vu*']

# --- Bài 12 (full chú thích từng dòng) ---
# Thay ký tự đầu bằng "*", giữ nguyên phần còn lại
chuoi = "python code vui"               # Chuỗi đầu vào
kq = []                                # Tạo list rỗng chứa kết quả
for tu in chuoi.split():                # Duyệt từng từ
    if len(tu) == 1:                    # Nếu chỉ có 1 ký tự
        tu_moi = "*"                    # Thay bằng *
    else:
        duoi = tu[1:]                   # Lấy phần từ ký tự thứ 2 đến hết
        tu_moi = "*" + duoi             # Ghép * + phần còn lại
    kq.append(tu_moi)                   # Thêm vào list kết quả
print(kq)                               # ['*ython', '*ode', '*ui']

# ------------------------
# TỔNG KẾT TƯ DUY LIST6:
# split() để tách từng từ từ chuỗi lớn.
# join() để ghép từ/các ký tự lại thành chuỗi.
# capitalize(), upper(), lower(): các hàm chuyển đổi kiểu chữ từng từ/ký tự.
# Slicing [start:end]: linh hoạt cắt chuỗi (từ, ký tự đầu, cuối, giữa).
# len() để xác định số ký tự, giúp kiểm soát trường hợp đặc biệt (từ ngắn, dài...).
# Lồng for, if để xử lý sâu từng ký tự (như thay nguyên âm).
# Luôn phân nhánh if với các trường hợp "biên" (1 ký tự, 2 ký tự...).
# f-string hoặc + dùng để ghép các chuỗi lại.
# Xử lý tiếng Việt có dấu cần nhập đúng Unicode (bộ gõ, bảng mã phù hợp).
