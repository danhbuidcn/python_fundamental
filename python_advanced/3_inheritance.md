# Kế thừa

- Một class con kế thừa từ class cha thì class con có thể sử dụng toàn bộ thuộc tính và phương thức được cho phép trong class cha

```
class Person:
  def __init__(self, name, age):
    self.name, self.age = name, age
  
  def getName(self):
    print("Name: %s" %(self.name))
  
  def getAge(self):
    print("Age: %d" %(self.age))
  
  def getSex(self):
    print("Sex: %s" %(self.sex))

class Male(Person):
  sex = "Male"

class Male(Person):
  sex = "Female"

a=Male('Mike', 24)
a.getAge()
```

## Ghi đè

```
class Foo:
    name = 'Foo'
    def getName(self):
        print("Class: Foo")
class Bar(Foo):
    name = 'Bar'
    def getName(self):
        print("Class: Bar")

print(Foo().name)
Foo().getName()
print(Bar().name)
Bar().getName()

# Ket qua:
# Foo
# Class: Foo
#
# Bar
# Class: Bar
```

## Super()

- Được dùng để gọi đến thành phần trong clas cha

```
class Foo:
  name = 'Foo'
  def getName(self):
    print("Class: Foo")

class Bar(Foo):
  name = 'Bar'
  def getName(self):
    print("Atribute name = " + super().name)
    super().getName()

Bar().getName()
# Ket qua:
# Atribute name = Foo
# Class: Foo
```

## Đa kế thừa

- Python hỗ trợ đa kế thừa
- Sử dụng super() thì sẽ gọi đến thành phần trong clas kế thừa được truyền vào đầu tiên

```
class First:
  def getClass(self):
    print("Class Fist")
    # super().getClass() : nếu muốn gọi đến Second

class Second:
  def getClass(self):
    print("Class Second")
        
class Third(First, Second):
  def getClass(self):
    super().getClass()

third = Third()
third.getClass()

# Kết Quả:
# Class Fist
```

