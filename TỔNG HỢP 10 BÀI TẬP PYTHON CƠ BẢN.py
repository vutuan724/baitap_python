# =====================================================================================
# TỔNG HỢP 10 BÀI TẬP PYTHON CƠ BẢN
# =====================================================================================

# --- BÀI TẬP 1: VIẾT HÀM CỘNG HAI SỐ ---
# Đề bài: Viết một hàm nhận vào hai số và trả về tổng của chúng.
def cong_hai_so(so1, so2):
    # Định nghĩa hàm có tên 'cong_hai_so' nhận vào hai tham số là 'so1' và 'so2'.
    ket_qua = so1 + so2
    # Khởi tạo biến 'ket_qua' và gán cho nó tổng của 'so1' và 'so2'.
    return ket_qua
    # Trả về giá trị của biến 'ket_qua' khi hàm được gọi.

                              # Ví dụ sử dụng Bài 1:
                              # tong_cua_hai_so = cong_hai_so(5, 3)
                              # print(f"Tổng của hai số là: {tong_cua_hai_so}") # Kết quả: 8


                              # --- BÀI TẬP 2: KIỂM TRA SỐ CHẴN/LẺ ---
                              # Đề bài: Viết một hàm kiểm tra xem một số có phải là số chẵn hay không. Hàm trả về True nếu là số chẵn, và False nếu là số lẻ.
def kiem_tra_so_chan_le(number):
    # Định nghĩa hàm 'kiem_tra_so_chan_le' nhận vào một tham số là 'number'.
    if number % 2 == 0:
        # Kiểm tra xem 'number' chia lấy dư cho 2 có bằng 0 hay không.
        # Nếu có (tức là số chẵn), thực hiện khối lệnh bên dưới.
        return True
        # Trả về giá trị Boolean True (đúng) vì đây là số chẵn.
    else:
        # Nếu điều kiện trên không đúng (tức là số lẻ), thực hiện khối lệnh này.
        return False
        # Trả về giá trị Boolean False (sai) vì đây là số lẻ.

# Ví dụ sử dụng Bài 2:
# la_so_chan = kiem_tra_so_chan_le(4)
# print(f"Số 4 là số chẵn: {la_so_chan}") # Kết quả: True
# la_so_le = kiem_tra_so_chan_le(7)
# print(f"Số 7 là số chẵn: {la_so_le}")   # Kết quả: False


# --- BÀI TẬP 3: TÍNH TỔNG CÁC SỐ TRONG DANH SÁCH ---
# Đề bài: Viết một hàm nhận vào một danh sách các số và trả về tổng của tất cả các số trong danh sách đó.
def tinh_tong_danh_sach(danh_sach_so):
    # Định nghĩa hàm 'tinh_tong_danh_sach' nhận vào một tham số là 'danh_sach_so' (một list).
    tong = 0
    # Khởi tạo biến 'tong' với giá trị ban đầu là 0. Biến này sẽ dùng để cộng dồn các số.
    for i in danh_sach_so:
        # Bắt đầu vòng lặp for để duyệt qua từng phần tử trong 'danh_sach_so'.
        # Mỗi phần tử sẽ được gán vào biến 'i' trong mỗi lần lặp.
        tong += i
        # Cộng giá trị của 'i' (phần tử hiện tại) vào biến 'tong'. (Viết tắt của: tong = tong + i)
    return tong
    # Sau khi vòng lặp kết thúc (đã duyệt hết tất cả các số), trả về giá trị cuối cùng của 'tong'.

# Ví dụ sử dụng Bài 3:
# my_numbers = [1, 2, 3, 4, 5]
# tong_cac_so = tinh_tong_danh_sach(my_numbers)
# print(f"Tổng các số trong danh sách là: {tong_cac_so}") # Kết quả: 15


# --- BÀI TẬP 4: ĐẾM KÝ TỰ TRONG CHUỖI ---
# Đề bài: Viết một hàm đếm xem một ký tự cụ thể xuất hiện bao nhiêu lần trong một chuỗi cho trước.
def dem_ky_tu(chuoi_can_kiem_tra, ky_tu_can_dem):
    # Định nghĩa hàm 'dem_ky_tu' nhận hai tham số: 'chuoi_can_kiem_tra' (chuỗi gốc) và 'ky_tu_can_dem' (ký tự muốn đếm).
    dem = 0
    # Khởi tạo biến 'dem' với giá trị ban đầu là 0. Biến này sẽ đếm số lần ký tự xuất hiện.
    for tu in chuoi_can_kiem_tra:
        # Duyệt qua từng ký tự trong 'chuoi_can_kiem_tra'. Mỗi ký tự sẽ được gán vào biến 'tu'.
        if tu == ky_tu_can_dem:
            # So sánh 'tu' (ký tự hiện tại) với 'ky_tu_can_dem'.
            # Nếu chúng giống nhau, điều kiện đúng.
            dem += 1
            # Tăng giá trị của biến 'dem' lên 1. (Viết tắt của: dem = dem + 1)
    return dem
    # Sau khi vòng lặp kết thúc, trả về tổng số lần ký tự xuất hiện.

# Ví dụ sử dụng Bài 4:
# my_string = "hello world"
# so_lan_l = dem_ky_tu(my_string, 'l')
# print(f"Ký tự 'l' xuất hiện {so_lan_l} lần trong '{my_string}'") # Kết quả: 3


# --- BÀI TẬP 5: TÌM SỐ LỚN NHẤT TRONG DANH SÁCH ---
# Đề bài: Viết một hàm tìm và trả về số lớn nhất có trong một danh sách các số.
def tim_so_lon_nhat(danh_sach_so):
    # Định nghĩa hàm 'tim_so_lon_nhat' nhận một tham số là 'danh_sach_so' (một list).
    lon_nhat = danh_sach_so[0]
    # Khởi tạo biến 'lon_nhat' bằng phần tử đầu tiên của 'danh_sach_so'.
    # Biến này sẽ lưu trữ số lớn nhất tìm được cho đến thời điểm hiện tại.
    for i in danh_sach_so:
        # Duyệt qua từng số trong 'danh_sach_so'. Mỗi số được gán vào biến 'i'.
        if i > lon_nhat:
            # So sánh 'i' (số hiện tại) với 'lon_nhat'.
            # Nếu 'i' lớn hơn 'lon_nhat', điều kiện đúng.
            lon_nhat = i
            # Cập nhật 'lon_nhat' bằng giá trị của 'i' vì 'i' là số lớn hơn.
    return lon_nhat
    # Sau khi duyệt hết danh sách, trả về giá trị cuối cùng của 'lon_nhat'.

# Ví dụ sử dụng Bài 5:
# my_numbers_for_max = [10, 3, 20, 5, 15]
# so_lon_nhat = tim_so_lon_nhat(my_numbers_for_max)
# print(f"Số lớn nhất trong danh sách là: {so_lon_nhat}") # Kết quả: 20


# --- BÀI TẬP 6: LOẠI BỎ CÁC PHẦN TỬ TRÙNG LẶP TRONG DANH SÁCH ---
# Đề bài: Viết một hàm nhận vào một danh sách các phần tử (có thể có trùng lặp) và trả về một danh sách mới chỉ chứa các phần tử DUY NHẤT.
def loai_bo_trung_lap(danh_sach_goc):
    # Định nghĩa hàm 'loai_bo_trung_lap' nhận một tham số là 'danh_sach_goc' (một list).
    danh_sach_moi = []
    # Khởi tạo một danh sách rỗng 'danh_sach_moi'. Đây là nơi sẽ chứa các phần tử duy nhất.
    for i in danh_sach_goc:
        # Duyệt qua từng phần tử trong 'danh_sach_goc'. Mỗi phần tử được gán vào biến 'i'.
        if i not in danh_sach_moi:
            # Kiểm tra xem 'i' (phần tử hiện tại) CÓ TRONG 'danh_sach_moi' hay KHÔNG.
            # Nếu 'i' CHƯA CÓ trong 'danh_sach_moi', điều kiện đúng.
            danh_sach_moi.append(i)
            # Thêm 'i' vào cuối 'danh_sach_moi' vì nó là một phần tử duy nhất mới tìm thấy.
    return danh_sach_moi
    # Sau khi duyệt hết 'danh_sach_goc', trả về 'danh_sach_moi' chứa các phần tử duy nhất.

# Ví dụ sử dụng Bài 6:
# list_co_trung_lap = ["apple", "banana", "apple", "orange", "banana"]
# list_duy_nhat = loai_bo_trung_lap(list_co_trung_lap)
# print(f"Danh sách sau khi loại bỏ trùng lặp: {list_duy_nhat}") # Kết quả: ['apple', 'banana', 'orange']


# --- BÀI TẬP 7: ĐẢO NGƯỢC CHUỖI ---
# Đề bài: Viết một hàm nhận vào một chuỗi và trả về một chuỗi mới đã được đảo ngược thứ tự các ký tự.
def dao_nguoc_chuoi(chao_hoi):
    # Định nghĩa hàm 'dao_nguoc_chuoi' nhận một tham số là 'chao_hoi' (một chuỗi).
    ten_moi = chao_hoi[::-1]
    # Sử dụng kỹ thuật slicing [::-1] để đảo ngược chuỗi 'chao_hoi' và gán kết quả vào 'ten_moi'.
    return ten_moi
    # Trả về chuỗi 'ten_moi' đã được đảo ngược.

# Ví dụ sử dụng Bài 7:
# original_string = "python"
# reversed_string = dao_nguoc_chuoi(original_string)
# print(f"Chuỗi đảo ngược của '{original_string}' là: {reversed_string}") # Kết quả: nohtyp


# --- BÀI TẬP 8: KIỂM TRA CHUỖI PALINDROME ---
# Đề bài: Viết một hàm kiểm tra xem một chuỗi có phải là chuỗi palindrome hay không (đọc xuôi hay đọc ngược đều giống nhau). Hàm trả về True nếu là palindrome, và False nếu không phải.
def kiem_tra_palindrome(chuoi_can_kiem_tra):
    # Định nghĩa hàm 'kiem_tra_palindrome' nhận một tham số là 'chuoi_can_kiem_tra' (một chuỗi).
    chuoi_dao_nguoc = chuoi_can_kiem_tra[::-1]
    # Đảo ngược chuỗi 'chuoi_can_kiem_tra' và lưu vào biến 'chuoi_dao_nguoc'.
    if chuoi_can_kiem_tra == chuoi_dao_nguoc:
        # So sánh chuỗi gốc ('chuoi_can_kiem_tra') với chuỗi đã đảo ngược ('chuoi_dao_nguoc').
        # Nếu chúng giống nhau, điều kiện đúng.
        return True
        # Trả về True vì đây là chuỗi palindrome.
    else:
        # Nếu hai chuỗi không giống nhau, điều kiện sai.
        return False
        # Trả về False vì đây không phải là chuỗi palindrome.

# Ví dụ sử dụng Bài 8:
# test_palindrome1 = "madam"
# print(f"'{test_palindrome1}' là palindrome: {kiem_tra_palindrome(test_palindrome1)}") # Kết quả: True
# test_palindrome2 = "hello"
# print(f"'{test_palindrome2}' là palindrome: {kiem_tra_palindrome(test_palindrome2)}") # Kết quả: False


# --- BÀI TẬP 9: XÓA NGUYÊN ÂM KHỎI CHUỖI ---
# Đề bài: Viết một hàm nhận vào một chuỗi và trả về một chuỗi mới mà đã loại bỏ tất cả các nguyên âm (a, e, i, o, u, A, E, I, O, U) khỏi chuỗi gốc.
def xoa_nguyen_am(chuoi_goc):
    # Định nghĩa hàm 'xoa_nguyen_am' nhận một tham số là 'chuoi_goc' (một chuỗi).
    chuoi_moi = []
    # Khởi tạo một danh sách rỗng 'chuoi_moi'. Đây là nơi sẽ chứa các ký tự không phải nguyên âm.
    nguyen_am = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U','ọ','y','ị'}
    # Định nghĩa một tập hợp (set) 'nguyen_am' chứa tất cả các nguyên âm cần loại bỏ.
    # Sử dụng set giúp việc kiểm tra 'in' hoặc 'not in' rất hiệu quả.
    for i in chuoi_goc:
        # Duyệt qua từng ký tự trong 'chuoi_goc'. Mỗi ký tự được gán vào biến 'i'.
        if not i in nguyen_am:
            # Kiểm tra xem 'i' (ký tự hiện tại) CÓ TRONG tập hợp 'nguyen_am' hay KHÔNG.
            # Nếu 'i' KHÔNG phải là nguyên âm, điều kiện đúng.
            chuoi_moi.append(i)
            # Thêm 'i' vào cuối danh sách 'chuoi_moi'.
    ko_nguyen_am = "".join(chuoi_moi)
    # Nối tất cả các ký tự trong danh sách 'chuoi_moi' lại với nhau để tạo thành một chuỗi hoàn chỉnh.
    # Kết quả được gán vào biến 'ko_nguyen_am'.
    return ko_nguyen_am
    # Trả về chuỗi 'ko_nguyen_am' không chứa nguyên âm.

# Ví dụ sử dụng Bài 9:
# original_text = "hoc py thon rat thu vi"
# text_no_vowels = xoa_nguyen_am(original_text)
# print(f"Chuỗi sau khi xóa nguyên âm: {text_no_vowels}") # Kết quả: hc py thn rt th v


# --- BÀI TẬP 10: LỌC SỐ CHẴN TỪ DANH SÁCH ---
# Đề bài: Viết một hàm nhận vào một danh sách các số (có thể là chuỗi số) và trả về một danh sách mới chỉ chứa các số chẵn từ danh sách gốc.
def loc_so_chan(danh_sach_so):
    # Định nghĩa hàm 'loc_so_chan' nhận một tham số là 'danh_sach_so' (một list, có thể chứa chuỗi số).
    danh_sach_moi = []
    # Khởi tạo một danh sách rỗng 'danh_sach_moi'. Đây là nơi sẽ chứa các số chẵn.
    for i in danh_sach_so:
        # Duyệt qua từng phần tử trong 'danh_sach_so'. Mỗi phần tử được gán vào biến 'i'.
        so_nguyen = int(i)
        # Chuyển đổi 'i' (là chuỗi) thành số nguyên và gán vào biến 'so_nguyen'.
        # Bước này quan trọng để có thể thực hiện phép toán số học.
        if so_nguyen % 2 == 0:
            # Kiểm tra xem 'so_nguyen' (số nguyên đã chuyển đổi) chia lấy dư cho 2 có bằng 0 hay không.
            # Nếu có (tức là số chẵn), điều kiện đúng.
            danh_sach_moi.append(so_nguyen)
            # Thêm 'so_nguyen' (là số nguyên) vào cuối 'danh_sach_moi'.
    return danh_sach_moi
    # Sau khi duyệt hết danh sách, trả về 'danh_sach_moi' chứa các số chẵn.

# Ví dụ sử dụng Bài 10:
# list_of_strings = ['1','2','6','5','8','0']
# even_numbers = loc_so_chan(list_of_strings)
# print(f"Các số chẵn trong danh sách là: {even_numbers}") # Kết quả: [2, 6, 8, 0]

# =====================================================================================
# HẾT TỔNG HỢP BÀI TẬP
# =====================================================================================