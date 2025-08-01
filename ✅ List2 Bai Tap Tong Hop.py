# ===============================
# 📘 TỔNG HỢP BÀI TẬP LIST2 (B1 → B25)
# ➤ Viết đầy đủ, có chú thích từng dòng, không rút gọn
# ➤ Bài nào có thể viết rút gọn thì có chú thích mở rộng để học so sánh
# ===============================

# -------------------------------
# B1 – So sánh chuỗi
chuoi_1 = "Hello World"  # Khởi tạo chuỗi 1
chuoi_2 = "Hello  World"  # Khởi tạo chuỗi 2 với 2 khoảng trắng
ket_qua = chuoi_1 == chuoi_2  # So sánh chuỗi bằng toán tử ==
print(ket_qua)  # In kết quả so sánh (sai do khoảng trắng khác)

# -------------------------------
# B2 – Dùng strip() để xóa khoảng trắng đầu/cuối
s = "  Hello World  "  # Chuỗi có khoảng trắng đầu/cuối
print("Trước khi dùng strip:", s)  # In chuỗi ban đầu
s = s.strip()  # Xóa khoảng trắng đầu và cuối chuỗi
print("Sau khi dùng strip:", s)  # In kết quả đã xử lý

# -------------------------------
# B3 – Đếm số từ trong chuỗi
s = "one   two  three"  # Chuỗi chứa nhiều khoảng trắng giữa các từ
s = s.strip()  # Xóa khoảng trắng đầu/cuối nếu có
s = s.split()  # Tách thành danh sách từ, tự bỏ khoảng trắng thừa
so_tu = len(s)  # Đếm số từ = độ dài danh sách
print("Số từ là:", so_tu)  # In số từ

# -------------------------------
# B4 – Thay dấu chấm thành dấu phẩy
s = "Python. is. fun."  # Chuỗi ban đầu có dấu chấm
s = s.replace(".", ",")  # Thay toàn bộ dấu chấm bằng dấu phẩy
print(s)  # In chuỗi sau khi thay thế

# -------------------------------
# B5 – Ẩn số điện thoại, chỉ hiển thị 4 số cuối
sdt = "0912345678"  # Chuỗi số điện thoại
so_cuoi = sdt[-4:]  # Lấy 4 số cuối bằng slicing (dạng s[-4:])
phan_an = "*" * (len(sdt) - 4)  # Tạo chuỗi dấu * bằng phép nhân chuỗi
sdt_an = phan_an + so_cuoi  # Ghép phần ẩn + phần hiển thị
print(sdt_an)  # In kết quả đã ẩn số

# Ghi chú rút gọn:
# ✅ Có thể viết 1 dòng: print("*"*(len(sdt)-4) + sdt[-4:])

# -------------------------------
# B6 – Ẩn tên (chỉ hiện chữ cái đầu)
ten = "Nguyen"  # Tên cần xử lý
chu_dau = ten[0].lower()  # Lấy chữ đầu, chuyển thành chữ thường
con_lai = len(ten) - 1  # Số ký tự còn lại để thay bằng *
ghep = chu_dau + "*" * con_lai  # Ghép chữ đầu + chuỗi *
print(ghep)  # In kết quả

# -------------------------------
# B7 – Tách họ tên và tạo username
ho_ten = "Nguyen Van An"  # Chuỗi họ tên đầy đủ
ho_ten = ho_ten.split()  # Tách thành list: ['Nguyen', 'Van', 'An']
ten = ho_ten[-1].lower()  # Lấy tên (cuối danh sách), viết thường
ho = ho_ten[0].lower()  # Lấy họ (đầu danh sách), viết thường
username = ten + "." + ho  # Ghép thành email: ten.ho
print(username)  # In username

# -------------------------------
# B8 – Ghép username có số random
import random  # Nhập thư viện tạo số ngẫu nhiên
ho_ten = "Nguyen Van An"
ho_ten = ho_ten.split()  # Tách thành list
ho = ho_ten[0].lower()  # Họ viết thường
ten = ho_ten[-1].lower()  # Tên viết thường
so = random.randint(0, 999)  # Tạo số ngẫu nhiên từ 0 đến 999
username = ten + "." + ho + str(so)  # Ghép username + số
print(username)

# -------------------------------
# B9 – Tách họ, tên đệm, tên
ho_ten = "Nguyen Van An"
ho_ten = ho_ten.split()  # Tách chuỗi thành danh sách
ho = ho_ten[0].lower()  # Họ là phần tử đầu tiên
ten_dem = ho_ten[1].lower()  # Tên đệm là phần tử giữa
ten = ho_ten[-1].lower()  # Tên là phần tử cuối
print(ho)
print(ten_dem)
print(ten)

# -------------------------------
# B10 – Tạo username dạng h.v.an
ho_ten = "Nguyen Van An"
ho_ten = ho_ten.split()  # Tách chuỗi
ho = ho_ten[0].lower()[0]  # Lấy chữ cái đầu họ, viết thường
ten_dem = ho_ten[1].lower()[0]  # Lấy chữ cái đầu tên đệm, viết thường
ten = ho_ten[-1]  # Lấy tên cuối cùng
username = ho + "." + ten_dem + "." + ten  # Ghép theo định dạng h.v.an
print(username)

# ✅ Có thể viết rút gọn thành 1 dòng:
# print(ho_ten[0][0].lower() + "." + ho_ten[1][0].lower() + "." + ho_ten[-1])

# -------------------------------
# 🔜 Phần tiếp theo: B11 → B25 đang được bổ sung ngay bên dưới theo format tương tự...


# -------------------------------
# B11 – Rút gọn họ tên thành 2 từ cuối
ho_ten = "Tran Thi Hong Gam"  # Họ tên đầy đủ
ho_ten = ho_ten.split()  # Tách thành danh sách từ
rut_gon = ho_ten[-2:]  # Lấy 2 phần tử cuối (tên đệm + tên)
ket_qua = " ".join(rut_gon)  # Ghép lại thành chuỗi
print(ket_qua)  # In kết quả: Hong Gam

# -------------------------------
# B12 – Viết hoa từng từ bằng for + capitalize()
ho_ten = "nguyen van an"  # Chuỗi viết thường
ho_ten = ho_ten.split()  # Tách chuỗi thành danh sách từ
ket_qua = []  # Tạo danh sách rỗng để lưu kết quả
for tu in ho_ten:  # Duyệt từng từ trong danh sách
    chu = tu.capitalize()  # Viết hoa chữ đầu mỗi từ
    ket_qua.append(chu)  # Thêm vào danh sách kết quả
ket_qua = " ".join(ket_qua)  # Ghép lại thành chuỗi
print(ket_qua)  # In kết quả: Nguyen Van An

# -------------------------------
# B13 – Lấy chữ cái đầu mỗi từ + 3 số cuối điện thoại
ho_ten = "Nguyen Van An"
sdt = "0912345678"
ho_ten = ho_ten.split()  # Tách chuỗi thành danh sách
chu_dau = ""  # Khởi tạo chuỗi để chứa chữ cái đầu
for tu in ho_ten:
    chu_dau += tu[0].lower()  # Lấy chữ cái đầu và viết thường
so_cuoi = sdt[-3:]  # Lấy 3 số cuối điện thoại
ket_qua = chu_dau + so_cuoi  # Ghép chữ đầu + 3 số cuối
print(ket_qua)  # In kết quả: nva678 (ví dụ)

# -------------------------------
# B14 – Ghép tên + năm sinh thành username
ho_ten = "Nguyen Van An"
nam_sinh = 1995
ho_ten = ho_ten.split()  # Tách họ tên thành danh sách
ten = ho_ten[-1].lower()  # Lấy tên và viết thường
ghep = ten + str(nam_sinh)  # Ghép tên + năm sinh thành chuỗi
print(ghep)  # Kết quả: an1995

# -------------------------------
# B15 – Tách tên và họ riêng biệt, rồi in dạng tên,họ
chuoi = "Nguyen Van An"
chuoi = chuoi.split()  # Tách chuỗi thành danh sách từ
ten = chuoi[-1]  # Lấy phần tử cuối là tên
ho = chuoi[0:-1]  # Lấy tất cả phần tử trừ tên cuối
ho = " ".join(ho)  # Ghép lại thành họ đầy đủ
ghep = ten + "," + ho  # Ghép dạng: tên,họ
print(ghep)  # Kết quả: An,Nguyen Van

# -------------------------------
# B16 – Viết hoa từng từ dùng vòng lặp (không dùng .title())
ho_ten = "nguyen van an"
ho_ten = ho_ten.split()  # Tách chuỗi thành danh sách từ
ds = []  # Tạo danh sách rỗng
for duyet in ho_ten:  # Duyệt từng từ
    chu = duyet.capitalize()  # Viết hoa chữ cái đầu mỗi từ
    ds.append(chu)  # Thêm từ đã viết hoa vào danh sách
ket_qua = " ".join(ds)  # Ghép các từ lại thành chuỗi
print(ket_qua)  # Kết quả: Nguyen Van An

# -------------------------------
# B17 – Tạo username: tên + chữ cái đầu họ (cách ngắn)
ho_ten = "Nguyen Van An"
ho_ten = ho_ten.split()  # Tách danh sách từ
ten = ho_ten[-1].lower()  # Tên viết thường
ho = ho_ten[0][0].lower()  # Lấy chữ cái đầu của họ
ghep = ten + "." + ho  # Ghép dạng: tên.h
print(ghep)  # Kết quả: an.n

# -------------------------------
# B18 – Lấy 2 từ cuối nếu danh sách dài ≥ 2 từ
ho_ten = "Pham Thi Bich Hong Gam"
ho_ten = ho_ten.split()  # Tách chuỗi thành danh sách
if len(ho_ten) >= 2:  # Chỉ thực hiện nếu có ít nhất 2 từ
    rut_gon = ho_ten[-2:]  # Lấy 2 từ cuối
ket_qua = " ".join(rut_gon)  # Ghép thành chuỗi
print(ket_qua)  # Kết quả: Hong Gam

# -------------------------------
# B19 – Kiểm tra tên có hợp lệ (không chứa số hay ký tự đặc biệt)
ho_ten = input("Nhập tên đầy đủ ở đây: ")  # Nhập tên từ người dùng
hop_le = True  # Giả sử ban đầu tên hợp lệ

for ky_tu in ho_ten:
    if not (ky_tu.isalpha() or ky_tu.isspace()):  # Nếu ký tự không phải chữ hoặc khoảng trắng
        hop_le = False  # Đánh dấu là không hợp lệ
        break  # Dừng kiểm tra nếu thấy sai

if hop_le:
    print("Tên hợp lệ")
else:
    print("Tên không hợp lệ")

# -------------------------------
# B20 – Tách email thành username và domain
email = "an.nguyen@gmail.com"
email = email.split("@")  # Tách email tại ký tự @ thành 2 phần
usname = email[0]  # Lấy phần trước @ là username
domain = email[-1]  # Lấy phần sau @ là domain
print(usname)  # In phần username
print(domain)  # In phần domain

# -------------------------------
# B21 – Che giấu username trong email bằng dấu *
email = "an.nguyen@gmail.com"
email = email.split("@")  # Tách thành [username, domain]
domain = email[-1]  # Phần sau @
usname = email[0]  # Phần trước @
chu_dau = usname[0]  # Lấy ký tự đầu tiên
con_lai = len(usname) - 1  # Đếm số ký tự còn lại để thay bằng *
ghep = chu_dau + "*" * con_lai + "@" + domain  # Ghép lại email đã ẩn
print(ghep)  # Ví dụ: a********@gmail.com

# -------------------------------
# B22 – Ghép tên viết thường + số ngẫu nhiên từ 000–999
import random
ho_ten = "Nguyen Van An"
ho_ten = ho_ten.split()  # Tách danh sách từ
ho = ho_ten[0].lower()  # Họ viết thường
ten = ho_ten[-1].lower()  # Tên viết thường
so = random.randint(0, 999)  # Sinh số ngẫu nhiên từ 0 đến 999
username = ten + "." + ho + str(so)  # Ghép thành username
print(username)  # Ví dụ: an.nguyen123

# -------------------------------
# B23 – Ghép chữ cái đầu họ, tên đệm + tên (không viết tắt hàm)
ho_ten = "Nguyen Van An"
ho_ten = ho_ten.split()  # Tách danh sách từ
ho = ho_ten[0].lower()[0]  # Lấy chữ cái đầu họ, viết thường
ten_dem = ho_ten[1].lower()[0]  # Lấy chữ cái đầu tên đệm
ten = ho_ten[-1]  # Lấy tên giữ nguyên chữ
username = ho + "." + ten_dem + "." + ten  # Ghép dạng: h.t.ten
print(username)  # Ví dụ: n.v.An

# -------------------------------
# B24 – Lấy chữ cái đầu mỗi từ trong họ tên + 3 số cuối điện thoại
ho_ten = "Nguyen Van An"
sdt = "0912345678"
ho_ten = ho_ten.split()  # Tách danh sách từ
chu_dau = ""
for tu in ho_ten:
    chu_dau += tu[0].lower()  # Lấy chữ đầu mỗi từ viết thường
so_cuoi = str(sdt[-3:])  # Lấy 3 số cuối từ số điện thoại
ket_qua = chu_dau + so_cuoi  # Ghép kết quả
print(ket_qua)  # Ví dụ: nva678

# -------------------------------
# B25 – Viết hoa từng từ trong họ tên (dùng for + capitalize đầy đủ)
ho_ten = "nguyen van an"  # Họ tên viết thường hoàn toàn
ho_ten = ho_ten.split()  # Tách chuỗi thành danh sách từng từ: ["nguyen", "van", "an"]

# Khởi tạo danh sách rỗng để chứa các từ đã viết hoa
ds = []

                                              # Duyệt từng phần tử trong danh sách ho_ten
for duyet in ho_ten:
                                              # ds.append(duyet.capitalize())  # ✅ Cách viết thường dùng – gọn gàng và đúng nghĩa
    chu = duyet.capitalize()                  # Viết hoa chữ cái đầu mỗi từ
    ds.append(chu)                            # Thêm từ đã viết hoa vào danh sách kết quả

                                              # Ghép danh sách lại thành chuỗi hoàn chỉnh cách nhau bởi khoảng trắng
ket_qua = " ".join(ds)

# In kết quả cuối cùng
print(ket_qua)  # Kết quả: Nguyen Van An

# 📌 Có thể viết gọn dòng for và append như sau:
# ds = [duyet.capitalize() for duyet in ho_ten]  # ← cách viết rút gọn dùng list comprehension
