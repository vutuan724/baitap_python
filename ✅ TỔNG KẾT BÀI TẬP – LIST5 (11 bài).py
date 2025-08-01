# List5 – Bài 1: Lấy từ viết hoa toàn bộ (isupper)
chuoi = ["GPT", "python", "AI", "tool", "OPENAI", "chat"]
ds = []
for tu in chuoi:                  # Duyệt từng từ trong danh sách
  if tu.isupper():               # Nếu từ đó là toàn chữ in hoa
    ds.append(tu)                # Thêm từ vào danh sách kết quả
print(ds)                        # In kết quả

# List5 – Bài 2: Lấy từ viết thường toàn bộ (islower)
chuoi = ["Hello", "world", "PYTHON", "code", "chatGPT", "tool"]
chu_thuong = []
for tu in chuoi:
  if tu.islower():               # Nếu từ là toàn chữ thường
    chu_thuong.append(tu)
print(chu_thuong)

# List5 – Bài 3: Lấy từ có chữ cái đầu viết hoa (istitle)
chuoi = ["Hello", "world", "OpenAI", "GPT", "python", "chatGPT"]
chu_hoa = []
for tu in chuoi:
  if tu.istitle():               # Nếu từ có chữ cái đầu in hoa
    chu_hoa.append(tu)
print(f"chữ hoa là:", chu_hoa)

# List5 – Bài 4: Lấy từ chứa chữ và số (any + isalpha + isdigit)
chuoi = ["user123", "admin", "super007", "456", "hello42", "GPT"]
ds = []
for tu in chuoi:
  if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):
    # Nếu có ít nhất 1 chữ và 1 số
    ds.append(tu)
print(ds)

# List5 – Bài 5: Lấy từ chứa chữ thường và số
chuoi = ["python3", "hello", "GPT4", "chat42", "AI", "gpt", "gpt123"]
ds = []
for tu in chuoi:
  if any(c.islower() for c in tu) and any(c.isdigit() for c in tu):
    # Nếu có ít nhất 1 chữ thường và 1 số
    ds.append(tu)
print(ds)

# List5 – Bài 6: Lấy từ chỉ chứa chữ và số (isalnum)
chuoi = ["abc!", "hello123", "456", "GPT", "code$", "learn_python", "data"]
ds = []
for tu in chuoi:
  if tu.isalnum():               # Nếu từ chỉ gồm chữ và số, không có ký tự đặc biệt
    ds.append(tu)
print(ds)

# List5 – Bài 7: Lấy từ chứa ký tự đặc biệt (not isalnum)
chuoi = ["hello!", "good_morning", "nice-day", "100%"]
ds = []
for tu in chuoi:
  if not tu.isalnum():           # Nếu từ có ký tự đặc biệt
    ds.append(tu)
print(f"ký tự đặc biệt là:", ds)

# List5 – Bài 8: Lấy từ có ít nhất 1 chữ và 1 số (any + isalpha + isdigit)
chuoi = ["abc123", "hello", "456", "gpt", "GPT4", "123AI", "AI123", "!@#", "hi5"]
ds = []
for tu in chuoi:
  if any(c.isalpha() for c in tu) and any(c.isdigit() for c in tu):
    ds.append(tu)
print(ds)

# List5 – Bài 9: Lấy từ chỉ chứa chữ cái và số (isalnum)
chuoi = ["abc!", "hello123", "456", "GPT", "code$", "learn_python", "data"]
ds = []
for tu in chuoi:
  if tu.isalnum():
    ds.append(tu)
print(ds)

# List5 – Bài 10: Lấy từ chỉ toàn chữ cái (isalpha)
chuoi = ["hello", "123", "chatGPT", "AI", "code123", "python!", "OpenAI", "abc"]
ds = []
for tu in chuoi:
  if tu.isalpha():               # Nếu từ chỉ toàn là chữ cái (không có số hay ký tự đặc biệt)
    ds.append(tu)
print(ds)

# List5 – Bài 11: Lấy từ có ít nhất 1 chữ thường và 1 chữ hoa
chuoi = ["hello", "GPT", "ChatBot", "AI", "python3", "OpenAI", "CODE", "gpt4"]
ds = []
for tu in chuoi:
  if any(c.islower() for c in tu) and any(c.isupper() for c in tu):
    # Nếu có cả chữ thường và chữ hoa
    ds.append(tu)
print(ds)
