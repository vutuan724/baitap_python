# 🔰 Bài 1: .strip()
# Đề bài: Cho người dùng nhập vào một chuỗi bất kỳ. 
# Hãy loại bỏ tất cả khoảng trắng ở đầu và cuối chuỗi đó rồi in kết quả.

print("Bài Tập 1: strip()")
chuoi = " Xin chào Python "
chuoi_moi = chuoi.strip()  # Xoá khoảng trắng ở đầu và cuối chuỗi
print(chuoi_moi)  # Kết quả: 'Xin chào Python'


# ▶️ Bài 2: .replace()
# Đề bài: Thay tất cả dấu phẩy , bằng dấu - và in ra kết quả.

print("Bài Tập 2 với .replace()")
chuoi = "Tôi, đang, học, Python"
chuoi_moi = chuoi.replace(",", "-")  # Thay dấu , bằng dấu -
print(chuoi_moi)  # Kết quả: 'Tôi- đang- học- Python'


# 🪜 Bài 3: .append()
# Đề bài: Duyệt chuỗi "ABC" từng ký tự một, dùng .append() để thêm vào danh sách, sau đó in danh sách ra.

print("Bài Tập 3: append")
chuoi = "ABC"
chuoi_moi = []
for i in chuoi:
    chuoi_moi.append(i)  # Thêm từng ký tự vào danh sách
print(chuoi_moi)  # Kết quả: ['A', 'B', 'C']


# 🔄 Bài 4: .join()
# Đề bài: Dùng .join() để nối danh sách ['A', 'B', 'C'] thành chuỗi "A-B-C"

print("Bài Tập 4: join")
ds = ['A', 'B', 'C']
chuoi_moi = "-".join(ds)  # Nối bằng dấu gạch ngang
print(chuoi_moi)  # Kết quả: 'A-B-C'


# ▶️ Bài 5: Kết hợp .strip() và .replace()
# Đề bài: Nhập chuỗi " Tôi yêu, Python ", xóa khoảng trắng đầu/cuối, thay , thành -

print("Bài Tập 5: strip() + replace()")
chuoi = " Tôi yêu, Python "
chuoi_moi = chuoi.strip()  # Xoá khoảng trắng
ket_qua = chuoi_moi.replace(",", "-")  # Thay dấu phẩy bằng dấu gạch ngang
print(ket_qua)  # Kết quả: 'Tôi yêu- Python'


#   🎓 Tóm tắt nhanh 5 hàm chính:
#   Hàm	Tác dụng chính
#   .strip()	Xoá khoảng trắng ở đầu và cuối chuỗi
#   .replace(old, new)	Thay tất cả chuỗi con old bằng new
#   .append()	Thêm từng phần tử vào danh sách
#   .join()	Nối danh sách thành chuỗi, ngăn cách bằng dấu chỉ định



