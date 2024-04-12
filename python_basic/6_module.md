# Module

- Chia nhỏ chương trình thành các nhánh nhỏ để dễ quản lý và gọi lại khi cần.
- Module có sẵn và custom module

```
import math # import toàn bộ module math vào không gian tên của chương trình

a = 3.2
# làm tròn lên 1 số
print(math.ceil(a)) # 4
# làm tròn xuống 1 số
print(math.floor(a)) # 3


from math import ceil # giảm bộ nhớ

a = 3.2
print(ceil(a)) 
# kết quả: 4
print(floor(a))
# Kết quả:  name 'floor' is not defined

from math import * # không import được các đối tượng có tên được bắt đầu bằng ký tự _
```

## Định danh cho modules

```
import modules as newname
# hoặc đối với from import
from modules import something as newname

from mathplus import _get_sum
print(_get_sum(5,7)) 
# kết quả: 12
```

- import module trong hệ thống

```
| modules/mathplus.py
| main.py

import os, sys
# lấy ra đường dẫn đến thư mục modules ở trong projetc hiện hành
lib_path = os.path.abspath(os.path.join('modules'))
# thêm thư mục cần load vào trong hệ thống
sys.path.append(lib_path)
# import
from mathplus import get_sum

print(get_sum(1,4));
# kết quả: 5
```