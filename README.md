# Tiktok-scroller
#Using arduino uno and python to make a button that allows you to scroll tiktok and press like
#Bước 1: Chuẩn bị đồ nghề
Phần cứng: Arduino Uno, Module Joystick, Dây cắm (5 sợi cái-đực), Cáp USB nối Arduino với máy tính, và 1 cái breadboard nếu bạn muốn cắm nó vào.
Phần mềm: Arduino IDE, Visual Studio Code hoặc Python.

#Bước 2: Đấu dây cho module joytick ( phần này quan trọng nhé) 
Cắm dây từ Joystick vào Arduino Uno theo đúng bảng này:
Chân Joystick Cắm vào Arduino Uno
GND cắm vào GND
5V cắm vào 5V
VRx cắm vào A0
VRy cắm vào A1
SW cắm vào 3 (Lưu ý: cái này không nhất thiết phải là 3 có thể là bất kì chân pin nào bạn thích )
(Phần cắm này dù có cắm sai cũng không có ảnh hưởng gì đến mạch đâu thế nên cứ thoải mái bung lụa( chỉ là sẽ không chạy được thôi) 

# Bước 3: Nạp code cho Arduino 
Bước này để Arduino đọc chuyển động của tay cầm và gửi tín hiệu về máy tính.
Bạn tải file có tên là Arduino về nhé 
Mở Arduino IDE, mở file này ra, cắm dây và bấm nạp code( dấu hình mũi tên -> ) 

# Bước 4: Cài đặt file Python ( Bước này khá khó nếu như bạn chưa tiếp xúc nhiều với visual studio code) 
Bước này để máy tính hiểu tín hiệu từ Arduino và điều khiển chuột.
Mở Visual Studio Code( hoặc python tùy ý)
Tạo một Folder mới để chứa dự án, ví dụ tên là TikTok_Controller.
Bấm Ctrl + ~ (phím ngã) để mở Terminal bên dưới.
Gõ lệnh cài thư viện (Copy paste vào rồi Enter):
pip install pyserial pyautogui ( đoạn này nếu bị lỗi thì tra chatgpt cách cài 2 thư viện kia nhé) 

# Bước 5: Chạy
Nhớ tải file python về nhé( bây giờ file sẽ chạy được vì đã cài đủ thư viện) 
Bấm Run đợi 1 lúc nó sẽ hiện ra là kết nối với Arduino thành công 

# Thao tác:

Mở trình duyệt (Chrome/Edge/Cốc Cốc), vào TikTok.com.

Gạt cần lên: Lướt sang video mới.

Gạt cần xuống: Quay lại video cũ.

Gạt trái: Vào trang cá nhân chủ kênh.

Ấn núm xuống: Thả tim ❤️.



