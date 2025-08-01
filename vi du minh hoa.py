"""📚 Ví dụ minh họa theo bài bạn đang học:
🔹 Bài 1: Tách chuỗi theo dấu phẩy
  """
chuoi = "  Học, Python , rất , vui  "
ds = chuoi.split(",")  # Tách thành danh sách các phần tử
print(ds)
""" ✅ Mục tiêu: học .split(",")

🔹 Bài 2: Dọn khoảng trắng cho từng phần tử
  """
chuoi = "  Học, Python , rất , vui  "
ds = chuoi.split(",")       # Tách thành danh sách
ds_moi = []                 # Danh sách sạch
for tu in ds:
    ds_moi.append(tu.strip())  # Loại bỏ khoảng trắng từng từ
print(ds_moi)
# ✅ Mục tiêu: luyện .strip() kết hợp vòng lặp + .append()

""" 🔹 Bài 3: Ghép lại thành chuỗi có dấu -
 """
chuoi = "  Học, Python , rất , vui  "
ds = chuoi.split(",")
ds_moi = []
for tu in ds:
    ds_moi.append(tu.strip())
ket_qua = "-".join(ds_moi)   # Ghép lại thành chuỗi sạch
print(ket_qua)