import pyautogui,time

# Ví dụ: di chuyển chuột tới vị trí (100, 100) trên màn hình và click
pyautogui.moveTo(1870, 945, duration=1)  # duration=1 giây di chuyển từ từ tới đó
pyautogui.doubleClick()
#  (Bạn thay số 100, 100 thành tọa độ lấy ở bước 1 nhé.)muốn lấy vị trí chuột chỗ nào thì điền thông số chỗ đó
time.sleep(5)
pyautogui.moveTo(860, 655, duration=1)
pyautogui.Click()