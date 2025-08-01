"""✅ Bài 1 – Làm sạch tên người dùng
Đề bài:
Người dùng nhập vào tên đầy đủ, có thể dư khoảng trắng ở đầu/cuối.
👉 Hãy loại bỏ khoảng trắng dư đó và in ra kết quả.

Ví dụ:
Nhập: " Nguyễn Văn A "
In: Nguyễn Văn A  """

print("Bài 1 : Làm sạch tên người dùng")
chuoi=" Nguyễn Văn A "
chuoi_moi=chuoi.strip()  # Xoá khoảng trắng đầu/cuối
print(chuoi_moi)         # In ra chuỗi đã làm sạch

""" 🔄 Bài 2: Làm sạch tên và thay đổi định dạng
Đề bài:
Người dùng nhập vào tên có khoảng trắng và dấu gạch dưới (_).
Hãy:

Xoá khoảng trắng đầu/cuối.

Thay dấu _ thành dấu cách ' ' để tên hiển thị rõ hơn.

🔸 Ví dụ:
Nhập: "  Le_Thi_Thao  "  
Kết quả in ra: "Le Thi Thao"   """
print("Bài 2: Làm sạch tên và thay đổi định dạng")
chuoi = "  Le_Thi_Thao  "                   # Chuỗi đầu vào có khoảng trắng và dấu gạch dưới
chuoi_moi = chuoi.strip()                   # Bước 1: Xoá khoảng trắng đầu và cuối chuỗi
ket_qua = chuoi_moi.replace("_"," ")        # Bước 2: Thay dấu _ thành khoảng trắng
print(ket_qua)                              # In ra kết quả cuối cùng: "Le Thi Thao"

"""  🧩 Bài 3: Tách họ và tên riêng từ chuỗi tên đầy đủ
🎯 Đề bài:
Người dùng nhập vào tên đầy đủ, có thể có khoảng trắng thừa và dấu _.
Bạn hãy:

Xoá khoảng trắng đầu/cuối tên.

Thay dấu _ thành dấu cách.

In ra:

Dòng 1: Họ

Dòng 2: Tên riêng (tức là phần cuối cùng của chuỗi sau khi xử lý)  """

print("Bài 3: Tách họ và tên riêng từ chuỗi tên đầy đủ")

chuoi = " Le_Thi_Thao "

# Bước 1: Làm sạch chuỗi (xoá khoảng trắng đầu/cuối)
chuoi_mot = chuoi.strip()

# Bước 2: Thay dấu _ bằng khoảng trắng
chuoi_hai = chuoi_mot.replace("_", " ")

# Bước 3: Tách thành danh sách các từ
chuoi_ba = chuoi_hai.split()

# Bước 4: Ghép lại phần họ và tên đệm (nếu có)
ho_va_dem = " ".join(chuoi_ba[:-1])

# Bước 5: Lấy tên riêng (phần cuối)
ten_rieng = chuoi_ba[-1]

# In kết quả
print(ho_va_dem)
print(ten_rieng)


""" ✅ Tổng kết lại:
Mục tiêu	Cách làm
Xoá khoảng trắng	.strip()
Thay dấu gạch dưới	.replace("_", " ")
Tách thành danh sách	.split()
Họ + tên đệm	" ".join(ds[:-1])
Tên riêng	ds[-1]   

💡 Tóm lại:
Cú pháp	Ý nghĩa	Ví dụ kết quả
ds[-1]	Phần tử cuối cùng	'Trung'
ds[:-1]	Tất cả phần tử trừ cái cuối cùng	['Nguyen', 'Van', 'Thanh']
ds[0]	Phần tử đầu tiên	'Nguyen'
ds[1:-1]	Phần tử giữa (tên đệm, nếu có)	['Van', 'Thanh']
"""