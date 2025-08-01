#Đề Bài: Phân Loại và Đếm Ký Tự Theo Từng Nhóm Cụ Thể
#Viết một chương trình Python để:

#Hỏi người dùng nhập vào một chuỗi bất kỳ.
#Khởi tạo các biến đếm cho 4 loại ký tự sau, ban đầu bằng 0:
#so_chu_hoa (số lượng chữ cái in hoa)
#so_chu_thuong (số lượng chữ cái thường)
#so_chu_so (số lượng chữ số)
#so_ky_tu_khac (số lượng ký tự còn lại không phải chữ cái và không phải chữ số)
Duyệt qua từng ký tự trong chuỗi đã nhập.
#Với mỗi ký tự:
#Nếu nó là chữ cái in hoa, tăng so_chu_hoa.
#Nếu nó là chữ cái thường, tăng so_chu_thuong.
#Nếu nó là chữ số, tăng so_chu_so.
#Trong các trường hợp còn lại (không phải chữ cái, không phải chữ số), tăng so_ky_tu_khac.
#Cuối cùng, in ra tổng số lượng của từng loại ký tự đã đếm được.
chuoi = input("Hãy nhập vào 1 chuỗi bất kỳ : ") # tạo chuỗi
chu_in_hoa = 0
chu_thuong = 0
ky_tu_dac_biet = 0
so = 0
for ky_tu in chuoi:
    if ky_tu.isalpha():
        elif ky_tu.isupper():
           chu_in_hoa += 1
    elif ky_tu.islower():
           chu_thuong += 1
    elif ky_tu.isdigit():
           so += 1
    else:
           ky_tu_dac_biet += 1
        
print(chu_in_hoa)
print(chu_thuong)
print(so)
print(ky_tu_dac_biet)
