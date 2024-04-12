# Phương thức khởi tạo - constructor

- Constructor là phương thức được gọi mặc định khi khởi tạo class
- Được dùng để khởi tạo các thuộc tính, xử lý phương thức, nhận các tham số truyền vào

```
class Person:
    def __init__(self, name, age, male):
        print("Class person được khởi tạo!")
        print("Name: %s - Age: %d - Male: %d" %(name, age, male))

person = Person('Vu Thanh Tai', 22, True)
```


# Phương thức hủy - destructor

- Destructor được gọi khi hủy một class, luôn được thực thi cuối cùng khi khởi tạo 1 class
- Thường được dùng để giải phòng tài nguyên của clas

```
class Person:
    def __init__(self, name, age, male):
        print("Class person được khởi tạo!")
        self.name, self.age, self.male = name, age, male
    
    def getName(self):
        print("Name: %s" %(self.name))
    
    def getAge(self):
        print("Age: %d" %(self.age))
    
    def getMale(self):
        print("Male: %d" %(self.male))
    
    def __del__(self):
        print('Class Person được hủy')
        del self.name,self.age,self.male

person = Person('Vu Thanh Tai', 22, True)
person.getName()
person.getAge()
person.getMale()
# kết quả: 
# Class person được khởi tạo!
# Name: Vu Thanh Tai
# Age: 22
# Male: 1
# Class Person được hủy
```
