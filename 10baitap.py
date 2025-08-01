# Bài 1: Đếm ký tự in hoa trong chuỗi
# Mô tả: Cho một chuỗi đầu vào, hãy đếm số ký tự in hoa (A-Z) trong chuỗi đó và in kết quả. Ví dụ, chuỗi "Hello World!" có 2 ký tự in hoa.
# Gợi ý:
# Dùng vòng lặp for để duyệt từng ký tự trong chuỗi.
# Sử dụng char.isupper() để kiểm tra ký tự có phải là chữ hoa hay không.
# Tạo biến đếm (ví dụ count = 0), mỗi lần gặp ký tự in hoa thì tăng biến đếm lên 1.
# Cuối cùng dùng print() để in kết quả. Không sử dụng hàm sum().
print("Bài tập 1 : Đếm ký tự in hoa trong chuỗi.")
chuoi = input("Hãy nhập chuỗi : ")
in_hoa = 0
for ky_tu in chuoi:
    if ky_tu.isupper():
        in_hoa += 1
print(in_hoa)
# Bài 2:Đếm ký tự in thường trong chuỗi
print("Bài 2 :Đếm ký tự in thường trong chuỗi")
chuoi = input("Hãy nhập chuỗi : ")
chu_thuong = 0
for ky_tu in chuoi:
    if ky_tu.islower():
        chu_thuong += 1
print(chu_thuong)
#Bài 3: Đếm chữ số trong chuỗi
print("Bài 3:Đếm chữ số trong chuỗi ")
chuoi = input("Hãy nhập chuỗi : ")
chu_so = 0
for ky_tu in chuoi:
    if ky_tu.isdigit():
        chu_so += 1
print(chu_so)
# Bài 4: Đếm chữ cái và chữ số trong chuỗi
print("Bài 4: Đếm chữ cái và chữ số trong chuỗi")
chuoi = input("Hãy nhập chuỗi : ")
chu_so = 0
chu_cai = 0
for ky_tu in chuoi:
    if ky_tu.isdigit():
        chu_so += 1
    if ky_tu.isalpha():
        chu_cai += 1
print(chu_so)
print(chu_cai)
# Bài 5: Tạo chuỗi chỉ gồm ký tự số từ chuỗi ban đầu
# Mô tả: Cho một chuỗi, hãy tạo một chuỗi mới chỉ gồm các ký tự số có trong chuỗi đó, sau đó in chuỗi mới. Ví dụ, từ "a1b2c3" ta được chuỗi "123".
print("Bài 5: Tạo chuỗi chỉ gồm ký tự số từ chuỗi ban đầu")
chuoi = input(" Hãy nhập chuỗi cả chữ và số : ")
chuoi_moi = ""
for i in chuoi:
    if i.isdigit():
        chuoi_moi += i
print(chuoi_moi,end="")
# Bai 6: Tạo chuỗi chỉ gồm ký tự chữ cái từ chuỗi ban đầu
# Mô tả: Cho một chuỗi, hãy tạo một chuỗi mới chỉ gồm các ký tự chữ cái (a-z, A-Z) có trong chuỗi đó và in ra chuỗi mới. Ví dụ, từ "H3ll0, W0rld!" ta được "HllWrld".
# Gợi ý:
# Tương tự bài 5, khởi tạo result = "".
# Dùng vòng for duyệt ký tự.
# Nếu char.isalpha() thì result += char.
# In chuỗi kết quả cuối cùng.
print("Bài 6: Tạo chuỗi chỉ gồm ký tự chữ cái từ chuỗi ban đầu")
chuoi = input(" Hãy nhập chuỗi cả chữ và số : ")
chuoi_moi = ""
for i in chuoi:
    if i.isalpha():
        chuoi_moi += i
print(chuoi_moi,end="")
#Bài 7: Kiểm tra chuỗi chỉ gồm chữ số hay không
# Mô tả: Cho một chuỗi, hãy kiểm tra xem chuỗi đó có chỉ chứa ký tự số (0-9) hay không. Nếu chỉ chứa số thì in "Chu\u1ed9i toan so", ngược lại in "Chu\u1ed9i khong toan so". Ví dụ, với "12345" in "Chuỗi toàn số", còn với "12a34" in "Chuỗi không toàn số".
# Gợi ý:
# Giả sử chuỗi s ban đầu. Tạo biến cờ all_digits = True.
# Dùng for duyệt từng ký tự char trong s.
# Nếu not char.isdigit(), gán all_digits = False và có thể break khỏi vòng lặp.
# Sau vòng lặp, nếu all_digits vẫn là True, in kết quả "Chuỗi toàn số", ngược lại in "Chuỗi không toàn số".

print("Bài 7:Kiểm tra chuỗi chỉ gồm chữ số hay không")
chuoi = input("Nhập chuỗi ở đây : ")           # Tạo chuỗi
toan_so = True                                 # tạo biến giả định toan_so = là đúng
for i in chuoi:                                # duyệt chuỗi
    if not i.isdigit():                        # nếu ký tự i ko phải là số
        toan_so = False                        # toan_so giả định ban đầu là sai
        break                                  # dừng kiểm tra,kết thúc vòng lập
if toan_so:                                    # ngoài vòng lập nếu toan_so là số
    print("Chuỗi toàn số")                     # in kết quả
else:                                          # ngược lại
    print("Chuỗi ko toàn số")                  # in kết quả
     

# Bài 8: Kiểm tra chuỗi có chứa ít nhất một chữ số hay không
# Mô tả: Cho một chuỗi, hãy kiểm tra xem có tồn tại ít nhất một ký tự số trong chuỗi hay không. Nếu có,
# in "Co chu so" , ngược lại in "Khong co chu so" . Ví dụ, chuỗi "Hello2World" có chữ số nên in
# "Co chu so" .
# Gợi ý:
# - Dùng biến cờ has_digit = False .
# - Dùng vòng for duyệt ký tự. Nếu char.isdigit() == True , đặt has_digit = True và có thể
# break .
# - Sau vòng lặp, nếu has_digit là True , in "Co chu so" , còn không in "Khong co chu so" . 
chuoi = input("Hãy nhập chuỗi ở đây :")   # tạo chuỗi
digit = False                             # đặt biến giả định digit = số là sai
for i in chuoi:                           # duyệt chuỗi
  if i.isdigit():                         # nếu ký tự i là số
    digit = True                          # digit = số là đúng
    break                                 # dừng vòng lập ko kiểm tra nữa
if digit :                                # ngoài vòng lập nếu digit có số 
  print("có chữ số")                      # in ra kết quả có số
else:                                     # ngược lại ko có số 
  print("ko có chữ số")                   # in ra kết quả ko có số

#  Bài 9: Tính tổng các chữ số trong chuỗi
# Mô tả: Cho một chuỗi gồm cả chữ cái và chữ số, hãy tính tổng tất cả các chữ số xuất hiện trong chuỗi và
# in kết quả. Ví dụ, "a1b2c3" có tổng chữ số là 1+2+3 = 6 .
# Gợi ý:
# - Tạo biến tổng total = 0 .
# - Dùng vòng for duyệt các ký tự.
# - Nếu char.isdigit() , chuyển ký tự thành số nguyên (ví dụ int(char) ) và cộng vào total .
# - Kết thúc vòng lặp, dùng print(total) để in kết quả. Không dùng hàm sum() . 

print("Bài 9 : Tính tổng các chữ số trong chuỗi")
chuoi = input("Hãy nhập chuỗi ở đây : ")  # Tạo chuỗi
tong = 0                                  # Tạo biến tổng ban đầu = 0
for i in chuoi:                           # duyệt chuỗi
    if i.isdigit():                       # nếu ký tự i là số
        i = int(i)                        # chuyển số về số nguyên
        tong += i                         # tăng biến đếm = vào số tiếp theo
print(tong)                               # thoát vòng lập in ra kết quả "tổng"

# Bài 10: Đếm ký tự đặc biệt trong chuỗi
# Mô tả: Cho một chuỗi, hãy đếm số ký tự không phải là chữ cái (a-z, A-Z) và không phải là chữ số (0-9),
# tức là các ký tự đặc biệt hoặc dấu cách, và in kết quả. Ví dụ, chuỗi "Hello, World!" có 3 ký tự đặc
# biệt (dấu phẩy, khoảng trắng và dấu chấm than).
# Gợi ý:
# - Tạo biến đếm count_special = 0 .
# - Dùng vòng for duyệt ký tự char trong chuỗi.
# - Nếu not char.isalnum() (không phải chữ cái hoặc số), tăng count_special thêm 1.
# - Cuối cùng, in count_special với print() .
print("Bài 10 : Đếm ký tự đặc biết trong chuỗi ")
ky_tu_dac_biet = 0
for i in chuoi:
    if not i.isalpha() and not i.isdigit():
        ky_tu_dac_biet += 1
print(ky_tu_dac_biet)