# 列表(list)中的元素可以是任意类型的
name_list=['python',111,6.6,True]
print(name_list)
print(type(name_list))
# 取出列表中的每个元素：1、从前往后：从0开始每次+1      2、从后往前：从-1开始每次-1
print(name_list[0]) # python
print(name_list[1]) # 111
print(name_list[-1]) # True
print(name_list[-2]) # 6.6

# 列表的操作
my_list=[1,2,3,4]

# 1.获取指定元素的下标 列表.index(元素) 如果查找的元素不存在会报错
print(my_list.index(1)) # 0
# 2.修改指定下标为x的元素的值为y: 列表[x]=y
# 3.在指定下标处插入指定元素:  列表.insert(下标，指定元素)
my_list.insert(1,6)
print(my_list) # [1, 6, 2, 3, 4]
# 4.追加元素1 在列表末尾添加一个元素
my_list.append(7)
print(my_list) # [1, 6, 2, 3, 4, 7]
# 5.追加元素2 将其他的数据容器的内容取出，依次追加到列表尾部
my_list.extend([1,2,3])
print(my_list) # [1, 6, 2, 3, 4, 7, 1, 2, 3]
# 6.删除元素1 del 列表[下标]
del my_list[0]
print(my_list) # [6, 2, 3, 4, 7, 1, 2, 3]
# 7.删除元素2 列表.pop(下标)
my_list.pop(0)
print(my_list) # [2, 3, 4, 7, 1, 2, 3]
# 8.删除某元素在列表中的第一个匹配项
my_list.remove(3)
print(my_list) # [2, 4, 7, 1, 2, 3]
# 9.清空列表 列表.clear()
# 10.统计某元素在列表中的数量
print(my_list.count(2)) # 2
# 11.统计列表中有多少个元素
print(len(my_list)) # 6
# 12.列表的循环遍历while/for
print("while循环遍历-------------------------------------------------------------------------")
index=0
while index<len(my_list) :
    print(my_list[index])
    index+=1
print("for循环遍历-------------------------------------------------------------------------")
for ele in my_list :
    print(ele)
