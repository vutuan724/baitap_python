# 🔹 [Bài 14 – Nhánh 1: Lọc chuỗi có điều kiện]
# 📌 Đề bài: In các chữ cái in HOA, nối bằng dấu gạch ngang -
# Mô tả:
# Cho một chuỗi bất kỳ, hãy in ra các ký tự chữ cái in HOA (A–Z), nối bằng dấu -, không dư dấu ở đầu/cuối.

# Ví dụ:
# Nhập: "AbC1!X"
# In: A-C-X

# Gợi ý:

# Tạo danh sách ds = [], mỗi khi gặp chữ HOA thì thêm vào danh sách đó.

# Cuối cùng dùng print('-'.join(ds)) để nối danh sách lại.
print("Bài 14: Lọc chuỗi có điều kiện - In chữ in HOA nối bằng dấu '-'")

# Bước 1: Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi ở đây: ")

# Bước 2: Tạo một danh sách rỗng để lưu các chữ cái in HOA tìm được
chuoi_hoa = []   # đây là list (danh sách) rỗng, dùng để lưu chữ in hoa

# Bước 3: Duyệt từng ký tự trong chuỗi
for ky_tu in chuoi:
    if ky_tu.isupper():                                # nếu ký tự là chữ in HOA (A-Z)
        chuoi_hoa.append(ky_tu)                        # thêm ký tự vào danh sách chuoi_hoa

# Bước 4: Dùng join để nối các phần tử trong danh sách bằng dấu "-"
ket_qua = "-".join(chuoi_hoa)                          # nối các phần tử: ['A', 'C', 'X'] -> "A-C-X"

# Bước 5: In kết quả ra màn hình
print(ket_qua)

# 🔹 [Bài 15 – Nhánh 2: Kiểm tra mẫu chuỗi]
# 📌 Đề bài: Kiểm tra chuỗi có ít nhất 1 chữ cái, 1 chữ số và 1 ký tự đặc biệt không?
#  Mô tả:
#  Viết chương trình kiểm tra chuỗi có đủ 3 yếu tố sau:

#  Có ít nhất 1 chữ cái

#  Có ít nhất 1 chữ số

# Có ít nhất 1 ký tự đặc biệt (không phải chữ, không phải số)

# Nếu đủ 3 điều kiện → in: "Chuỗi hợp lệ"
# Nếu thiếu → in: "Chuỗi không hợp lệ"

# Ví dụ:

# "abc123!" → hợp lệ

# "abc123" → không hợp lệ

#  Gợi ý:

# Dùng 3 biến cờ: has_letter, has_digit, has_special

# Duyệt chuỗi, nếu gặp char.isalpha(), char.isdigit() hay ký tự đặc biệt thì đổi cờ.

print("Bài 15 : Kiểm tra mẫu chuỗi")
chuoi = input("Hãy nhập chuỗi ")
has_letter = False
has_digit = False
has_special = False
for i in chuoi:
    if  i.isalpha():
        has_letter = True
    elif i.isdigit():
        has_digit = True
    else:
        has_special = True
    if has_letter and has_digit and has_special :
        break
if has_letter and has_digit and has_special :
   print("chuỗi hợp lệ")
else:
    print("chuỗi ko hợp lệ")




