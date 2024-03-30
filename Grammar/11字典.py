# 字典(dict) key不可以重复 value可以重复 无索引 可以通过key找到对应的value 类似于json格式
my_dict={
    'a':100,
    'b':90,
    'c':80
}
print(my_dict['b']) # 90
# 字典的修改 若存在该key则只是修改其value的值 若key不存在则表示新增一个键值对
my_dict['a']=101
print(my_dict) # {'a': 101, 'b': 90, 'c': 80}
my_dict['d']=70
print(my_dict) # {'a': 101, 'b': 90, 'c': 80, 'd': 70}
value=my_dict.pop('a') # 删除一个键值对 返回其value
print(value) # 101
print(my_dict) # {'b': 90, 'c': 80, 'd': 70}
# keys()获取全部的key 以列表形式返回
keys=my_dict.keys()
print(keys) # dict_keys(['b', 'c', 'd'])
# 字典的遍历 方式1：获取到所有的key，在通过key找到其value
for key in keys:
    value=my_dict[key]
    print(f"字典中键为{key}的值为{value}")
print("--------------------------------------")
# 字典的遍历 方式2：直接进行遍历获取到的就是每一个key
for key in my_dict:
    value = my_dict[key]
    print(f"字典中键为{key}的值为{value}")
print("--------------------------------------")
# len()统计字典元素数量