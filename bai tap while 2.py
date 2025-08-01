#Bài 5: Tính giai thừa của một số nguyên dương n (dùng while)

#Nhập vào số nguyên dương n.
#Tính và in ra n! (giai thừa của n).
#Bài 6: In ra bảng cửu chương của một số n (dùng for)

#Nhập vào số nguyên dương n.
#In ra bảng cửu chương của n từ 1 đến 10.
#Bài 7: Đếm số lượng chữ số của một số nguyên dương n (dùng while)

#Nhập vào số nguyên dương n.
#Đếm và in ra số lượng chữ số của n.
#Bài 8: Tính tổng các chữ số của một số nguyên dương n (dùng while)

#Nhập vào số nguyên dương n.
#Tính và in ra tổng các chữ số của n.

print("Bài 5: Tính giai thừa của một số nguyên dương n (dùng while)")
n = int(input("Nhập vào số nguyên dương n: "))  
giai_thua = 1 # khởi tạo biến giai thừa,khi n = 0 thì giai thừa = 1
i = 1 # biến đếm bắt đầu từ i = 1
while i <= n: # chừng nào i nhỏ hơn hoặc bằng n thì lặp
    giai_thua *= i  # nhân giai thừa với i
    i += 1
    #print("có thể in ra kết quả ở đây để kiểm tra số lần lặp của n")
print("Giai thừa của", n, "là", giai_thua)
# Bài 6: In ra bảng cửu chương của một số n (dùng for)
print("Bài 6: In ra bảng cửu chương của một số n (dùng for)")
n = int(input("Nhập vào số nguyên dương n: "))
for i in range(1, 11):
  print(n, "x", i, "=", n * i)
# bài 7:Đếm số lượng chữ số của một số nguyên dương n (dùng while)
n = int(input("nhập vào số nguyên dương n : "))
dem = 0
while n > 0:
    n //= 10
    dem += 1
print("Số lượng chữ số của n là:", dem)