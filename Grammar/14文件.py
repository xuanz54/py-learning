'''
r表示只读
w表示写入 会覆盖原内容
a表示追加 不会覆盖原内容
encoding参数由于并不是最后一个参数(文件对象还有很多参数)，所以只能用关键字传参

'''
file = open('D:/Python/test.txt', 'r', encoding='utf-8')
print(type(file)) # <class '_io.TextIOWrapper'>
# 程序中多次调用read系列方法 下一个read会从上一个read结尾接着读
print(file.read(1)) # read(要读取的字节数) 若不填则读取全部数据
result=file.readlines() #一行一行读取 返回一个列表对象 其中每个元素为file中的一行数据 而readline()只读一行
print(result)
file.close()
print("-----------------------------")
with open('D:/Python/test.txt','r',encoding='utf-8') as f : # 自动关闭文件
    for line in f :
        line=line.strip() # 去除后面的换行符
        print(line)
# write()写入数据到内存 flush()刷新内存数据到硬盘 close()内置flush()