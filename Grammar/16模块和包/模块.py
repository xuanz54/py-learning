# 模块就是一个Python文件 里面有函数 变量 类等 我们可以导入模块并直接使用
# 语法： from[模块名] import[模块/类/变量/函数/*] [as 别名]
import time,random # 导入内置模块
time.sleep(2)

print('TEST')
from time import sleep as s
s(1)
print("aaaaaaa")  # import 模块 和 from 模块 import * 的区别是:前者需要使用“模块名.” ， 后者可以直接使用

# 自定义模块
from my_module import add

print(add(1, 1))
# main
if __name__ == '__main__': # 内置变量name 运行时name的值为main
    print()