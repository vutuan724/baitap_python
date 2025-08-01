# ✅ List6 – Tổng kết xử lý chuỗi nâng cao (12 bài)
# Bạn hãy rà soát lại chú thích, sau này quên sẽ dễ ôn lại từng dòng!

# ---

# 🔹 Bài 1
# 📅 Nhập: "python ai model"
# 📆 Kết quả: ["Python", "Ai", "Model"]
# 🎯 Yêu cầu: Viết hoa chữ cái đầu mỗi từ
chuoi = "python ai model"           # Gán chuỗi đầu vào
ket_qua = []                        # Tạo list rỗng để chứa kết quả
for tu in chuoi.split():            # Duyệt từng từ trong chuỗi sau khi tách bằng split()
    ket_qua.append(tu.capitalize()) # Viết hoa chữ cái đầu mỗi từ, thêm vào list
print(ket_qua)                      # In ra list kết quả cuối cùng

# ---

# 🔹 Bài 2
# 📅 Nhập: "Nguyen Van Quang"
# 📆 Kết quả: "NVQ"
# 🎯 Yêu cầu: Lấy chữ cái đầu của mỗi từ và ghép lại, viết hoa
chuoi = "Nguyen Van Quang"          # Gán chuỗi đầu vào
chuoi_moi = []                      # Tạo list rỗng để chứa từng chữ cái đầu
for tu in chuoi.split():            # Duyệt từng từ
    chuoi_moi.append(tu[0].upper()) # Lấy ký tự đầu tiên, chuyển thành hoa, thêm vào list
print("".join(chuoi_moi))           # Ghép các phần tử list thành 1 chuỗi

# ---

# 🔹 Bài 3
# 📅 Nhập: "Pham Thi Minh Khoa"
# 📆 Kết quả: "Pham T. M. Khoa"
# 🎯 Yêu cầu: Viết tắt tên đệm, giữ họ và tên đầy đủ
chuoi = "Pham Thi Minh Khoa"             # Gán chuỗi đầu vào
ho_ten = chuoi.split()                    # Tách thành list các từ
ho = ho_ten[0]                            # Lấy họ (phần tử đầu tiên)
dem = ho_ten[1:-1]                        # Lấy tên đệm (tất cả trừ đầu và cuối)
ten = ho_ten[-1]                          # Lấy tên (phần tử cuối)
dem_viettat = " ".join([d[0].upper() + "." for d in dem]) # Viết tắt từng tên đệm
kq = ho + " " + dem_viettat + " " + ten # Ghép lại họ, đệm viết tắt và tên
print(kq)                                 # In ra kết quả cuối cùng

# ---

# 🔹 Bài 4
# 📅 Nhập: "Python Ai Model"
# 📆 Kết quả: "P.A.M"
# 🎯 Yêu cầu: Viết tắt toàn bộ bằng chữ cái đầu, cách nhau dấu chấm
chuoi = "Python Ai Model"                # Gán chuỗi đầu vào
kq = []                                   # List rỗng chứa chữ cái đầu
for tu in chuoi.split():                  # Duyệt từng từ
    kq.append(tu[0].upper())              # Lấy ký tự đầu, chuyển hoa, thêm vào list
print(".".join(kq))                       # Ghép list thành chuỗi, cách nhau dấu chấm

# ---

# 🔹 Bài 5
# 📅 Nhập: "python ai model"
# 📆 Kết quả: ["Python - N", "Ai - I", "Model - L"]
# 🎯 Yêu cầu: In từ đã capitalize + chữ cái cuối (viết hoa), ghép bằng " - "
chuoi = "python ai model"                # Gán chuỗi đầu vào
ket_qua = []                              # List rỗng để chứa từng từ sau xử lý
for tu in chuoi.split():                  # Duyệt từng từ
    tu_moi = tu.capitalize() + " - " + tu[-1].upper()  # Viết hoa đầu từ, lấy ký tự cuối viết hoa, ghép lại
    ket_qua.append(tu_moi)                # Thêm kết quả vào list
print(ket_qua)                            # In ra list kết quả

# ---

# 🔹 Bài 6
# 📅 Nhập: "python ai model"
# 📆 Kết quả: ["pyth*n", "*", "m*d*l"]
# 🎯 Yêu cầu: Thay tất cả nguyên âm bằng dấu "*"
chuoi = "python ai model"                # Gán chuỗi đầu vào
ket_qua = []                              # List rỗng để chứa từ đã thay nguyên âm
for tu in chuoi.split():                  # Duyệt từng từ
    tu_moi = ""                           # Biến tạm chứa từ sau xử lý
    for c in tu:                          # Duyệt từng ký tự của từ
        if c in "aeiouAEIOU":             # Nếu ký tự là nguyên âm (hoa/thường)
            tu_moi += "*"                 # Thay bằng dấu *
        else:
            tu_moi += c                   # Nếu không, giữ nguyên ký tự
    ket_qua.append(tu_moi)                # Thêm từ đã xử lý vào list
print(ket_qua)                            # In ra list kết quả cuối

# ---

# 🔹 Bài 7
# 📅 Nhập: "Python Model AI"
# 📆 Kết quả: ["P****n", "M***l", "A*"]
# 🎯 Yêu cầu: Giữ chữ đầu và cuối, thay phần giữa bằng dấu "*"
chuoi = "Python Model AI"                 # Gán chuỗi đầu vào
ket_qua = []                              # List rỗng để chứa từ đã thay phần giữa
for tu in chuoi.split():                  # Duyệt từng từ
    if len(tu) == 1:                      # Nếu từ chỉ có 1 ký tự
        tu_moi = tu.upper()               # Chuyển thành chữ hoa
    elif len(tu) == 2:                    # Nếu từ 2 ký tự
        tu_moi = tu[0] + "*"              # Giữ ký tự đầu, thay ký tự cuối
    else:
        tu_moi = tu[0].upper() + "*" * len(tu[1:-1]) + tu[-1].upper()  # Giữ đầu/cuối hoa, thay giữa bằng *
    ket_qua.append(tu_moi)                # Thêm vào list kết quả
print(ket_qua)                            # In ra list kết quả

# ---

# 🔹 Bài 8
# 📅 Nhập: "python ai model"
# 📆 Kết quả: ["PYTHOn", "AI", "MODEl"]
# 🎯 Yêu cầu: Viết hoa toàn bộ trừ chữ cuối (chữ cuối viết thường)
chuoi = "python ai model"                # Gán chuỗi đầu vào
ket_qua = []                              # List rỗng chứa từng từ sau xử lý
for tu in chuoi.split():                  # Duyệt từng từ
    if len(tu) == 1:                      # Nếu từ chỉ 1 ký tự
        ds = tu.upper()                   # Chuyển thành hoa
    elif len(tu) == 2:                    # Nếu từ có 2 ký tự
        ds = tu[0].upper() + tu[1].upper()# Cả hai ký tự chuyển hoa
    else:
        ds = tu[0].upper() + tu[1:-1].upper() + tu[-1].lower() # Đầu & giữa hoa, cuối thường
    ket_qua.append(ds)                    # Thêm từ đã xử lý vào list
print(ket_qua)                            # In ra list kết quả

# ---

# 🔹 Bài 9
# 📅 Nhập: "Python Ai Model"
# 📆 Kết quả: ["PythoN", "A*", "ModeL"]
# 🎯 Yêu cầu: Viết hoa chữ đầu và cuối, phần giữa thay "*"
chuoi = "Python Ai Model"                 # Gán chuỗi đầu vào
ket_qua = []                              # List rỗng chứa từ đã xử lý
for tu in chuoi.split():                  # Duyệt từng từ
    if len(tu) <= 2:                      # Nếu từ 1 hoặc 2 ký tự
        tu_moi = tu[0].upper() + "*"      # Đầu hoa, còn lại là *
    else:
        tu_moi = tu[0].upper() + "*" * len(tu[1:-1]) + tu[-1].upper()  # Đầu/cuối hoa, giữa là *
    ket_qua.append(tu_moi)                # Thêm vào list kết quả
print(ket_qua)                            # In ra list kết quả

# ---

# 🔹 Bài 10
# 📅 Nhập: "python ai model"
# 📆 Kết quả: ["*ytho*", "**", "*ode*"]
# 🎯 Yêu cầu: Thay chữ đầu và cuối bằng "*"
chuoi = "python ai model"                # Gán chuỗi đầu vào
ket_qua = []                              # List rỗng chứa từ sau xử lý
for tu in chuoi.split():                  # Duyệt từng từ
    if len(tu) == 2:                      # Nếu từ 2 ký tự
        tu_moi = "**"                     # Đổi cả 2 ký tự thành **
    else:
        tu_moi = "*" + tu[1:-1] + "*"      # Đầu/cuối thành *, giữ giữa nguyên
    ket_qua.append(tu_moi)                # Thêm vào list kết quả
print(ket_qua)                            # In ra list kết quả

# ---

# 🔹 Bài 11
# 📅 Nhập: "python ai model"
# 📆 Kết quả: ["Pytho*", "Ai*", "Mode*"]
# 🎯 Yêu cầu: Đổi chữ cuối thành "*", giữ nguyên phần còn lại
chuoi = "python ai model"                # Gán chuỗi đầu vào
ket_qua = []                              # List rỗng để chứa kết quả
for tu in chuoi.split():                  # Duyệt từng từ
    tu_moi = tu[:-1] + "*"                # Lấy tất cả trừ ký tự cuối, thay cuối bằng *
    ket_qua.append(tu_moi)                # Thêm vào list kết quả
print(ket_qua)                            # In ra list kết quả

# ---

# 🔹 Bài 12
# 📅 Nhập: "python ai model"
# 📆 Kết quả: ["*ython", "*i", "*odel"]
# 🎯 Yêu cầu: Đổi chữ đầu thành "*", giữ nguyên phần còn lại
chuoi = "python ai model"                # Gán chuỗi đầu vào
ket_qua = []                              # List rỗng để chứa kết quả
for tu in chuoi.split():                  # Duyệt từng từ
    tu_moi = "*" + tu[1:]                 # Đổi ký tự đầu thành *, giữ phần còn lại
    ket_qua.append(tu_moi)                # Thêm vào list kết quả
print(ket_qua)                            # In ra list kết quả

# ---

# 🎯 Tổng hợp tư duy – Ghi nhớ chung List6
# - split(), join(): tách/ghép từ
# - capitalize(), upper(), lower(): thay đổi kiểu chữ
# - Slicing [start:end]: linh hoạt cắt chuỗi theo yêu cầu
# - Duyệt từng ký tự, từng từ: giúp xử lý linh hoạt nhiều trường hợp đặc biệt
# - Điều kiện if/elif: cần để xử lý đúng các trường hợp từ 1, 2 hoặc nhiều ký tự
# - Nhớ kiểm tra kỹ đề bài, tránh nhầm giữa các dạng: đổi đầu/cuối, giữ/viết hoa, thay bằng *, ...
