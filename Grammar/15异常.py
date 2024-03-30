# 异常的捕获
name=1
try:  # 可以出现异常的代码
    print(1/0)
    print(name)
except (NameError,ZeroDivisionError) as e: # 捕获指定的异常: except 异常名 as 别名:
    print("发生了变量未定义或者除零的异常") # 发生异常后，处理异常的代码 NameError ZeroDivisionError 顶级异常Exception
    print(f"具体异常是:{e}")
else:
    print("没有发生异常执行的代码")
finally:
    print("无论是否有异常都会执行")