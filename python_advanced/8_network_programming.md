# Lập trình mạng với module socket trong Python

- Socket là các endpoint của một kênh giao tiếp 2 chiều
- Sử dụng để kết nối với 1 chương trình khác chạy trên internet
- Một chương trình mạng có thể sử dụng nhiều socket cùng một lúc, nhờ đó nhiều chương trình có thể sử dụng internet cùng một lúc

- Socket thường được chia làm 2 loại
  + Stream socket: 
    - Dựa trên TCP
    - Việc truyền dữ liệu chỉ thực hiện giữa 2 quá trình đã thiết lập kết nối
    - Đảm bảo dữ liệu được truyền đến nơi nhận một cách đáng tin cậy, đúng thứ tự nhờ vào cơ chế quản lý luồng lưu thông trên mạng và cơ chế chống tắc nghẽn
  + Datgram socket: 
    - Dựa trên UDP
    - Truyền dữ liệu không yêu cầu có sự kết nối giữa 2 quá trình
    - Dữ liệu truyền không được tin cập, có thể không đúng trình tự và lặp lại, tốc độ nhanh

# Module socket

- Giúp thực hiện các kết nối client server

```
import socket
socket.socket(AddressFamily, socketType, Protocol)
```

- AddressFamily là cách chúng ta thiết lập địa chỉ kết nối. có 3 kiểu:
  + AF_INET kiểu này là thiết lập dưới dạng ipv4.
  + AF_INET6 kiểu này là thiết lập dưới dạng ipv6.
  + AF_UNIX
- SocketType là cách thiết lập giao thức cho socket. Thông thường thì sẽ là SOCK_STREAM (TCP) hoặc SOCK_DGRAM (UDP).
- Protocol tham số thiết lập loại giao thức, Tham số này có thể không cần thiết lập. Mặc định sẽ bằng 0.
Và dưới đây là một vài phương thức hay được sử dụng trong đối tượng socket.

| Phương thức        | Mô tả                                                                                           |
|--------------------|-------------------------------------------------------------------------------------------------|
| bind(address, port) | Phương thức này được dùng để lắng nghe đến địa chỉ `address` và `port`                        |
| listen(backlog)    | Phương thức này thiết lập mở kết nối trên server, với tham số truyền vào là số kết nối được phép (nhỏ nhất là 0 và lớn nhất là do cấu hình của server). |
| accept()           | Phương thức này thiết lập chấp nhận một kết nối, và nó sẽ trả về một tuple gồm 2 thông số (`conn`, `address`) để chúng ta có thể gửi ngược về client. |
| connect(address)   | Phương thức này thiết lập một kết nối từ client đến server.                                     |
| recv(bufsize, flag) | Phương thức này dùng để nhận dữ liệu qua giao thức TCP.                                          |
| send(byte, flag)   | Phương thức này gửi dữ liệu thông qua giao thức TCP.                                             |
| recvfrom(bufsize, flag) | Phương thức này dùng để nhận dữ liệu qua giao thức UCP.                                          |
| sendto(bytes, address) | Phương thức này dùng để gửi dữ liệu qua giao thức UCP.                                          |
| close()            | Phương thức này dùng để đóng một kết nối.                                                        |

## Example

#server.py

```
import socket

HOST = 'localhost' # Thiết lập địa chỉ address
PORT = 8000 # Thiết lập post lắng nghe
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cấu hình kết nối
s.bind((HOST, PORT)) # lắng nghe
s.listen(1) # thiết lập tối ta 1 kết nối đồng thời
conn, addr = s.accept() # chấp nhận kết nối và trả về thông số
with conn:
    try:
        # in ra thông địa chỉ của client
        print('Connected by', addr)
        while True:
            # Đọc nội dung client gửi đến
            data = conn.recv(1024)
            # In ra Nội dung 
            print(data)
            # Và gửi nội dung về máy khách
            conn.sendall(b'Hello client')
            if not data: # nếu không còn data thì dừng đọc
                break
    finally:
        s.close() # đóng socket
```

#client.py

```
import socket

HOST = 'localhost'    # Cấu hình address server
PORT = 8000              # Cấu hình Port sử dụng
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cấu hình socket
s.connect((HOST, PORT)) # tiến hành kết nối đến server
s.sendall(b'Hello server!') # Gửi dữ liệu lên server 
data = s.recv(1024) # Đọc dữ liệu server trả về
print('Server Respone: ', repr(data))
```