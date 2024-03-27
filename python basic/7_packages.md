# Packages

- Là một thư mục chứa một hoặc nhiều modules hay các package khác nhau
- Mục đích: phân bổ module có cùng chức năng

```
|--demopackage/
|             |--modules.py
|             |--packagechild/
|                            |-- childmodule.py
|                            └── __init__py
|             └── __init__py
|--main.py

# __init__.py
print("Duoc in tu file __init__py")

# main.py
import demopackage
import demopackage.modules
from demopackage.modules import *
```





