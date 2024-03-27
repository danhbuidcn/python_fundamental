# Map

- Duyệt qua tất cả các phần từ của một hoặc nhiều list, dictionary

```
map(function, iterable1, iterable2 ,...)
- function là hàm xử lý logic qua mỗi lần lặp giá trị trong interable1, ......
- interable1, interable2 là các list, dict ,... các bạn cần lặp.
Hàm map sẽ trả về một map object chứa các kết quả sau khi thực thi.
```

VD:
```
result = map(lambda x, y: x + " " + y, ['red', 'blue'], ['green', 'black'])

print(list(result))  # ['red green', 'blue black']
```

# Fillter

- Duyệt qua tất cả các phần tử trong list, dictionary và trả về những giá trị đáp ứng điều kiện

```
filter(function, iterable)
- function là hàm xử lý logic qua mỗi lần lặp giá trị trong interable, ......
- interable là các list, dict ,... các bạn cần lặp.
Hàm filter sẽ trả về một map object chứa các kết quả sau khi thực thi.
```

VD:
```
result = filter(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 22])

print(list(result))  # [1, 3, 5, 7, 9]
# 3%2 dư 1 -> 1 được coi là true
```