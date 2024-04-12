# Phân biệt thủ tục proceduce và function mysql

Trong MySQL, có hai loại đối tượng được sử dụng để lưu trữ các khối mã SQL: Stored Procedures và Functions.

## Stored Procedures:

### Phạm vi sử dụng:

- Stored Procedures có thể chứa một loạt các câu lệnh SQL
- Có thể thực hiện nhiều thao tác như INSERT, UPDATE, DELETE, SELECT và nhiều hơn nữa.
- Có thể chứa các điều kiện, vòng lặp, và các câu lệnh điều khiển luồng khác.

### Trả về giá trị:

- Stored Procedures không nhất thiết phải trả về một giá trị. 
- Nếu chúng trả về giá trị, nó có thể là một giá trị INT, STRING, TABLE, hoặc một kết hợp của chúng.

### Sử dụng:

Được sử dụng khi bạn muốn thực hiện một loạt các thao tác và lưu trữ chúng để tái sử dụng.


## Functions:

### Phạm vi sử dụng:

- Functions chủ yếu được sử dụng để trả về một giá trị. 
- Chúng không thể thực hiện các câu lệnh như INSERT, UPDATE, DELETE.
- Chúng không có thể chứa các câu lệnh như SELECT, INSERT, UPDATE, hoặc DELETE, trừ khi trong các câu lệnh SELECT INTO.

### Trả về giá trị:

Functions phải trả về một giá trị.

### Sử dụng:

Được sử dụng khi bạn chỉ muốn thực hiện một phép tính nào đó và nhận kết quả trả về.

# Ví dụ:

Stored Procedure:
```sql
CREATE PROCEDURE GetAllUsers()
BEGIN
    SELECT * FROM users;
END
```

Function:
```sql
CREATE FUNCTION CalculateAveragePrice()
RETURNS DECIMAL(10,2)
BEGIN
    DECLARE avg_price DECIMAL(10,2);
    SELECT AVG(price) INTO avg_price FROM products;
    RETURN avg_price;
END
```
