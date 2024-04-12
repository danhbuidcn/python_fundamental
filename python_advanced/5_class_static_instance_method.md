# Class method

- Là phương thức được gắn với lớp không phải instance cụ thể
- Được đánh dấu bằng decorator `@classmethod`
- Tham số đầu tiên là `cls` thay vì `self` (trong instance method) để tham chiếu đến lớp chứa phương thức đó
- Có thể truy cập và thay đổi các class variable của lớp
- Sử dụng khi muốn thực hiện các thao tác liên quan đến toàn bộ lớp

# Static method

- Không phụ thuộc vào bất kì instance hoặc lớp nào, không có tham số đặc biệt
- Được đánh dấu bằng decorator `@staticmethod`
- Thực hiện một số công việc không phụ thuộc vào bất kì thông tin nào của lớp hoặc instance
- Static method không thể truy cập, thay đổi các class variable hoặc instance variable

# Instance method

- Là phương thức gắn với 1 instance cụ thể của 1 lớp
- Có thể truy vập và thao tác với instance variable thông qua từ khóa self

```
class MyClass:
  class_variable = "Hello";
  
  def __init__(self, value):
    self.instance_variable = value
  
  @classmethod
  def class_method(cls):
    print("Class method")
    print(cls.class_variable)  # Access class variable
  
  @staticmethod
  def static_method():
    print("Static method")
  
  def instance_method(self):
    print("This is an instance method")
    print("Instance variable:", self.instance_variable)

# Sử dụng class method
MyClass.class_method()

# Sử dụng static method
MyClass.static_method()

# Tạo một instance của lớp MyClass
obj = MyClass("Hello")
# Gọi instance method từ instance đã tạo
print(obj.instance_variable)
```
