import serial
import pyautogui
import time

# --- CẤU HÌNH ---
# Sửa 'COM3' thành cổng COM bạn vừa tìm thấy ở bước 2
# Ví dụ: 'COM4', 'COM5'...
cong_com = 'COM3' 
toc_do = 9600



print("Dang ket noi voi Arduino...")

try:
    ser = serial.Serial(cong_com, toc_do)
    time.sleep(2) # Đợi 2 giây cho Arduino khởi động
    print("DA KET NOI THANH CONG! MO TIKTOK LEN VA QUAY TAY!")
except Exception as e:
    print("Loi roi: Khong tim thay cong COM. Kiem tra lai day cam hoac so COM.")
    print("Chi tiet loi:", e)
    exit()

while True:
    try:
        if ser.in_waiting > 0:
            # Đọc tín hiệu từ Arduino
            data = ser.readline().decode('utf-8').strip()
            
            # --- XỬ LÝ TÍN HIỆU ---
            if data == "UP":
                # Gạt cần lên -> Lướt xuống video dưới
                pyautogui.press('down')
                print("Lướt Next Video")
                
            elif data == "DOWN":
                # Gạt cần xuống -> Lướt về video cũ
                pyautogui.press('up')
                print("Lướt Back Video")
                
            elif data == "LEFT":
                # Gạt trái -> Vào trang (Mô phỏng phím Enter)
                pyautogui.press('enter')
                print("Vào trang/Chi tiết")
                
            elif data == "CLICK":
                # Ấn nút -> Tim (Click đúp chuột)
                pyautogui.doubleClick() 
                print("Đã Tim <3")
                
    except Exception as e:
        print("Loi ngat ket noi:", e)
        break