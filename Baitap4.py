# 🔹 CÁCH 1: Thêm thoải mái, sau đó cắt dấu phẩy cuối ([:-1])
chuoi = input("Nhập chuỗi: ")
ket_qua = ""  # Biến lưu kết quả các chữ in hoa được nối bằng dấu phẩy

for ky_tu in chuoi:
    if ky_tu.isupper():             # Nếu là chữ in hoa
        ket_qua += ky_tu + ","      # Thêm vào kết quả + dấu phẩy

if ket_qua != "":                   # Nếu có ít nhất 1 chữ in hoa
    ket_qua = ket_qua[:-1]          # Xóa dấu phẩy cuối cùng (cắt đi 1 ký tự cuối)

print(ket_qua)                      # In kết quả cuối cùng

# 🔹 CÁCH 2: Làm đúng từ đầu, không cần cắt (if la_dau_tien)
chuoi = input("Nhập chuỗi: ")
ket_qua = ""          # Biến lưu kết quả
la_dau_tien = True    # Biến cờ để kiểm tra có phải ký tự in hoa đầu tiên không

for ky_tu in chuoi:
    if ky_tu.isupper():            # Nếu là chữ in hoa
        if la_dau_tien:            # Nếu là chữ in hoa đầu tiên
            ket_qua += ky_tu       # Thêm trực tiếp, không có dấu phẩy
            la_dau_tien = False    # Đánh dấu đã qua ký tự đầu tiên
        else:
            ket_qua += "," + ky_tu # Từ lần 2 trở đi thì thêm dấu phẩy trước

print(ket_qua)                     # In kết quả

# Cách 3:
chuoi = input("Nhập chuỗi: ")
ket_qua = ""  # Biến lưu các chữ in hoa được nối bằng dấu phẩy

for ky_tu in chuoi:
    if ky_tu.isupper():             # Nếu là chữ in hoa
        if ket_qua != "":           # Nếu đã có ký tự trước đó, thì thêm dấu phẩy
            ket_qua += ","
        ket_qua += ky_tu            # Thêm chữ in hoa vào kết quả

print(ket_qua)                      # In kết quả cuối cùng

# 🧩 🔹 CÔNG THỨC KHUNG: Lọc và nối ký tự có điều kiện, không dư dấu
# chuoi = input("Nhập chuỗi: ")
# ket_qua = ""  # Biến để nối kết quả

# for ky_tu in chuoi:
#    if <điều _kiện>:                # Nếu ký tự thỏa điều kiện cần giữ lại
#        if ket_qua != "":          # Nếu không phải ký tự đầu tiên
#            ket_qua += "<dấu_nối>" # Thêm dấu nối (ví dụ: dấu phẩy)
#        ket_qua += ky_tu           # Thêm ký tự vào kết quả

#print(ket_qua)
