# Bài 1: Lọc các từ là chữ viết hoa toàn bộ
chuoi = ["GPT", "AI", "NASA", "chat"]
ds = []
for tu in chuoi:                      # Duyệt từng từ trong danh sách
  if tu.isupper():                   # Nếu từ là viết hoa toàn bộ
    ds.append(tu)                    # Thêm vào danh sách kết quả
print(ds)

# Bài 2: Lọc các từ là chữ viết thường toàn bộ
chuoi = ["hello", "python", "chatbot"]
ds = []
for tu in chuoi:
  if tu.islower():                   # Nếu từ là chữ thường toàn bộ
    ds.append(tu)
print(ds)

# Bài 3: Lọc các từ viết hoa chữ cái đầu (dạng title)
chuoi = ["Today", "is", "a", "Beautiful", "Day", "in", "VietNam", "and", "HaNoi"]
ds = []
for tu in chuoi:
  if tu.istitle():                   # Nếu từ có chữ cái đầu viết hoa
    ds.append(tu)
print(ds)

# Bài 4: Lọc các từ chỉ gồm ký tự đặc biệt (không phải chữ, không phải số)
chuoi = ["hello!", "good_morning", "nice-day", "100%"]
ds = []
for tu in chuoi:
  if not tu.isalnum():               # Nếu từ không phải là chữ hoặc số
    ds.append(tu)
print(ds)

# Bài 5: Lọc các từ chứa cả chữ và số
chuoi = ["user123", "admin", "super007", "456", "hello42", "GPT"]
ds = []
for tu in chuoi:
  if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):  # Có ít nhất 1 chữ và 1 số
    ds.append(tu)
print(ds)

# Bài 6: Lọc các từ có cả chữ thường và chữ hoa
chuoi = ["Python", "GPT", "ai", "ChatBot", "HELLO", "code"]
ds = []
for tu in chuoi:
  if any(c.islower() for c in tu) and any(c.isupper() for c in tu):  # Có ít nhất 1 thường và 1 hoa
    ds.append(tu)
print(ds)

# Bài 7: Lọc các từ không phải là chữ hoặc số
chuoi = ["hello!", "good_morning", "nice-day", "100%"]
ds = []
for tu in chuoi:
  if not tu.isalnum():               # Loại bỏ từ toàn là chữ hoặc số
    ds.append(tu)
print(ds)

# Bài 8: Lọc từ là chữ thường và có ít nhất 1 số
chuoi = ["python3", "hello", "GPT4", "chat42", "AI", "gpt", "gpt123"]
ds = []
for tu in chuoi:
  if tu.islower() and any(c.isdigit() for c in tu):  # Toàn bộ chữ là thường + có ít nhất 1 số
    ds.append(tu)
print(ds)

# Bài 9: Lọc từ có cả chữ hoa và chữ thường
chuoi = ["GPT", "chatBot", "python", "OpenAI", "AI", "CODE", "learn123"]
ds = []
for tu in chuoi:
  if any(c.islower() for c in tu) and any(c.isupper() for c in tu):  # Có ít nhất 1 hoa và 1 thường
    ds.append(tu)
print(ds)

# Bài 10: Lọc từ chứa cả chữ cái và số
chuoi = ["abc123", "hello", "456", "gpt", "GPT4", "123AI", "AI123", "!@#", "hi5"]
ds = []
for tu in chuoi:
  if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):  # Có cả chữ và số
    ds.append(tu)
print(ds)

# 3 công thức mẫu quan trọng


""" 1. Có cả chữ và số:
if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):

# 2. Có cả chữ thường và chữ hoa:
if any(c.islower() for c in tu) and any(c.isupper() for c in tu):

# 3. Là chữ thường toàn bộ và có ít nhất 1 số:
if tu.islower() and any(c.isdigit() for c in tu):    """
