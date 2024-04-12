# Tính đa hình

- Một phương thức có thể có các hành vi khác nhau tùy thuộc vào đối tượng được gọi
- Được thể hiện qua việc ghi đè phương thức (method overriding) và ghi đè thuộc tính (attribute overriding)

```
class Animal:
  def sound(self):
    print("Animal makes a sound")

class Dog(Animal):
  def sound(self):
    print("Dog barks")

class Cat(Animal):
  def sound(self):
    print("Cat meows")

# Tạo các đối tượng và gọi phương thức sound()
animal = Animal()
animal.sound()  # Output: "Animal makes a sound"

dog = Dog()
dog.sound()  # Output: "Dog barks"

cat = Cat()
cat.sound()  # Output: "Cat meows"
```
