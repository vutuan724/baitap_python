#Đề Bài:
#Viết một chương trình Python để:

#1: Hỏi người dùng nhập vào một chuỗi bất kỳ.
#2: Duyệt qua từng ký tự trong chuỗi đó.
#3: Đếm số lượng các loại ký tự sau:
   #-Chữ cái (bao gồm cả chữ in hoa và chữ thường, ví dụ: 'a', 'B', 'c').
   #-Chữ số (ví dụ: '0', '1', '9').
   #-Ký tự đặc biệt (tất cả những ký tự còn lại không phải chữ cái và không phải chữ số, ví dụ: '!', '@', '#', '$', ' ').
#4: In ra tổng số lượng của mỗi loại ký tự tìm được.
print("Bài Tập")
chuoi = input("hãy nhập vào 1 chuỗi : ")
chu_cai = 0
chu_so = 0
ky_tu = 0
for i in chuoi:
   if i.isalpha():
      chu_cai += 1
   elif i.isdigit():
      chu_so += 1
   else: 
      ky_tu += 1
print(chu_cai)
print(chu_so)
print(ky_tu)