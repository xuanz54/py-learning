# 字符串(str) 不支持修改
name="abcd"
# 索引
print(name[0]) #a
print(name[-1]) # d
print(name.index('b')) # 1
# 字符串修改(得到的是一个新的字符串，原字符串不变) 字符串a.replace(字符串b,字符串c) 把字符串a中的子串b替换为c
print(name.replace('bc','ad')) # aadd
# 将原字符串按制定分割的字符串进行分割，原字符串不变，返回一个列表对象  split(指定分割的字符)
# 去前后内容 strip()默认是去前后空格，换行符 strip(指定的字符)去前后该指定的字符
# count()统计字符个数 len(字符串) 统计字符串长度