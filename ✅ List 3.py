# --------------------- List3 - Bài 1 ---------------------
# Lấy các chữ số trong chuỗi, chuyển thành số nguyên
chuoi = "abc12xy9m5"
result = []
for char in chuoi:                      # Duyệt từng ký tự trong chuỗi
    if char.isdigit():                 # Nếu là chữ số
        result.append(int(char))       # Chuyển thành số nguyên rồi thêm vào danh sách
print(result)                          # Kết quả: [1, 2, 9, 5]


# --------------------- List3 - Bài 2 ---------------------
# Lấy các chữ cái trong chuỗi
chuoi = "a1B#2cD!"
chu_cai = []
for text in chuoi:                     # Duyệt từng ký tự
    if text.isalpha():                # Nếu là chữ cái
        chu_cai.append(text)          # Thêm vào danh sách
print(chu_cai)                         # Kết quả: ['a', 'B', 'c', 'D']


# --------------------- List3 - Bài 3 ---------------------
# Lấy ký tự đặc biệt (không phải chữ, không phải số)
chuoi = "a1B#2cD!"
ky_tu = []
for chu in chuoi:
    if not chu.isalpha() and not chu.isdigit():  # Nếu không phải chữ, không phải số
        ky_tu.append(chu)
print(ky_tu)                          # Kết quả: ['#', '!']


# --------------------- List3 - Bài 4 ---------------------
# Gom nhóm các số liền nhau thành số nguyên
chuoi = "abc12xy9m56"
so = []
temp = ""                             # Biến tạm để nối các chữ số liền nhau
for c in chuoi:
    if c.isdigit():                   # Nếu là số → nối vào temp
        temp += c
    else:                             # Gặp chữ hoặc ký tự khác
        if temp:                      # Nếu temp đang có số
            so.append(int(temp))      # Đưa vào kết quả
            temp = ""                 # Xóa temp để bắt đầu lại
if temp:                              # Nếu kết thúc chuỗi mà temp vẫn còn số
    so.append(int(temp))
print(so)                             # Kết quả: [12, 9, 56]


# --------------------- List3 - Bài 5 ---------------------
# Lấy từ viết hoa chữ cái đầu (viết hoa kiểu Title)
chuoi = "Today is a beautiful Day in VietNam and HaNoi."
ds = []
for tu in chuoi.split():              # Duyệt từng từ
    if tu.isalpha() and tu.istitle(): # Nếu từ toàn chữ và viết hoa chữ cái đầu
        ds.append(tu)
print(ds)                             # Kết quả: ['Today', 'Day']


# --------------------- List3 - Bài 6 ---------------------
# Lấy từ viết thường hoàn toàn
chuoi = "hello world Python GPT openai gpt4"
ds = []
for tu in chuoi.split():
    if tu.isalpha() and tu.islower():  # Từ toàn chữ và viết thường
        ds.append(tu)
print(ds)                              # Kết quả: ['hello', 'world', 'openai']


# --------------------- List3 - Bài 7 ---------------------
# Lấy từ viết HOA hoàn toàn
chuoi = "This is GPT AI and NASA"
ds = []
for tu in chuoi.split():
    if tu.isupper():                   # Nếu toàn bộ viết hoa
        ds.append(tu)
print(ds)                              # Kết quả: ['GPT', 'AI', 'NASA']


# --------------------- List3 - Bài 8 ---------------------
# Lấy từ chứa cả chữ và số (dùng any)
chuoi = "user123 admin super007 456 hello42 GPT"
ds = []
for tu in chuoi.split():
    if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):
        ds.append(tu)                  # Nếu có cả chữ và số → thêm vào danh sách
print(ds)                              # Kết quả: ['user123', 'super007', 'hello42']


# --------------------- List3 - Bài 9 ---------------------
# Bài luyện tập lại giống bài 8
chuoi = "abc123 789 !@# abc DEF123 ghi56 123ghi GHI"
ds = []
for tu in chuoi.split():
    if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):
        ds.append(tu)
print(ds)                              # Kết quả: ['abc123', 'DEF123', 'ghi56', '123ghi']


# --------------------- List3 - Bài 10 ---------------------
# Viết lại bài 8 mà không dùng any() – dùng biến diễn giải
chuoi = "abc123 xyz hello45"
ds = []
for tu in chuoi.split():               # Duyệt từng từ
    co_chu = False                     # Biến giả định ban đầu: chưa có chữ
    co_so = False                      # Biến giả định ban đầu: chưa có số
    for c in tu:                       # Duyệt từng ký tự trong từ
        if c.isalpha():
            co_chu = True
        if c.isdigit():
            co_so = True
    if co_chu and co_so:               # Nếu có cả chữ và số
        ds.append(tu)
print(ds)                              # Kết quả: ['abc123', 'hello45']

# --------------------- List3 - Bài 10 ---------------------
# Lấy các từ chứa cả chữ và số
# Viết theo kiểu KHÔNG dùng any(), mà dùng for và biến logic

chuoi = "abc123 xyz hello45"
ds = []
for tu in chuoi.split():               # Duyệt từng từ
    co_chu = False                     # Biến giả định: chưa thấy chữ
    co_so = False                      # Biến giả định: chưa thấy số
    for c in tu:                       # Duyệt từng ký tự
        if c.isalpha():
            co_chu = True             # Ghi nhận nếu thấy chữ
        if c.isdigit():
            co_so = True              # Ghi nhận nếu thấy số
    if co_chu and co_so:              # Nếu thấy cả chữ và số
        ds.append(tu)
print(ds)                              # Kết quả: ['abc123', 'hello45']

# ----------- Ghi chú mở rộng: cách viết bằng any() cho nhanh hơn -----------

# if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):
#     ds.append(tu)

# Dùng any() giúp viết gọn, nhưng dùng for+biến giúp học sâu và thấy rõ logic hoạt động từng bước.
