# List 8 - Bài tập nâng cao: Xử lý List & String

#----------------------------------------
# Bài 1 - Tìm từ dài nhất và ngắn nhất trong danh sách

cities = ["Hanoi", "Ho Chi Minh", "Da Nang", "Hue", "Nha Trang", "Can Tho", "Vung Tau"]  # Danh sách mẫu

# --- Cách 1: Dùng vòng lặp for ---
dai_nhat = cities[0]   # Giả sử ban đầu phần tử đầu là dài nhất
ngan_nhat = cities[0]  # Giả sử ban đầu phần tử đầu là ngắn nhất
for tu in cities:                      # Duyệt từng thành phố trong danh sách
    if len(tu) > len(dai_nhat):        # Nếu thành phố hiện tại dài hơn "dai_nhat"
        dai_nhat = tu                  # thì cập nhật lại "dai_nhat"
    if len(tu) < len(ngan_nhat):       # Nếu thành phố hiện tại ngắn hơn "ngan_nhat"
        ngan_nhat = tu                 # thì cập nhật lại "ngan_nhat"
print(dai_nhat, ngan_nhat)  # 👉 Ho Chi Minh Hue

# --- Cách 2: Dùng max/min với key=len ---
dai_nhat = max(cities, key=len)        # Lấy thành phố có độ dài lớn nhất
ngan_nhat = min(cities, key=len)       # Lấy thành phố có độ dài nhỏ nhất
print(dai_nhat, ngan_nhat)  # 👉 Ho Chi Minh Hue

#----------------------------------------
# Bài 2 - Đếm số từ chứa ký tự nhất định trong danh sách

animals = ["cat", "dog", "rabbit", "elephant", "tiger", "ant", "goat", "bat"]  # Danh sách mẫu

# --- Cách 1: Dùng vòng lặp for ---
chu_a = 0   # Đếm số từ chứa 'a'
chu_t = 0   # Đếm số từ chứa 't'
for tu in animals:          # Duyệt từng từ
    if "a" in tu:           # Nếu từ chứa chữ 'a'
        chu_a += 1          # tăng biến đếm chu_a
    if "t" in tu:           # Nếu từ chứa chữ 't'
        chu_t += 1          # tăng biến đếm chu_t
print(chu_a, chu_t)  # 👉 6 5

# --- Cách 2: Dùng sum với điều kiện ---
chu_a = sum(1 for tu in animals if "a" in tu)  # Đếm số từ chứa 'a'
chu_t = sum(1 for tu in animals if "t" in tu)  # Đếm số từ chứa 't'
print(chu_a, chu_t)  # 👉 6 5

#----------------------------------------
# Bài 3 - Đếm số từ chứa nhiều ký tự khác nhau (nâng cao)

# --- Cách 1: Dùng for lồng for ---
for ky_tu in "at":                        # Lặp qua từng ký tự cần kiểm tra: 'a' và 't'
    dem = 0                               # Biến đếm số từ thỏa mãn
    for tu in animals:                    # Duyệt từng từ trong danh sách
        if ky_tu in tu:                   # Nếu ký tự xuất hiện trong từ
            dem += 1                      # tăng biến đếm
    print(f"Số từ chứa '{ky_tu}': {dem}") # In kết quả

# 👉 Số từ chứa 'a': 6
# 👉 Số từ chứa 't': 5

# --- Cách 2: Dùng sum cho ngắn gọn ---
for ky_tu in "at":                                # Lặp từng ký tự
    print(f"Số từ chứa '{ky_tu}':", sum(1 for tu in animals if ky_tu in tu))

#----------------------------------------
# Bài 4 - Chuyển tất cả từ trong list thành chữ HOA hoặc chữ thường

words = ["Python", "là", "Ngôn", "ngữ", "Tuyệt", "Vời"]  # Danh sách từ gốc

chu_hoa = []      # Tạo list mới để lưu từ viết hoa
chu_thuong = []   # Tạo list mới để lưu từ viết thường

for tu in words:              # Duyệt từng từ trong list
    hoa = tu.upper()          # Đổi từ thành chữ HOA
    chu_hoa.append(hoa)       # Thêm vào list chu_hoa
    thuong = tu.lower()       # Đổi từ thành chữ thường
    chu_thuong.append(thuong) # Thêm vào list chu_thuong

print(chu_hoa)     # 👉 ['PYTHON', 'LÀ', 'NGÔN', 'NGỮ', 'TUYỆT', 'VỜI']
print(chu_thuong)  # 👉 ['python', 'là', 'ngôn', 'ngữ', 'tuyệt', 'vời']

# --- GHI CHÚ: Cách viết ngắn gọn hơn với list comprehension ---
chu_hoa = [tu.upper() for tu in words]      # List mới gồm toàn bộ từ viết HOA
chu_thuong = [tu.lower() for tu in words]   # List mới gồm toàn bộ từ viết thường
print(chu_hoa)
print(chu_thuong)

# Bài 5 - Lọc các từ có độ dài lớn hơn n

words = ["Python", "là", "ngôn", "ngữ", "tuyệt", "vời", "cơ", "bản"]

# --- Cách 1: Dùng vòng lặp for ---
tu_dai = []                        # List mới để lưu từ dài hơn 3 ký tự
for tu in words:                   # Duyệt từng từ
    if len(tu) > 3:                # Nếu dài hơn 3 ký tự
        tu_dai.append(tu)          # Thêm vào list mới
print(tu_dai)    # 👉 ['Python', 'ngôn', 'ngữ', 'tuyệt', 'vời', 'bản']

# --- Cách 2: Dùng list comprehension ---
tu_dai = [tu for tu in words if len(tu) > 3]
print(tu_dai)    # 👉 ['Python', 'ngôn', 'ngữ', 'tuyệt', 'vời', 'bản']

# Bài 6 - Ghép các từ thành một câu

words = ["Python", "là", "ngôn", "ngữ", "lập", "trình", "tuyệt", "vời"]

# --- Cách 1: Dùng ' '.join() ---
cau = " ".join(words)
print(cau)  # 👉 Python là ngôn ngữ lập trình tuyệt vời

# --- Cách 2: Dùng vòng lặp for ---
cau = ""
for tu in words:
    cau += tu + " "
cau = cau.strip()   # Xóa dấu cách cuối chuỗi
print(cau)  # 👉 Python là ngôn ngữ lập trình tuyệt vời


# ========================

# ------- Bài 7: Tách một câu thành các từ, loại bỏ dấu câu -------
import string
cau = "Python, la ngon ngu lap trinh tuyet voi!"
bang_xoa = str.maketrans('', '', string.punctuation)      # Tạo bảng xóa các dấu câu
cau_khong_dau = cau.translate(bang_xoa)                  # Xóa dấu câu khỏi chuỗi
ds_tu = cau_khong_dau.split()                            # Tách thành danh sách từ
print(ds_tu)    # 👉 ['Python', 'la', 'ngon', 'ngu', 'lap', 'trinh', 'tuyet', 'voi']

# ------- Bài 8: Tìm các từ vừa có số vừa có chữ trong danh sách -------
ds_tu = ["abc123", "hello", "123", "abc", "x1y2", "2024", "openai4", "chat", "py"]
ds = []                        # List mới để lưu từ thỏa điều kiện
for tu in ds_tu:
    co_chu = any(c.isalpha() for c in tu)    # Kiểm tra có chữ không
    co_so = any(c.isdigit() for c in tu)     # Kiểm tra có số không
    if co_chu and co_so:                     # Nếu cả 2 điều kiện đúng
        ds.append(tu)                        # Thêm từ vào list kết quả
print(ds)    # 👉 ['abc123', 'x1y2', 'openai4']

# ------- Bài 9: Tìm từ xuất hiện nhiều nhất trong danh sách -------

ds_tu = ["cat", "dog", "cat", "dog", "cat", "mouse", "cat", "dog", "dog"]

tu_max = ds_tu[0]                  # 1. Giả sử từ đầu tiên là nhiều nhất
so_lan_max = ds_tu.count(ds_tu[0]) # 2. Đếm số lần xuất hiện của từ đầu tiên (gán làm giá trị lớn nhất ban đầu)

for tu in ds_tu:                   # 3. Duyệt từng từ trong danh sách
    dem = ds_tu.count(tu)          #    - Đếm số lần từ hiện tại xuất hiện trong danh sách
    if dem > so_lan_max:           #    - Nếu số lần này lớn hơn số lần lớn nhất đang có
        so_lan_max = dem           #        → Cập nhật lại số lớn nhất (so_lan_max)
        tu_max = tu                #        → Cập nhật lại từ nhiều nhất (tu_max)

# 4. Kết thúc vòng lặp, in ra kết quả:
print(f"Từ xuất hiện nhiều nhất: {tu_max}, xuất hiện {so_lan_max} lần.")
# 👉 Từ xuất hiện nhiều nhất: dog, xuất hiện 4 lần.

# ------- Bài 10: Đếm/lọc các từ là chữ HOA hoàn toàn trong list -------
ds_tu = ["PYTHON", "java", "CODE", "Python", "AI", "ML", "hello"]
ds = []                    # List mới để lưu các từ là chữ HOA hoàn toàn
for tu in ds_tu:
    if tu == tu.upper():   # Nếu từ đó là chữ HOA hoàn toàn
        ds.append(tu)
print(ds)  # 👉 ['PYTHON', 'CODE', 'AI', 'ML']
# Nếu chỉ muốn đếm số lượng từ là chữ HOA:
# print(len(ds))  # 👉 4
#Bài 11 - Đếm số lần xuất hiện của từng từ trong chuỗi
chuoi = "cat dog cat dog cat mouse cat dog dog"
chuoi= chuoi.split()
ds=[]
for tu in chuoi:
  co_tu = False
  for tu_moi in ds:
    if tu == tu_moi[0]:
      tu_moi[1] +=1
      co_tu = True
      break
  if not co_tu:
    ds.append([tu,1])
print(ds )
""" chuoi = "cat dog cat dog cat mouse cat dog dog"

Đây là dữ liệu đầu vào của bạn.

chuoi = chuoi.split()

Dòng này biến chuỗi thành một danh sách các từ: ['cat', 'dog', 'cat', 'dog', 'cat', 'mouse', 'cat', 'dog', 'dog'].

ds = []

Đây là danh sách kết quả của bạn, ban đầu nó rỗng. Dòng này là bước chuẩn bị để lưu trữ các cặp [từ, số đếm].

for tu in chuoi:

Đây là vòng lặp ngoài. Nó duyệt qua từng từ trong danh sách ban đầu của bạn, ví dụ cat, sau đó dog, rồi cat lần nữa,...

co_tu = False

Đây là một biến cờ hiệu. Bạn đã đặt nó là False trước mỗi lần lặp của vòng lặp ngoài. Nó giống như một lời hứa: "Tôi chưa tìm thấy từ này trong danh sách kết quả đâu."

for tu_moi in ds:

Đây là vòng lặp trong. Nó duyệt qua từng cặp [từ, số đếm] trong danh sách kết quả ds để tìm xem từ hiện tại đã có ở đó chưa.

if tu == tu_moi[0]:

Đây là câu lệnh kiểm tra. Nó so sánh từ hiện tại (tu) với từ trong danh sách kết quả (tu_moi[0]).

tu_moi[1] += 1

Nếu hai từ khớp nhau, dòng này sẽ tăng số đếm lên 1.

co_tu = True

Nếu tìm thấy từ, bạn đã đúng khi đặt biến cờ hiệu thành True. "Lời hứa" lúc nãy đã được thực hiện.

break

Vì đã tìm thấy từ, bạn không cần phải duyệt tiếp nữa. Lệnh này giúp thoát khỏi vòng lặp trong để tiết kiệm thời gian.

if not co_tu:

Dòng này kiểm tra. Nếu biến cờ hiệu vẫn là False (sau khi vòng lặp trong kết thúc), điều đó có nghĩa là từ này là từ mới.

ds.append([tu, 1])

Vì là từ mới, dòng này thêm từ đó vào danh sách kết quả với số đếm ban đầu là 1.

print(ds)

Cuối cùng, dòng này in ra kết quả.   """