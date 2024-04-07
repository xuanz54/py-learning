# 函数的多返回值 返回值的数量和类型不受限
def test():
    return 'a',1

result1,result2 = test()
print(f"返回值1是{result1},返回值2是{result2}") # 返回值1是a,返回值2是1

# 函数传参方式 1.位置参数：即一一对应 2.关键字参数：用键=值形式传参 消除了传参时的参数顺序要求
# 若两种参数均包含,则在进行函数设计和函数传参时均需要位置参数在关键字参数之前
def test2(name,age=20): # 设置年龄默认值为20 默认值必须在最后
    print(f"姓名是{name},年龄是{age}")

# 位置参数的不定长参数 参数默认封装到元组中去
def test3(*args):
    print(args)
    print(type(args))
test3('a',1,True) # ('a', 1, True) <class 'tuple'>

# 关键字参数的不定长参数 参数默认封装到字典中去
def test4(**kwargs):
    print(kwargs)
    print(type(kwargs))
test4(name="xuanz",age=20) # {'name': 'xuanz', 'age': 20} <class 'dict'>

# 匿名函数 将函数作为参数 参数确定 但是执行逻辑不确定
def computer(get_result):
    get_result(1,2)
def add(x,y):
    print(f"{x}+{y}的结果是{x+y}")
def subtract(x,y):
    print(f"{x}-{y}的结果是{x-y}")
computer(add) # 1+2的结果是3
computer(subtract) # 1-2的结果是-1

'''
lambda匿名函数 定义一个无名称的函数(只需要使用一次该函数时使用)
语法: lambda 传入参数: 函数体(一行代码)
lambda是关键字用来定义匿名函数
'''
computer(lambda x,y:print(f"{x}+{y}的结果是{x+y}")) # 若’：‘后直接写x+y 即代表返回x+y
