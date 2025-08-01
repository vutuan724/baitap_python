import pyautogui,time
import os
time.sleep(3)
pyautogui.moveTo(317,1059,duration = 1)  # Di chuyển tới biểu tượng trình duyệt, click mở
pyautogui.click()
time.sleep(3)                            # mở ra 1 bảng
pyautogui.moveTo(778,594,duration = 1)   # Di chuột tới nick cần mở (tọa độ bạn đã lấy)
pyautogui.click()                        # Click vào nick đó
time.sleep(2)                            # Chờ trang web mở ra
pyautogui.moveTo(175,62,duration = 1)    # đưa con chuột lên toạ độ thanh địa chỉ
time.sleep(2)                            # click cho con chuột nhấp nháy ở thanh địa chỉ đó
pyautogui.write("facebook.com", interval=0.05)  # Gõ địa chỉ
time.sleep(2)                                   # chờ 2 giây
pyautogui.press('enter')                         # Nhấn Enter để vào web
time.sleep(5)
pyautogui.moveTo(1088,262,duration = 1)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')

pyautogui.write("61552152903473", interval=0.05)
time.sleep(2)
pyautogui.moveTo(1085,324,duration = 1)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')

pyautogui.write("0988342379hoai", interval=0.05)
time.sleep(2)
pyautogui.press("enter")
time.sleep(5)
pyautogui.moveTo(293,19,duration = 1)
pyautogui.click()
time.sleep(3)

pyautogui.moveTo(175,62,duration = 1) 
pyautogui.click() 
pyautogui.write("2fa.live", interval=0.05)
pyautogui.press("enter")
time.sleep(2)

pyautogui.moveTo(518,219,duration = 1)
pyautogui.click()
pyautogui.write("PEKP BSVT V4MG ATKC MQBN ICYK 37AI KRBG", interval=0.05)
time.sleep(1)
pyautogui.moveTo(512,360,duration = 1)
pyautogui.click()
time.sleep(2)

pyautogui.moveTo(816,456,duration = 1)
pyautogui.mouseDown() 
pyautogui.moveTo(863,455,duration = 1)
pyautogui.mouseUp()
pyautogui.hotkey('ctrl', 'c')
time.sleep(3)
pyautogui.moveTo(161,19,duration = 1)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(693,600,duration = 1)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
time.sleep(5)

pyautogui.moveTo(952,681,duration = 1)
pyautogui.click()
time.slepp(5)