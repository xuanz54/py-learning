# # while循环
i=1
while i<=100 :
    print("%d、次" % i)
    i+=1
# for循环 for 临时变量 in 待处理数据集
name="xuanz"
for x in name :
    print(x)
# # range(a):从0到a，不包括a
# # range(a,b):从a到b，不包括b
# # range(a,b,c):从a到b，不包括b，步长为c
for x in range(0,10):
    print(x)
#输出99乘法表
for x in range(1,10):
    for y in range(1,x+1):
        print(f"{y}*{x}={x*y}",end='  ')
    print()
'''
    怎么才能让 print() 函数不换行呢？
    解决方法：print() 函数有一个内置参数 end，使用 print() 时默认为 end=‘\n’。如果想要不换行显示，只要根据需要，把 end 设置为‘’（空字符）或‘ ’（空格符）即可。
'''
# continue结束本次循环 break跳出循环
