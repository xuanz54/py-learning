# 用包来管理模块 包其实就是一个带有__init__.py的文件夹
# 导入包中的模块
# 多种导入方式
from my_package import module1
module1.test1() # 模块1的功能

from my_package.module2 import test
test() # 模块2的功能

from my_package.module1 import *


