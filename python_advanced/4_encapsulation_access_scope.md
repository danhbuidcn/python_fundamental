# Phạm vi truy cập thuộc tính và phương thức

- 3 mức độ truy cập pucblic, protected, private (đại diện cho tính đóng gói của đối tượng)

## public

- Thuộc tính và phương thức có thể được truy cập từ bên trong class, bên ngoài class, từ class con
- Tên bắt đầu bằng chữ cái

```
class Foo:
  # Khai báo thuộc tính ở dạng public
  name = "Foo"
  # Khai báo phương thức ở dạng public
  def getName(self):
    # gọi thành phần trong class
    print(self.name)

# gọi thành phần ngoài class
print(Foo().name) # Foo
Foo().getName() # Foo

class Bar(Foo):
  pass

#test
Bar().getName() # Foo
```

## protected

- Thuộc tính và phương thức có thể được truy cập từ bên trong class, từ class con
- Trong python không tồn tại phạm vi này. Bản chất nó là public nhưng chúng ta quy chuẩn nó về protected
- Tên bắt đầu bằng _

```
class Foo:
  # Khai báo thuộc tính ở chuẩn protected
  _name = "Foo"
  # Khai báo phương thức ở chuẩn protected
  def _getName(self):
    # gọi thành phần trong class
    print(self._name)

# gọi thành phần ngoài class
print(Foo()._name) # Foo
Foo()._getName() # Foo

class Bar(Foo):
  pass

#test
Bar()._getName() # Foo
```

## private

- Thuộc tính và phương thức có thể được truy cập từ bên trong class
- Tên bắt đầu bằng __

```
class Foo:
  # Khai báo thuộc tính ở chuẩn private
  __name = "Foo"
  # Khai báo phương thức ở chuẩn private
  def __getName(self):
    # gọi thành phần trong class
    print(self.__name)
  # khai báo một phương thức ở dạng public để gọi thành phần private
  def get(self):
    self.__getName()

# gọi thành phần ngoài class
print(Foo().__name) # 'Foo' object has no attribute '__name'
Foo().__getName() # 'Foo' object has no attribute '__getName'
Foo().get() # Foo

class Bar(Foo):
  def getNameinFoo(self):
    self.__getName()

#test
Bar().getNameinFoo() # 'Bar' object has no attribute '_Bar__getName'
```
