# Abstract class

- Là class chứa 1 hoặc nhiều phương thức trìu tượng (được khai báo mà không được phép viết code thực thi)
- Không thể nào khởi tạo trực tiếp, mà chỉ có thể khởi tạo thông qua class con
- Class con của abstract class phải khai báo lại toàn bộ các phương thức trìu tượng của class cha

# Khai báo abstract class

- Abstract class được kế thừa từ Abstract Base Classes

```
from abc import ABC, abstractmethod

class PersonAbstact(ABC):
  name = None
  age = 0
  
  def getName(self):
    print(self.name)
  
  def getAge(self):
    print(self.age)
  
  @abstractmethod
  def getFull(self):
    pass

class Person(PersonAbstact):
  name = 'Vu Thanh Tai'
  age = 22
  
  def getFull(self):
    self.getName()
    self.getAge()

Person().getFull()
```
