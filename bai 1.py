#📝 Bài tập nâng cao nhẹ:
#Viết chương trình duyệt chuỗi:
#"Python 3.12 có những chữ IN HOA và thường"
#và in ra:

#Tất cả chữ IN HOA trên cùng 1 dòng, cách nhau dấu -

#Tất cả chữ chữ thường trên cùng 1 dòng khác, cách nhau dấu .
chuoi = "Python 3.12 có những chữ IN HOA và thường" #  tạo chuỗi
chu_thuong = "" # tạo biến rỗng
chu_in_hoa = "" # tạo biến rỗng
for ky_tu in chuoi: # duyệt chuỗi
    if ky_tu.isalpha(): # nếu ký tự là chữ cái
        if ky_tu.islower(): # nếu ký tự là chữ thường
            ky_tu += "."

            
    
print(chu_thuong)
print(chu_in_hoa)

