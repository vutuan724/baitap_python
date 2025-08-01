#📝 Bài tập nâng cao nhẹ:
#Viết chương trình duyệt chuỗi:
#"Python 3.12 có những chữ IN HOA và thường"
#và in ra:

#t cả chữ IN HOA trên cùng 1 dòng, cách nhau dấu -

#Tất cả chữ chữ thường trên cùng 1 dòng khác, cách nhau dấu .

#Gợi ý nhỏ:
#Dùng for duyệt từng ký tự

#Dùng if i.isupper() để lọc chữ in hoa

#Dùng if i.islower() để lọc chữ thường

#ỏ qua khoảng trắng và ký tự không phải chữ cái (dùng isalpha())
s = "Python 3.12 có những chữ IN HOA và thường"
upper_case = [] 
lower_case = []
for i in s:
    if i.isupper() and i.isalpha():
        upper_case.append(i)
    elif i.islower() and i.isalpha():
        lower_case.append(i)
print("-".join(upper_case))
print(".".join(lower_case))
pin