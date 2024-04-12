#  Regular Expression trong Python

- Đoạn kí tự để so sánh khớp các chuỗi

```
import re

str = 'Học lập trình Toidicode.com'
match = re.search(r'Toidicode.com', str)
if match: #nếu tồn tại chuỗi khớp                     
    print (match.group()) # in ra chuỗi đó
else:
    print ('Khong tim thay!') # Không thì hiện thông báo
#Kết quả:
#Toidicode.com
```

- group() : Phương thức này trả về các giá trị so khớp giữa biểu thức chính quy và chuỗi cần so
- groups() : Phương thức này sẽ trả về một tupel các chuỗi được so khớp khớp.
- search(pattern, string, flags) : Phương thức này thực hiện tìm kiếm chuỗi so khớp trên string và nó sẽ trả về các giá trị được so khớp.
- match(pattern, string, flags) : Phương thức này cũng thực hiện việc so khớp chuỗi nhưng nó sẽ tính từ phạm vi đầu chuỗi cho đến kết thúc, còn các tham số truyền vào thì tương tự như đối với phương thức search().
- fullmatch(pattern, string, flags) : Phương thức này cũng thực hiện việc so khớp nhưng nó là so khớp hoàn toàn, còn các tham số truyền vào là tương tự như phương thức match.
- split(pattern, string, maxsplit) : Hàm này có tác dụng so khớp và cắt chuỗi so khớp thành công.
- findall(partern, string, flags) : Phương thức này có tác dụng so khớp và trả về tất cả các chuỗi mà nó đã so khơp được, còn lại các tham số truyền và sử dụng như đối với phương thức search.
- sub(pattern, replace, string, flags) : Phương thức này có tác dụng so khớp và thay thế chuỗi so khớp được.

# Các cú pháp pattern trong Python.

- [] : Trong cặp dấu này chứa các ký tự có thể so khớp với văn bẳn
- Ký tự dấu . này tương đương với việc so khớp một chuỗi phải chứa ít nhất một ký tự.
- ^ : Ký tự này đại diện cho việc so khớp từ đầu của chuỗi.
- $ : Ký tự này đại diện cho việc so khớp đến cuối chuỗi.
- * : Ký tự này đại diện cho có thể có hoặc không có ký tự trước nó.
- + : Ký tự này đại diện cho có thể xuất hiện ít nhất hoặc nhiều ký tự trước nó.
- ? : Ký tự này đại diện cho chuỗi sẽ khớp với một trong các ký tự đằng trước nó.
- {m, n} : Ký tự này đại diện cho việc so khớp xem chuỗi đằng trước nó xuất hiện bao nhiêu tối thiểu m lần và tối đa n lần. Nếu bỏ trống n thì là so khớp sự xuất hiện m lần của chuỗi đằng trước nó.
- | : Ký tự này đại diện cho sự tồn tại của một trong 2 ký tự trước và sau nó.
- () : Ký tự này dùng để gom nhóm các pattern lại với nhau.
- \ : Ký tự này giúp phân biệt chuỗi sau nó không phải là ký tự đặc biệt.

| Pattern | Mô Tả                                            |
|---------|--------------------------------------------------|
| \A      | So khớp chuỗi là chuỗi.                         |
| \B      | So khớp nếu vị trí đặt \B không phải là đầu hoặc cuối chuỗi. |
| \d      | So khớp với số nguyên.                           |
| \D      | So khớp với các ký tự không phải là số.         |
| \s      | So khớp với khoảng trắng và các ký tự chữ.      |
| \S      | So khớp với các kỹ tự không phải là chữ.        |
| \w      | So khớp với chữ hoặc số.                         |
| \W      | So khớp với các ký tự không phải là chữ hoặc số.|

# Các flags trong Python

- I hoặc IGNORECASE - Không phân biệt hoa thường khi so khớp.
- L hoặc LOCALE - So Khớp với local hiện tại.
- M hoặc MULTILINE - Thay đổi $ và ^ thành kết thúc của một dòng và bắt đầu của một dòng thay vì mặc định là kết thúc chuỗi và bắt đầu chuỗi.
- A hoặc ACSII - Thay đổi \w, \W, \b, \B, \d, \D, \S và \s thành so khơp full unicode.
- S hoặc DOTALL -Thay đổi pattern . thành khớp với bất kỳ ký tự nào và dòng mới.
