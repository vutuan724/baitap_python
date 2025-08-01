#🔔 Bắt đầu bài mới:
#🧠 Bài tập:
#Duyệt chuỗi "Học Python số 1 năm 2025!"
#→ In ra các chữ cái in hoa, trên một dòng, cách nhau bởi dấu -.
chuoi = "Học Python số 1 năm 2025!" # tạo chuỗi
chu_in_hoa = "" # tạo biến (đáp án) rỗng
for ky_tu in chuoi: # duyệt chuỗi kiểm tra tất cả các ký tự "ky_tu"
    if ky_tu.isupper():  # nếu ký tự là chữ in hoa
        if chu_in_hoa != "": # nếu đã có ký tự 
            chu_in_hoa = chu_in_hoa + "-" # sẽ cộng thêm dấu - trước ký tự
        chu_in_hoa = chu_in_hoa + ky_tu   # 👉 Gắn thêm ký tự ky_tu vào chuỗi chu_in_hoa hiện tại.
print(chu_in_hoa)  # in ra kết quả


#   🧩 🔹 CÔNG THỨC KHUNG: Lọc và nối ký tự có điều kiện, không dư dấu

#   chuoi = input("Nhập chuỗi: ")
#   ket_qua = ""  # Biến để nối kết quả

#   for ky_tu in chuoi:
#    if <điều kiện>:                # Nếu ký tự thỏa điều kiện cần giữ lại
#        if ket_qua != "":          # Nếu không phải ký tự đầu tiên
#            ket_qua += "<dấu_nối>" # Thêm dấu nối (ví dụ: dấu phẩy)
#        ket_qua += ky_tu           # Thêm ký tự vào kết quả

# print(ket_qua)
