#📝 Bài tập nâng cao nhẹ:
#Viết chương trình duyệt chuỗi:
#"Python 3.12 có những chữ IN HOA và thường"
#và in ra:

#Tất cả chữ IN HOA trên cùng 1 dòng, cách nhau dấu -

#Tất cả chữ chữ thường trên cùng 1 dòng khác, cách nhau dấu .

#Gợi ý nhỏ:
#Dùng for duyệt từng ký tự

#Dùng if i.isupper() để lọc chữ in hoa

#Dùng if i.islower() để lọc chữ thường

#Bỏ qua khoảng trắng và ký tự không phải chữ cái (dùng isalpha())
chuoi = "Python 3.12 có những chữ IN HOA và thường"
chu_in_hoa = ""
chu_thuong = ""
for i in chuoi:
    if i.isalpha():
        if i.islower():
            if i != "":
              i = i + " . "
              chu_thuong = chu_thuong + i

print(chu_thuong)
