# Khai báo biến

```
a = b = c = 1996
name, age, male = "Vũ Thanh Tài", 22 , True
```

# Các kiểu dữ liệu

- Khi khai báo biến thì kiểu dữ liệu sẽ tự động được detect (phát hiện)

```
name = "Vũ Thanh Tài"
#string

age = 22
#integer

point = 8.9
#float

var = True
#bool

option = [1,2,3,4,5]
#lists

tuple = ('Vũ Thanh Tài', 22 , True)
#Tuple

dictionary = {"name": "Vu Thanh Tai", "age": 22, "male": True}
#Dictionary
```

## Kiểm tra kiểu dữ liệu

type(data)

## Ép kiểu

- float(data) chuyển đổi sang kiểu số thực.
- int(data,base) chuyển đổi sang kiểu số, trong đó base là kiểu hệ số mà các bạn muốn chuyển đổi sang (tham số này có thể bỏ trống).
- str(data) chuyển đổi sang dạng chuỗi.
- complex(data) chuyển đổi sang kiểu phức hợp.
- tuple(data) chuyển đổi sang kiểu Tuple.
- dict(data) chuyển đổi sang kiểu Dictionary.
- hex(data) chuyển đổi sang hệ 16.
- oct(data) chuyển đổi sang hệ 8.
- chr(data) chuyển đổi sang dạng ký tự.

## Hàm print trong Python

- Hiển thị dữ liệu khi chương trình thực thi

# String

## Fomat chuỗi

| Cú pháp fomat | Mô tả                           |
|---------------|---------------------------------|
| %c            | character                       |
| %s            | chuỗi                           |
| %i            | số nguyên                       |
| %d            | số nguyên                       |
| %u            | số nguyên                       |
| %o            | bát phân                        |
| %x            | thập lục phân (in thường)      |
| %X            | thập lục phân (in hoa)          |
| %e            | số mũ  (với e thường)          |
| %E            | số mũ  (với e hoa)              |
| %f            | số thực                         |
| %g            | dạng rút gọn của %f and %e      |
| %G            | dạng rút gọn của %f and %E      |


VD:

```
guy = "Ban"
doamin = "toidicode.com"
full = "Chao mung %s den voi website %s" %(guy, doamin)
print(full)
```

## Truy cập tới từng nội dung của chuỗi

stringName[index]
stringName[start:end]

# Number

## Kiểu dữ liệu

int, float, complex

`del variable` # giải phóng vùng nhớ

- Python có một bộ thu gom rác (garbage collector) tích hợp, nhiệm vụ của nó là thu hồi bộ nhớ được sử dụng bởi các biến không còn được sử dụng nữa. 
- Mặc dù điều này giúp giảm thiểu vấn đề rò rỉ bộ nhớ, nhưng nó không đảm bảo rằng bộ nhớ sẽ không bao giờ đầy.

```
b = 10 + 24j
print(b + 20)
print(isinstance(b, complex))
```

## Các toán tử

| Toán tử | Mô tả                                    | Cú pháp | Ví dụ             |
|---------|------------------------------------------|---------|-------------------|
| +       | Thực hiện phép cộng cho các toán hạng.   | a + b   | 100+200=300       |
| -       | Thực hiện phép trừ cho các toán hạng.    | a - b   | 200-100=100       |
| *       | Thực hiện phép nhân 2 toán hạng.         | a * b   | 16*5=80           |
| /       | Thực hiện phép chia cho 2 toán hạng.     | a / b   | 8/5=1.6           |
| %       | Phép chia lấy phần dư.                   | a % b   | 8%5=3             |
| //      | Phép chia làm tròn dưới (chia nguyên).  | a // b  | 8//5=1            |
| **      | Số mũ.                                   | a**b    | 2**3=8            |

## Phép gán tắt

| Phép toán | Ví dụ     | Tương đương với |
|-----------|-----------|-----------------|
| =         | x = 5     | x = 5           |
| +=        | x += 5    | x = x + 5       |
| -=        | x -= 5    | x = x - 5       |
| *=        | x *= 5    | x = x * 5       |
| /=        | x /= 5    | x = x / 5       |
| %=        | x %= 5    | x = x % 5       |
| //=       | x //= 5   | x = x // 5      |
| **=       | x **= 5   | x = x ** 5      |

a,b = 3586, 952
print("Tổng của 3586 + 952 là: %i", a + b)
print("Hiệu của 3586 - 952 là: %i", a - b)
print("Tích của 3586 * 952 là: %i", a * b)
print("Thương của 3586 / 952 là: %i", a / b)
print("3586 chia 952 dư là: %i", a%b)

# List

- Bao gồm nhiều kiểu dữ liệu bên trong

```
name = ['Vu Thanh Tai', 'Nguyen Van A', 'Nguyen Thi E', 5,  [12, 5, 1996]]
name[1] = 1996
my_list.append(5) # add element into end list
my_list.insert(2, 5) # Insert into position second
del name[2]
```

# Tuple

- Là kiểu dữ liệu dùng để lưu trữ các đối tượng không thay đổi về sau

```
day1 = ('monday', 'tuesday', 'wednesday')
day2 = ('thursday', 'friday', 'saturday' , 'sunday', day1)
day = day1 + day2
print(day2[4][0])
```

# Dictionary

- Là kiểu dữ liệu lưu trữ key, value (giống với JSON)

```
person = {
  'name': 'Vũ Thanh Tài',
  'age': 22,
  'male': True,
  'status': 'single'        
  }

person['status'] # signle
person['status'] = 'married'
del person['status']
dictName.clear() # delete all element
```
