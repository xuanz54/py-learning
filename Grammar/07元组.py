# 元组(tuple)内的元素不允许修改 元素类型任意
my_tuple=(1,True,"hello",1.1)
print(my_tuple)
print(type(my_tuple))
# 定义单个元素的元组 (元素,) 若不带’,‘ 则会被解释器识别为str类型
print(my_tuple[1]) # True
# 由于元组不可修改 其主要方法只有 len(元组) 元组.index() 元组.count()