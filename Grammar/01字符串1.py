# 字符串拼接使用 +
name1="a"
name2=2
print("我是"+name1)
# 字符串占位 %s表示以str格式占位 %d表示以int格式占位 %f表示以float格式占位
print("我是%s,%s" %(name1,name2))
# m.n%f 表示宽度为m，小数后n位置
print("%5.2f" %111) # 111.00
# 快速格式化 f"{}"
print(f"{name1},{name2}")
# 数据输入
result = input("输入一个数字：")
print(result)
