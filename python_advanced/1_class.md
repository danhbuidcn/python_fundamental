# Class

- Một đối tượng có thể chứa 1 hoặc nhiều class
- Trong mỗi class chứa một hoặc nhiều thuộc tính và phương thức
  - Thuộc tính của class là các biến nằm trong phạm vi của class
  - Class có thể có hoặc không có phương thức. Phương thức của class phải khai báo trong phạm vi của class

```
class Person:
  # thuộc tính
  name = "Vũ Thanh Tài";
  age = 22;
  male = True
  # phương thức
  def setName(self, name):
    self.name = name
  
  def getName(self):
    return self.name
  
  def setAge(self, age):
    self.age = age
  
  def getAge(self):
    return self.age
  
  def setMale(self, male):
    self.male = male
  
  def getMale(self):
    return self.male

person = Person()
person.name
person.getMale()
```
