#📌 Công Thức Khung: Duyệt chuỗi – Lọc ký tự – In kết quả
#   python
#   Sao chép
#   Chỉnh sửa
#   chuoi = "..."           # 1. Tạo chuỗi cần xử lý
#   ket_qua = ""            # 2. Tạo biến rỗng để lưu kết quả

for ky_tu in chuoi:     # 3. Duyệt từng ký tự trong chuỗi
    if điều_kiện:     # 4. Kiểm tra điều kiện lọc
        if ket_qua != "":
            ket_qua += ngăn_cách   # 5. Thêm dấu phân cách nếu cần
        ket_qua += ky_tu             # 6. Thêm ký tự thỏa điều kiện vào kết quả

# print(ket_qua)          # 7. In ra kết quả cuối cùng
# 🧠 Một số điều kiện thường dùng:
# Mục tiêu lọc	Điều kiện viết trong if
# Chỉ chữ cái	ky_tu.isalpha()
# Chỉ chữ cái thường	ky_tu.islower()
# Chỉ chữ cái in hoa	ky_tu.isupper()
# Chỉ số	ky_tu.isdigit()
# Bỏ khoảng trắng	ky_tu != " "
# Bỏ dấu chấm than (!)	ky_tu != "!"
# Lấy mọi ký tự không phải chữ	not ky_tu.isalpha()

# ✅ Mẹo ghi nhớ:
# isalpha() → chữ cái (a-z, A-Z)

# isdigit() → chữ số (0–9)

# islower() → chữ thường

# isupper() → chữ IN HOA

# != → khác (loại bỏ)

# not → phủ định điều kiện