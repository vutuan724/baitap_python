# Khởi tạo một danh sách rỗng để lưu trữ các mặt hàng
loai_hang = []

# --- PHA 1: NHẬP LIỆU SẢN PHẨM ---
# Vòng lặp vô hạn để liên tục hỏi người dùng nhập thông tin sản phẩm
while True:
    # Yêu cầu người dùng nhập tên sản phẩm. Nếu nhập 'n' (hoặc 'N'), thoát khỏi vòng lặp này.
    ten = input("Mời nhập tên sản phẩm (nhấn 'n' để dừng): ")
    if ten.lower() == "n":
        break # Thoát khỏi vòng lặp nhập liệu khi người dùng không muốn nhập nữa

    # Kiểm tra tính hợp lệ của tên: không được rỗng hoặc chỉ chứa ký tự không phải chữ/số
    if not ten.replace(" ", "").isalnum() or ten.strip() == "":
        print("Tên không hợp lệ, vui lòng nhập lại!")
        continue # Quay lại đầu vòng lặp while True để nhập lại tên

    # Chuẩn hóa tên: loại bỏ khoảng trắng thừa, viết hoa chữ cái đầu mỗi từ
    ten = ten.strip() # Xóa khoảng trắng ở đầu và cuối chuỗi
    ten_chuan = ten.split() # Tách chuỗi thành danh sách các từ
    ten = " ".join(ten_chuan) # Nối lại các từ bằng một khoảng trắng duy nhất
    ten = ten.title() # Viết hoa chữ cái đầu của mỗi từ (ví dụ: "ao thun" thành "Ao Thun")

    # Vòng lặp để đảm bảo nhập giá hợp lệ
    while True:
        try:
            gia = input("Mời nhập giá: ")
            gia = float(gia) # Chuyển đổi giá trị nhập vào thành số thực
            if gia <= 0:
                print("Giá phải lớn hơn 0, vui lòng nhập lại.")
                continue # Quay lại đầu vòng lặp while True để nhập lại giá
            break # Thoát khỏi vòng lặp nhập giá khi giá hợp lệ
        except ValueError: # Bắt lỗi nếu người dùng nhập không phải là số
            print("Vui lòng nhập một số hợp lệ cho giá.")
            continue # Quay lại đầu vòng lặp while True để nhập lại giá

    # Vòng lặp để đảm bảo nhập số lượng hợp lệ
    while True:
        try:
            so_luong = input("Mời nhập số lượng: ")
            so_luong = float(so_luong) # Chuyển đổi giá trị nhập vào thành số thực
            if so_luong <= 0:
                print("Số lượng phải lớn hơn 0, vui lòng nhập lại.")
                continue # Quay lại đầu vòng lặp while True để nhập lại số lượng
            break # Thoát khỏi vòng lặp nhập số lượng khi số lượng hợp lệ
        except ValueError: # Bắt lỗi nếu người dùng nhập không phải là số
            print("Vui lòng nhập một số hợp lệ cho số lượng.")
            continue # Quay lại đầu vòng lặp while True để nhập lại số lượng

    # Tạo một dictionary để lưu thông tin mặt hàng vừa nhập
    mat_hang = {
        "tên": ten,
        "giá": gia,
        "số lượng": so_luong,
    }
    # Thêm dictionary mặt hàng vào danh sách loai_hang
    loai_hang.append(mat_hang)

"""

## Tính Tổng Giá Trị của Một Mặt Hàng Cụ Thể

```python"""
# --- PHA 2: TÌM KIẾM VÀ TÍNH TỔNG THEO TÊN MẶT HÀNG ---
# Vòng lặp ngoài để cho phép người dùng liên tục tìm kiếm và tính tổng các mặt hàng khác nhau
while True:
    tong_ao = 0 # Khởi tạo tổng bằng 0 cho MỖI LẦN TÌM KIẾM MỚI

    # Yêu cầu người dùng nhập tên sản phẩm muốn tính tổng
    lua_chon_tim_kiem = input("Nhập sản phẩm muốn tính tổng: ")
    # Chuẩn hóa tên nhập vào (giống như khi nhập liệu) để so sánh chính xác
    lua_chon_tim_kiem = lua_chon_tim_kiem.strip()
    lua_chon_tim_kiem = " ".join(lua_chon_tim_kiem.split())
    lua_chon_tim_kiem = lua_chon_tim_kiem.title()

                                                                                        # Vòng lặp để duyệt qua từng mặt hàng trong danh sách loai_hang
    for mat_hang in loai_hang:
                                                                                        # Nếu tên mặt hàng khớp với lựa chọn của người dùng
        if mat_hang["tên"] == lua_chon_tim_kiem:
                                                                                        # Cộng dồn giá trị của mặt hàng hiện tại vào tong_ao
            tong_ao += mat_hang["giá"] * mat_hang["số lượng"]

                                                                                        # Sau khi vòng lặp 'for' kết thúc (đã duyệt qua HẾT danh sách)
    if tong_ao > 0:                                                                     # Nếu tong_ao lớn hơn 0, nghĩa là đã tìm thấy mặt hàng và tính được tổng
        print(f"Tổng giá trị của mặt hàng '{lua_chon_tim_kiem}' là: {tong_ao} VND")     # Hỏi người dùng có muốn tiếp tục tìm kiếm mặt hàng khác không
        
        cau_tra_loi_tiep_tuc = input("Bạn có muốn tính tiếp không? (y/n): ").lower()
        if cau_tra_loi_tiep_tuc == "n":
            break                                                                        # Nếu người dùng nhập 'n', thoát khỏi vòng lặp 'while True' bên ngoài
    else:                                                                                # Nếu tong_ao vẫn bằng 0, nghĩa là không tìm thấy mặt hàng nào khớp
        print(f"Không tìm thấy mặt hàng '{lua_chon_tim_kiem}'. \
              Vui lòng nhập chính xác tên mặt hàng.")
                                                                                         # Dùng 'continue' để bỏ qua phần còn lại của lần lặp 'while True' hiện tại
                                                                                         # và quay lại đầu vòng lặp để hỏi tên sản phẩm mới ngay lập tức
        continue

"""

## Tính Tổng Số Lượng Các Mặt Hàng

```python"""
                                                                                          # --- PHA 3: TÍNH TỔNG SỐ LƯỢNG CỦA TẤT CẢ CÁC MẶT HÀNG ---
tong_so_luong_tat_ca = 0                                                                  # Khởi tạo biến tổng số lượng của tất cả mặt hàng

                                                                                           # Duyệt qua từng mặt hàng trong danh sách loai_hang
for mat_hang in loai_hang:
                                                                                           # Cộng dồn số lượng của mỗi mặt hàng vào tong_so_luong_tat_ca
    tong_so_luong_tat_ca = tong_so_luong_tat_ca + mat_hang["số lượng"]

                                                                                            # In ra tổng số lượng của tất cả các mặt hàng
print(f"\nTổng số lượng của tất cả mặt hàng là: {int(tong_so_luong_tat_ca)} sản phẩm.")
                                                                                            # Sử dụng int() để hiển thị số lượng dưới dạng số nguyên,
                                                                                            #  nhìn đẹp hơn nếu số lượng là số nguyên.

                                                                                            # --- PHA 4: HIỂN THỊ DANH SÁCH CÁC MẶT HÀNG ---
print("\n--- DANH SÁCH CÁC MẶT HÀNG ĐÃ NHẬP ---")
if not loai_hang:                                                                           # Kiểm tra nếu danh sách rỗng
    print("Chưa có mặt hàng nào trong danh sách.")
else:
    # Duyệt qua từng mặt hàng trong danh sách loai_hang để in thông tin chi tiết
    for i, mat_hang in enumerate(loai_hang): # Dùng enumerate để có số thứ tự
        # In thông tin của từng mặt hàng một cách có định dạng, dễ đọc
        print(f"{i+1}. Tên hàng: {mat_hang['tên']}, Giá: {mat_hang['giá']:.0f} VND, Số lượng: {mat_hang['số lượng']:.0f} sản phẩm")
        # Dùng :.0f để in số thực không có phần thập phân nếu nó là số nguyên (ví dụ: 4.0 in thành 4)