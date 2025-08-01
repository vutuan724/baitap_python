# Danh sách bài tập tổng hợp thực tế Python

bai_tap = [
    "1. Quản lý danh bạ điện thoại: \
    - Nhập nhiều tên và số điện thoại (dictionary). \
    - Tìm số điện thoại theo tên, thêm/xóa/sửa liên hệ.",
    
    "2. Quản lý điểm học sinh: \
    - Nhập tên, điểm cho nhiều học sinh (list/dictionary). \
    - Tìm học sinh điểm cao/thấp nhất, tính điểm trung bình, tìm kiếm theo tên.",
    
    "3. Đếm số lần xuất hiện của từng từ trong câu: \
    - Nhập một chuỗi. \
    - Tách từ, đếm số lần xuất hiện từng từ (dictionary).",
    
    "4. Kiểm tra mật khẩu mạnh/yếu: \
    - Nhập mật khẩu. \
    - Kiểm tra độ dài, có số, chữ hoa, ký tự đặc biệt chưa (string, if, for, hàm chuỗi).",
    
    "5. Thống kê số lượng các chữ cái, chữ số trong chuỗi: \
    - Nhập chuỗi. \
    - Đếm số ký tự chữ, số, ký tự đặc biệt (string, biến đếm, .isalpha(), .isdigit()).",
    
    "6. Tính tổng, tích, trung bình một dãy số: \
    - Nhập dãy số, lưu vào list. \
    - Tính tổng (sum), tích (dùng for), trung bình (sum/len).",
    
    "7. Quản lý sản phẩm: \
    - Nhập tên, giá, số lượng sản phẩm (list/dictionary). \
    - Tính tổng giá trị hàng hóa, thêm/xóa/sửa sản phẩm.",
]

# Gợi ý: Bạn có thể in ra danh sách này để lựa chọn
"""for bt in bai_tap:
    print(bt)  """
# --- BÀI TOÁN 1: QUẢN LÝ DANH BẠ ĐIỆN THOẠI ---

danh_ba = {}

# Vòng lặp chính để hiển thị menu và xử lý yêu cầu của người dùng.
while True:
    print("\n--- MENU QUẢN LÝ DANH BẠ ---")
    print("1. Thêm liên hệ mới")
    print("2. Tìm kiếm số điện thoại")
    print("3. Sửa số điện thoại")
    print("4. Xóa liên hệ")
    print("5. Hiển thị tất cả liên hệ")
    print("6. Thoát")
    
    lua_chon = input("Nhập lựa chọn của bạn (1-6): ")

    if lua_chon == "1":
        # CHỨC NĂNG: Thêm liên hệ mới
        ten = input("Nhập tên: ")
        so_dien_thoai = input("Nhập số điện thoại: ")
        
        # Bạn hãy viết code để thêm tên và số điện thoại vào dictionary ở đây.
        # Gợi ý: danh_ba[ten] = so_dien_thoai

        print(f"Đã thêm liên hệ '{ten}'.")

    elif lua_chon == "2":
        # CHỨC NĂNG: Tìm kiếm số điện thoại
        ten = input("Nhập tên bạn muốn tìm: ")
        
        # Bạn hãy viết code để kiểm tra xem tên này có trong danh bạ không.
        # Gợi ý: Sử dụng `if ten in danh_ba:`
        
        # Nếu có, in ra số điện thoại. Ngược lại, báo không tìm thấy.
        print("Kết quả tìm kiếm...")

    elif lua_chon == "3":
        # CHỨC NĂNG: Sửa số điện thoại
        ten = input("Nhập tên liên hệ cần sửa: ")
        
        # Bạn hãy viết code để kiểm tra xem tên có trong danh bạ không.
        # Nếu có, yêu cầu nhập số điện thoại mới và cập nhật. Ngược lại, báo không tìm thấy.
        # Gợi ý: Dòng code để sửa tương tự như dòng thêm mới.

    elif lua_chon == "4":
        # CHỨC NĂNG: Xóa liên hệ
        ten = input("Nhập tên liên hệ cần xóa: ")
        
        # Bạn hãy viết code để kiểm tra và xóa liên hệ này khỏi dictionary.
        # Gợi ý: Sử dụng `if ten in danh_ba:` và `del danh_ba[ten]`.

    elif lua_chon == "5":
        # CHỨC NĂNG: Hiển thị tất cả liên hệ
        if danh_ba:
            print("--- DANH BẠ ---")
            # Bạn hãy viết code để duyệt qua dictionary và in ra tất cả tên và số điện thoại.
            # Gợi ý: Sử dụng vòng lặp `for ten, so in danh_ba.items():`
        else:
            print("Danh bạ rỗng.")

    elif lua_chon == "6":
        # CHỨC NĂNG: Thoát chương trình
        print("Thoát chương trình. Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 6.")

#✅ CÁCH LÀM DIỄN GIẢI TỪNG BAI TẬP

# --- BÀI TOÁN 1: QUẢN LÝ DANH BẠ ĐIỆN THOẠI ---

print("--- Quản lý danh bạ điện thoại ---")

# Khởi tạo một dictionary rỗng để lưu trữ các cặp tên (khóa) và số điện thoại (giá trị).
danh_ba = {}

# Bắt đầu một vòng lặp vô hạn để nhập liệu linh hoạt.
while True:
    # Lấy tên từ người dùng.
    ten = input("Nhập tên liên hệ (hoặc nhấn Enter để dừng): ")
    
    # Kiểm tra nếu người dùng nhấn Enter, thì thoát khỏi vòng lặp.
    if ten == "":
        break
    
    # Lấy số điện thoại tương ứng.
    so_dien_thoai = input(f"Nhập số điện thoại của {ten}: ")
    
    # Thêm cặp tên-số điện thoại vào dictionary.
    danh_ba[ten] = so_dien_thoai
    
print("\n")
print("Danh bạ hiện tại:")
print(danh_ba)

print("\n" + "="*50 + "\n")


# --- BÀI TOÁN 2: QUẢN LÝ ĐIỂM SỐ HỌC SINH ---

print("--- Quản lý điểm số học sinh ---")

# Khởi tạo một dictionary rỗng để lưu tên và điểm số.
danh_sach_hoc_sinh = {}

# Vòng lặp nhập liệu tương tự như trên.
while True:
    ten = input("Nhập tên học sinh (hoặc nhấn Enter để dừng): ")
    if ten == "":
        break
    
    # Chuyển đổi điểm số sang kiểu số thực (float) để tính toán chính xác.
    diem = float(input(f"Nhập điểm của {ten}: "))
    danh_sach_hoc_sinh[ten] = diem

print("\n")

# Kiểm tra để tránh lỗi khi dictionary rỗng.
if danh_sach_hoc_sinh:
    
    # --- 2.1: Tìm học sinh có điểm cao nhất ---
    # Lấy danh sách tất cả các điểm số để tìm điểm cao nhất.
    diem_lon_nhat = max(danh_sach_hoc_sinh.values())
            
    print("Học sinh có điểm cao nhất:")
    # Duyệt qua các cặp khóa-giá trị để tìm tên tương ứng với điểm số cao nhất.
    for ten_hs, diem_hs in danh_sach_hoc_sinh.items():
        if diem_hs == diem_lon_nhat:
            print(f"- Tên: {ten_hs}, Điểm: {diem_hs}")

    print("\n")

    # --- 2.2: Tính điểm trung bình của tất cả học sinh ---
    # Sử dụng hàm sum() để tính tổng tất cả các điểm số.
    tong_diem = sum(danh_sach_hoc_sinh.values())
    
    # Sử dụng hàm len() để đếm số lượng học sinh.
    so_luong_hoc_sinh = len(danh_sach_hoc_sinh)
    
    # Tính điểm trung bình bằng phép chia thông thường.
    diem_trung_binh = tong_diem / so_luong_hoc_sinh
    
    # In kết quả với định dạng làm tròn 2 chữ số thập phân.
    print(f"Điểm trung bình của lớp là: {diem_trung_binh:.2f}")

else:
    print("Không có dữ liệu học sinh nào được nhập.")

print("\n" + "="*50 + "\n")

    #Tìm kiếm theo tên.
    


# --- BÀI TOÁN 3: ĐẾM SỐ LẦN XUẤT HIỆN CỦA TỪ ---

print("--- Đếm số lần xuất hiện của từng từ ---")

# Dữ liệu mẫu ban đầu.
cau_chuoi = "cat dog cat dog cat mouse cat dog dog"
# Tách chuỗi thành một danh sách các từ.
danh_sach_tu = cau_chuoi.split()

print(f"Câu gốc: '{cau_chuoi}'")
print("\n")

# --- CÁCH 1: Sử dụng Dictionary (Cách làm hiệu quả và chuyên nghiệp) ---
dem_tu_dic = {}
for tu in danh_sach_tu:
    # Nếu từ đã tồn tại trong dictionary...
    if tu in dem_tu_dic:
        # ...thì tăng giá trị đếm của nó lên 1.
        dem_tu_dic[tu] += 1
    # Nếu từ chưa tồn tại...
    else:
        # ...thì thêm từ đó vào dictionary với giá trị đếm là 1.
        dem_tu_dic[tu] = 1

print("Kết quả đếm từ (sử dụng Dictionary):")
print(dem_tu_dic)
print("\n")


# --- CÁCH 2: Sử dụng List (Cách làm để ôn luyện tư duy vòng lặp lồng nhau) ---
dem_tu_list = []
for tu in danh_sach_tu:
    # Biến cờ hiệu để kiểm tra xem từ đã được tìm thấy chưa.
    da_tim_thay = False
    
    # Vòng lặp trong để duyệt qua danh sách kết quả hiện tại.
    for item in dem_tu_list:
        # item[0] là từ, item[1] là số đếm.
        if item[0] == tu:
            item[1] += 1
            da_tim_thay = True
            # Thoát vòng lặp trong vì đã tìm thấy từ.
            break
            
    # Nếu cờ hiệu vẫn là False sau khi duyệt xong vòng lặp trong...
    if not da_tim_thay:
        # ...thì thêm từ mới này vào danh sách kết quả với số đếm là 1.
        dem_tu_list.append([tu, 1])

print("Kết quả đếm từ (sử dụng List):")
print(dem_tu_list)       

# Câu 3:
chuoi = input("nhập chuỗi bất kỳ : ")
chuoi = chuoi.split()
danh_sach = {}
for tu in chuoi:
  if tu in danh_sach:
    danh_sach[tu] += 1
  else:
    danh_sach[tu] = 1
print(danh_sach)

# --- BÀI TOÁN 4: KIỂM TRA MẬT KHẨU MẠNH YẾU ---
import string # Thư viện này chứa các chuỗi ký tự hữu ích, ví dụ như ký tự đặc biệt.

# --- BÀI TOÁN 4: KIỂM TRA MẬT KHẨU MẠNH/YẾU ---

print("--- Kiểm tra mật khẩu mạnh/yếu ---")

# Lấy mật khẩu từ người dùng.
mk = input("Nhập mật khẩu: ")

# --- Các biến cờ hiệu (flags) để theo dõi từng tiêu chí ---
# Biến boolean này sẽ lưu kết quả kiểm tra độ dài.
do_dai = False 
# Biến này theo dõi xem có chữ số không.
co_so = False
# Biến này theo dõi xem có chữ in hoa không.
co_chu_hoa = False
# Biến này theo dõi xem có ký tự đặc biệt không.
cdac_biet = False


# --- Bước 1: Kiểm tra độ dài ---
# Dòng này kiểm tra độ dài và gán giá trị True/False cho biến cờ.
do_dai = (len(mk) >= 8)

# --- Bước 2: Duyệt qua từng ký tự để kiểm tra các tiêu chí khác ---
for ky_tu in mk:
    # Kiểm tra xem ký tự có phải chữ số không.
    if ky_tu.isdigit():
        co_so = True
    
    # Kiểm tra xem ký tự có phải chữ in hoa không.
    if ky_tu.isupper():
        co_chu_hoa = True
        
    # Kiểm tra xem ký tự có phải ký tự đặc biệt không.
    if ky_tu in string.punctuation:
        dac_biet = True

# --- Bước 3: Đưa ra kết luận cuối cùng ---
# Dùng toán tử 'and' để kiểm tra xem tất cả các cờ hiệu có cùng là True không.
if do_dai and co_so and co_chu_hoa and dac_biet:
    print("Mật khẩu mạnh!")
else:
    print("Mật khẩu yếu. Vui lòng nhập mật khẩu mạnh hơn:")
    
    # In ra các tiêu chí chưa đạt để người dùng biết cần sửa gì.
    if not do_dai:
        print("- Cần có ít nhất 8 ký tự.")
    if not co_so:
        print("- Cần có ít nhất một chữ số.")
    if not co_chu_hoa:
        print("- Cần có ít nhất một chữ cái in hoa.")
    if not dac_biet:
        print("- Cần có ít nhất một ký tự đặc biệt.")

# --- BÀI TOÁN 5: THỐNG KÊ SỐ LƯỢNG CHỮ CÁI, CHỮ SỐ TRONG CHUỖI ---
import string # Thư viện này chứa các chuỗi ký tự hữu ích, ví dụ như string.punctuation cho ký tự đặc biệt.

#✅ --- BÀI TOÁN 5: THỐNG KÊ SỐ LƯỢNG CÁC CHỮ CÁI, CHỮ SỐ TRONG CHUỖI ---

print("--- Thống kê ký tự trong chuỗi ---")

# Lấy chuỗi từ người dùng.
# (Bạn đã thử nghiệm với chuỗi cố định, giờ có thể thay bằng input() theo đúng yêu cầu đề bài)
chuoi = input("Nhập một chuỗi bất kỳ: ") 

# Khởi tạo các biến đếm cho từng loại ký tự.
# Ban đầu, số lượng của mỗi loại đều là 0.
so_chu = 0          # Đếm số lượng chữ cái
so_so = 0           # Đếm số lượng chữ số
ky_tu_db = 0        # Đếm số lượng ký tự đặc biệt

# Duyệt qua từng ký tự một trong chuỗi.
# Biến 'ky_tu' sẽ lần lượt nhận giá trị của từng ký tự trong 'chuoi'.
for ky_tu in chuoi:
    # --- Kiểm tra từng loại ký tự ---
    
    # Kiểm tra xem 'ky_tu' có phải là một chữ cái (a-z, A-Z) không.
    # Phương thức .isalpha() trả về True nếu là chữ cái, False nếu không.
    if ky_tu.isalpha():
        so_chu += 1  # Nếu là chữ cái, tăng biến đếm 'so_chu' lên 1.
    
    # Kiểm tra xem 'ky_tu' có phải là một chữ số (0-9) không.
    # Phương thức .isdigit() trả về True nếu là chữ số, False nếu không.
    elif ky_tu.isdigit(): # Sử dụng elif để đảm bảo một ký tự chỉ được đếm vào một loại duy nhất.
        so_so += 1   # Nếu là chữ số, tăng biến đếm 'so_so' lên 1.
    
    # Nếu ký tự không phải là chữ cái và cũng không phải là chữ số,
    # thì nó được coi là ký tự đặc biệt (hoặc khoảng trắng, dấu câu...).
    # Lưu ý: Điều kiện này cũng sẽ đếm cả khoảng trắng.
    else: 
        ky_tu_db += 1 # Tăng biến đếm 'ky_tu_db' lên 1.

# --- In ra kết quả cuối cùng ---
print(f"Trong chuỗi '{chuoi}':")
print(f"Số chữ cái: {so_chu}")
print(f"Số chữ số: {so_so}")
print(f"Số ký tự đặc biệt (bao gồm cả khoảng trắng): {ky_tu_db}")


#✅ Bai Tâp 6 - Tính tổng, tích, trung bình một dãy số
# --- BÀI TOÁN 6: TÍNH TỔNG, TÍCH, TRUNG BÌNH MỘT DÃY SỐ ---

print("--- Tính Tổng, Tích, Trung Bình của một Dãy Số ---")

# 1. Khởi tạo một danh sách rỗng để lưu trữ các số.
# Đây là nơi tất cả các số mà người dùng nhập vào sẽ được thêm vào.
day_so = []

# 2. Vòng lặp để nhập dữ liệu từ người dùng.
# 'while True' tạo một vòng lặp vô hạn, sẽ chạy cho đến khi gặp lệnh 'break'.
while True:
    # Yêu cầu người dùng nhập số, hoặc nhập 'n' để dừng.
    # input() luôn trả về một chuỗi (string).
    chuoi_nhap = input('Mời nhập số (hoặc nhập "n" để dừng lại): ')

    # Kiểm tra xem người dùng có muốn dừng nhập liệu không.
    # Nếu chuỗi nhập vào là "n", thoát khỏi vòng lặp.
    if chuoi_nhap == "n":
        break

    # 3. Xử lý và chuyển đổi dữ liệu nhập vào.
    # Khối 'try-except' được dùng để "thử" thực hiện một hành động
    # có thể gây lỗi (ở đây là chuyển chuỗi sang số) và "bắt" lỗi nếu nó xảy ra.
    try:
        # Chuyển đổi chuỗi nhập vào thành số thực (float).
        # Sử dụng float để có thể xử lý cả số nguyên và số thập phân.
        so = float(chuoi_nhap)
        
        # Nếu chuyển đổi thành công, thêm số đó vào danh sách 'day_so'.
        day_so.append(so)
    
    # Nếu việc chuyển đổi thất bại (ví dụ: người dùng nhập "abc"),
    # Python sẽ ném ra lỗi 'ValueError', và khối 'except' này sẽ được chạy.
    except ValueError:
        print("Đầu vào không hợp lệ. Vui lòng nhập một SỐ hoặc 'n' để dừng.")

# --- Sau khi đã thu thập xong dãy số ---

# 4. Tính Tổng.
# Hàm sum() là một hàm tích hợp sẵn của Python, giúp tính tổng các số trong một list.
tong = sum(day_so)
print(f"\nTổng của dãy số là: {tong}")

# 5. Tính Tích.
# Khởi tạo biến 'tich' là 1.
# Nếu khởi tạo là 0, thì dù nhân với số nào kết quả cũng sẽ là 0.
tich = 1
# Duyệt qua từng số trong 'day_so' để nhân dồn vào biến 'tich'.
for so_trong_list in day_so:
    tich = tich * so_trong_list
print(f"Tích của dãy số là: {tich}")

# 6. Tính Trung bình.
# Cần kiểm tra để tránh lỗi chia cho 0 nếu danh sách rỗng.
# Lỗi 'ZeroDivisionError' xảy ra khi chia cho 0.
if len(day_so) == 0:
    print("Không thể tính trung bình vì dãy số rỗng (chưa có số nào được nhập).")
else:
    # Nếu danh sách không rỗng, tính trung bình bằng tổng chia cho số lượng phần tử.
    tb = tong / len(day_so)
    print(f"Trung bình của dãy số là: {tb}")

#✅ Bài Tập 7 - Quản lý sản phẩm
# --- BÀI TOÁN 7: QUẢN LÝ SẢN
# PHẨM ---

import sys # Import thư viện sys để dùng sys.float_info.min và sys.float_info.max

# --- BÀI TOÁN 7: TÌM SỐ LỚN NHẤT VÀ NHỎ NHẤT TRONG DÃY SỐ ---

print("--- Tìm số lớn nhất và nhỏ nhất trong dãy số ---")

# 1. Khởi tạo một danh sách rỗng để lưu trữ các số.
day_so = []

# 2. Vòng lặp để nhập dữ liệu từ người dùng.
# 'while True' giúp chương trình liên tục hỏi nhập cho đến khi người dùng muốn dừng.
while True:
    # Yêu cầu người dùng nhập số, hoặc nhập 'n' để dừng.
    chuoi_nhap = input('Mời nhập số (hoặc nhập "n" để dừng lại): ')

    # Nếu người dùng nhập "n", thoát khỏi vòng lặp nhập liệu.
    if chuoi_nhap == "n":
        break

    # 3. Xử lý và chuyển đổi dữ liệu nhập vào, bắt lỗi nếu không phải số.
    try:
        # Chuyển đổi chuỗi nhập vào thành số thực (float).
        so = float(chuoi_nhap)
        # Thêm số hợp lệ vào danh sách.
        day_so.append(so)
    except ValueError:
        # Nếu không chuyển đổi được, thông báo lỗi.
        print("Đầu vào không hợp lệ. Vui lòng nhập một SỐ hoặc 'n' để dừng.")

# --- Sau khi đã thu thập xong dãy số ---

# 4. Kiểm tra trường hợp danh sách rỗng trước khi tìm min/max.
# Nếu danh sách không có số nào, sẽ không thể tìm được min/max.
if not day_so: # Cách kiểm tra list rỗng gọn gàng hơn là len(day_so) == 0
    print("\nKhông có số nào được nhập. Không thể tìm số lớn nhất và nhỏ nhất.")
else:
    # 5. Khởi tạo biến để lưu số lớn nhất và nhỏ nhất.
    # Ban đầu, gán cả hai bằng phần tử đầu tiên của danh sách.
    # Cách này đảm bảo rằng lon_nhat và nho_nhat luôn có giá trị hợp lệ từ list.
    lon_nhat = day_so[0]
    nho_nhat = day_so[0]
    
    # (Một cách khởi tạo khác, nếu không chắc chắn list không rỗng ngay lúc này, 
    # là dùng giá trị cực đại/cực tiểu của hệ thống:
    # lon_nhat = -sys.float_info.max # Số âm rất lớn
    # nho_nhat = sys.float_info.max  # Số dương rất lớn
    # Nhưng cách dùng day_so[0] thường trực quan hơn cho bài này.)


    # 6. Duyệt qua các số trong danh sách để tìm số lớn nhất và nhỏ nhất.
    # Trong mỗi lần lặp, so sánh số hiện tại với lon_nhat và nho_nhat đã lưu.
    for so_hien_tai in day_so:
        # So sánh để tìm số lớn nhất.
        if so_hien_tai > lon_nhat:
            lon_nhat = so_hien_tai
        
        # So sánh để tìm số nhỏ nhất.
        # Sử dụng 'if' độc lập thay vì 'elif' để đảm bảo cả hai điều kiện
        # đều được kiểm tra (mặc dù trong trường hợp này, kết quả vẫn đúng với elif).
        if so_hien_tai < nho_nhat:
            nho_nhat = so_hien_tai

    # 7. In ra kết quả cuối cùng.
    print(f"\nSố lớn nhất trong dãy là: {lon_nhat}")
    print(f"Số nhỏ nhất trong dãy là: {nho_nhat}")

# --- Gợi ý thêm: Cách ngắn gọn hơn với hàm có sẵn ---
# Python có các hàm tích hợp sẵn để tìm min và max một cách rất nhanh chóng:
# if day_so:
#     print(f"Số lớn nhất (dùng max()): {max(day_so)}")
#     print(f"Số nhỏ nhất (dùng min()): {min(day_so)}")

# --- BÀI TOÁN 8: QUẢN LÝ SẢN PHẨM ---