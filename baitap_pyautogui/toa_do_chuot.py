import pyautogui

# Di chuyển chuột thủ công đến vị trí bất kỳ, chờ 3 giây rồi lấy tọa độ
print("Di chuột tới điểm bất kỳ, chờ 3 giây...")
pyautogui.sleep(3)
print("Vị trí chuột hiện tại là:", pyautogui.position())
