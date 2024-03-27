# Hàm input

```
print("Hello guy!")
age = input("How old are you? ")
print("age: " + age)
```

# File IO

open(filePath, mode, buffer)
- filePath là đường dẫn đến địa chỉ của file.
- mode là thông số thiết lập chế độ chúng ta mở file được cấp những quyền gì? Mặc địn mode sẽ bằng r (xem các mode ở dưới).
- buffer là thông số đệm cho file mặc định thì nó sẽ là 0.

| Mode | Chú thích                                                     |
|------|---------------------------------------------------------------|
| r    | Chế độ chỉ được phép đọc.                                    |
| rb   | Chế độ chỉ được phép đọc nhưng cho định dạng nhị phân.       |
| r+   | Chế độ này cho phép đọc và ghi file, con trỏ nó sẽ nằm ở đầu file. |
| rb+  | Chế độ này cho phép đọc và ghi file ở dạng nhị phân, con trỏ sẽ nằm ở đầu file. |
| w    | Chế độ ghi file, nếu như file không tồn tại thì nó sẽ tạo mới file và ghi nội dung, còn nếu như file đã tồn tại nó sẽ ghi đè nội dung lên file cũ. |
| wb   | Tương tự chế độ w nhưng đối với nhị phân.                    |
| w+   | Mở file trong chế độ đọc và ghi. còn lại như w.              |
| wb+  | Giống chế độ w+ nhưng đối với nhị phân.                       |
| a    | Mở file trong chế độ ghi tiếp. Nếu file đã tồn tại rồi thì nó sẽ ghi tiếp nội dung, và nếu như file chưa tồn tại thì nó sẽ tạo một file mới và ghi nội dung vào đó. |
| ab   | Tương tự a nhưng đối với nhị phân.                            |
| a+   | Mở file trong chế độ đọc và ghi tiếp nội dung, còn lại cơ chế giống chế độ a. |
| ab+  | Tương tự chế độ a+ nhưng đối với nhị phân.                     |

```
# open file
file = open('readme.md')

# read file
data = file.read();

# close file
file.close()

# print data
print(data)
```

| Thuộc tính  | Chú thích                                                                                                  |
|-------------|------------------------------------------------------------------------------------------------------------|
| file.name   | Trả về tên của file đang được mở.                                                                          |
| file.mode   | Trả về chế độ mode của file đang được mở.                                                                  |
| file.closed | Trả về true nếu file đã được đóng, và false nếu file chưa đóng.                                           |
