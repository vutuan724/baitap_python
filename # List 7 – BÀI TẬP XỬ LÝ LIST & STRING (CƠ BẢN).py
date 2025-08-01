# ========================
# List 7 – BÀI TẬP XỬ LÝ LIST & STRING (CƠ BẢN)
# ========================

# --- Bài 1: Tìm từ dài nhất, ngắn nhất trong list ---
words = ["apple", "banana", "cherry", "date"]

# Cách 1: Dùng for để tìm từ dài nhất/ngắn nhất
dai_nhat = words[0]               # Giả sử phần tử đầu tiên là dài nhất
ngan_nhat = words[0]              # Giả sử phần tử đầu tiên là ngắn nhất
for tu in words:                  # Duyệt từng từ trong danh sách
    if len(tu) > len(dai_nhat):   # Nếu từ này dài hơn từ dài nhất hiện tại
        dai_nhat = tu             # Gán lại là dài nhất mới
    if len(tu) < len(ngan_nhat):  # Nếu từ này ngắn hơn từ ngắn nhất hiện tại
        ngan_nhat = tu            # Gán lại là ngắn nhất mới
print("Từ dài nhất:", dai_nhat)
print("Từ ngắn nhất:", ngan_nhat)

# Cách 2: Dùng max, min với key=len cho ngắn gọn
print("Từ dài nhất:", max(words, key=len))
print("Từ ngắn nhất:", min(words, key=len))

# --- Bài 2: Đếm số từ chứa ký tự cho trước (vd: 'a') ---
words = ["apple", "banana", "cherry", "date"]
dem = 0                                   # Biến đếm số từ thỏa điều kiện
for tu in words:
    if "a" in tu:                         # Nếu từ có chứa ký tự 'a'
        dem += 1                          # Tăng biến đếm lên 1
print("Số từ chứa 'a':", dem)

# --- Bài 3: Đếm số từ có độ dài lớn hơn 5 ---
words = ["apple", "banana", "cherry", "date"]
dem = 0                                   # Biến đếm số từ thỏa điều kiện
for tu in words:
    if len(tu) > 5:                       # Nếu độ dài từ lớn hơn 5
        dem += 1                          # Tăng biến đếm lên 1
print("Số từ dài hơn 5 ký tự:", dem)

# --- Bài 4: Tạo list mới gồm các từ viết hoa/thường ---
words = ["Python", "là", "Ngôn", "ngữ", "Tuyệt", "Vời"]
chu_hoa = []                              # List chứa các từ viết HOA
chu_thuong = []                           # List chứa các từ viết thường
for tu in words:
    chu_hoa.append(tu.upper())            # Đổi sang chữ HOA và thêm vào list
    chu_thuong.append(tu.lower())         # Đổi sang chữ thường và thêm vào list
print("Các từ viết HOA:", chu_hoa)
print("Các từ viết thường:", chu_thuong)

# Viết gọn hơn bằng list comprehension:
print([tu.upper() for tu in words])
print([tu.lower() for tu in words])

# --- Bài 5: Ghép các từ trong list thành một câu ---
words = ["Python", "là", "ngôn", "ngữ", "lập", "trình", "tuyệt", "vời"]
cau = " ".join(words)                     # Ghép các từ, mỗi từ cách nhau bằng dấu cách
print("Câu sau khi ghép:", cau)

# --- Bài 6: Tách một câu thành các từ ---
cau = "Python là ngôn ngữ lập trình tuyệt vời"
ds_tu = cau.split()                       # Tách câu thành list các từ (cắt theo dấu cách)
print("Danh sách từ:", ds_tu)
