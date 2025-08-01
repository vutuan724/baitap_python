thong_tin = {}

ten = input("nhập tên của bạn : ")
tuoi =int(input("nhập tuổi của bạn :"))
email = input("nhập email của bạn : ")
noi_o = input("nhập thành phố của bạn : ")
thong_tin = {
"tên":ten,
"tuổi":tuoi,
"email":email,
"thành phố" :noi_o,
}
print(f'\nTên của bạn là:{thong_tin["tên"]},\
      \nTuổi của bạn là:{thong_tin["tuổi"]},\
      \nemail của bạn là: {thong_tin["email"]},\
      \nThành phố của bạn là:{thong_tin["thành phố"]}')
# sửa thông tin
cap_nhat = input("Bạn muốn sửa gì? (tên/tuổi/email/thành phố?): ")
if cap_nhat in thong_tin:
    if cap_nhat == "tên":
       ten_moi = input("nhập tên muốn sửa: ")
       thong_tin[cap_nhat]= ten_moi
    elif cap_nhat =="tuổi":        
        try:
            tuoi_moi = int(input("Nhập Tuổi muốn sửa: "))
            thong_tin[cap_nhat]= tuoi_moi
        except ValueError:
            print(" tuổi ko hợp lệ")
    elif cap_nhat == "email":
        email_moi = input("nhập email muốn sửa:")
        thong_tin[cap_nhat]= email_moi
    elif cap_nhat == "thành phố":
        noi_o_moi = input("nhập thành phố muốn sửa:")
        thong_tin[cap_nhat]= noi_o_moi
else:
    print("thông tin này ko trùng khớp :")
print(thong_tin)