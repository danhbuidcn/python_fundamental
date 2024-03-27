# Hàm

- Hàm là một tập các khối code.

```
def sum(a, b=2):
  print("sum = " + str(a + b))
sum(1)
```

# Phạm vi của biến

- Biến cục bộ (Local Scope) được khai báo trong hàm thì có phạm vi trong hàm. biến là list thì có thể tác động ra ngoài hàm

```
a = [5, 10, 15]
def change():
  a[0] = 1000
  print(a)

change()
print(a)
# KQ: [1000, 10, 15]
```

- Biến toàn cầu (Global Scope) có thể gọi và tác động từ bất kì đâu trong chương trình

```
a = "Hello Guy!"
def say():
    global a
    a = "Toidicode.com"
    print(a)

say()
# KQ: Toidicode.com
print(a)
# KQ: Toidicode.com
```

- Biến không cục bộ (Nonlocal Scope) trong các hàm lồng nhau, biến có thể được xác định ở mức giữa phạm vi cục bộ và toàn cục

```
def myfunc1():
  x = "John"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2() 
  return x

print(myfunc1())
```
