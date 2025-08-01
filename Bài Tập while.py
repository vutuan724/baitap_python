# Bài Tập while
n = int(input("Nhập số nguyên dương n: "))  # Nhập vào một số nguyên dương n
while n > 0:  # Lặp khi n còn lớn hơn 0
    if n % 2 == 0:  # Nếu n là số chẵn
        print(n)  # In ra số chẵn đó
    n -= 1  # Giảm n đi 1 sau mỗi lần lặp
# Bài tập này yêu cầu người dùng nhập một số nguyên dương n và in ra các số chẵn từ n về 1.
# Khi n là số chẵn, nó sẽ được in ra, sau đó n sẽ giảm đi 1 cho đến khi n không còn lớn hơn 0.
#Bài 2: In ra các số chẵn từ 1 đến n (dùng for)
#Nhập vào số nguyên dương n.
#In ra các số chẵn từ 1 đến n.
n = int(input("Nhập số  n: "))  # Nhập vào một số nguyên dương n
for i in range(n, 1 ,- 1):  # Lặp từ 1 đến n
    if i % 2 == 0:  # Nếu i là số chẵn
        print(i)  # In ra số chẵn đó
#Bai 3 tính tổng các từ 1 đến n (dùng while)
n = int(input("Nhập số nguyên dương n: "))  # Nhập vào một số nguyên dương n
tong = 0  # Khởi tạo biến tổng ban đầu là 0
i = 1  # Khởi tạo biến đếm i từ 1
while i <= n:  # Lặp từ 1 đến n
    tong += i  # Cộng dồn giá trị của i vào tổng
    i += 1  # Tăng i lên 1 sau mỗi lần lặp
print("Tổng từ 1 đến", n, "là:", tong)  # In ra tổng

# Bài 4: Tính tổng các số chẵn từ 1 đến n (dùng while)
tong = 0  # Khởi tạo biến tổng chẵn ban đầu là 0
i = 1
n = int(input("nhập vào n : "))
while i <= n:
    if i % 2 == 0:
        tong = tong + i
    i = i + 1
print(f"tổng là {tong}")

#Bài 4: Đếm có bao nhiêu số lẻ từ 1 đến n (dùng for)
# Bài 4: Đếm có bao nhiêu số lẻ từ 1 đến n (dùng for)

dem = 0 # Khởi tạo biến đếm số lẻ
n = int(input("Hãy nhập số: ")) # người dùng nhập số n để xác định số cuối trong vòng lặp
for i in range(1, n + 1): # các số được in ra từ 1 đến n là i
    if i % 2 != 0: #nếu i là số lẻ
        dem += 1 # tăng biến đếm lên 1
print(dem) # In ra số lượng số lẻ từ 1 đến n

