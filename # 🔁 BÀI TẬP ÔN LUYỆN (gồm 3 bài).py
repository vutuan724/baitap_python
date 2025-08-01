#  🔁 BÀI TẬP ÔN LUYỆN (gồm 3 bài)
#  🧩 Bài ôn 11: In các ký tự in thường, nối bằng dấu cách
#  Mô tả: Cho một chuỗi, hãy in ra tất cả các chữ cái in thường (a–z), nối nhau bằng dấu cách (' '), không in dư dấu.
#  Ví dụ:

#   Nhập: "AbcD1eF!"

#  In: "b c e"
print("Bài 11 :In các ký tự in thường, nối bằng dấu cách ")
chuoi = input("Hãy nhập chuỗi ở đây : ")
chuoi_moi = ""               # tạo biến chuỗi mới ban đầu ko có gì
for i in chuoi:              # duyệt chuỗi
    if i.isalpha():          # nếu ký tự i là chữ cái
        i = i.lower()        # chuyển chữ cái i về chữ thường
        if chuoi_moi != "":          # nếu ký tự i ko trống
            chuoi_moi += " "         # ký tự sẽ cộng thêm dấu
        chuoi_moi += i       # chuỗi mới sẽ cộng thêm biến i
print(chuoi_moi)
# 🔢 Bài ôn 12: Tính trung bình các chữ số có trong chuỗi
#  Mô tả: Cho một chuỗi gồm cả chữ cái và số. Hãy tính trung bình cộng các chữ số xuất hiện (nếu có), làm tròn kết quả xuống số nguyên.

#  Gợi ý:

#  Tổng các số → dùng tong

#  Đếm số chữ số → dùng dem

#  Trung bình = tong // dem

#  Ví dụ:

#  Nhập: "a1b2c3"

#  In: 2 (vì (1+2+3)//3 = 2)
print("Bài 12 :Tính trung bình các chữ số có trong chuỗi ")
tong = 0                     # tạo biến tổng ban đầu  = 0
dem = 0                      # tạo biến đếm ban đầu = 0
chuoi = input("hãy nhập 1 chuỗi gồm cả chữ và số :")    # tạo chuỗi
for i in chuoi:              # duyệt chuỗi
    if i.isdigit():          # điều kiện - nếu ký tự i là số         
        i= int(i)            # chuyển ký tự số về số nguyên
        tong += i            # tổng = tổng + số 
        dem += 1              # phép tính thú nhất xảy ra nên đếm = 1
if dem > 0:
    ket_qua = tong // dem
    print(ket_qua)
else:
    print("ko có chữ số nào để tính trung bình")

 

# 📌 Bài ôn 13: Kiểm tra chuỗi có chứa ký tự đặc biệt không
#  Mô tả: Cho một chuỗi, hãy kiểm tra xem có tồn tại ký tự đặc biệt hay không (tức là không phải chữ cái, không phải số).

#  Yêu cầu:

#  Nếu có: in "Có ký tự đặc biệt"

#  Nếu không: in "Không có ký tự đặc biệt"
print("Bài 13: Kiểm tra chuỗi có chứa ký tự đặc biệt không ")
ky_tu = False               # tạo giả định ban đầu ký tự đặc biệt là sai
chuoi = input("Hãy nhập chuỗi ở đây : "):                # tạo chuỗi
for i in chuoi:                                          # duyệt chuỗi
    if not i.isalpha() and not i.isdigit():              # điều kiện(nếu ký tự ko phải là số và cũng ko phải là chữ cái)
        ky_tu = True                                     # thì ký tự đặc biệt là đúng,ko đúng với giả định ban đầu 
        break                                            # dừng vòng lập ko kiểm tra nữa                                 
if ky_tu:                                                # ngoài vòng lập ,kiểm tra nếu ký tự đặc biệt là đúng
    print("có ký tự đặc biệt ")                          # in kết quả 
else:
    print("ko có ký tự đặc biệt")                      