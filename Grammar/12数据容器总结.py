'''
都可以使用for进行遍历 可以使用 len() max() min()等方法
可以进行相互格式转换 list() tuple() str() set()
sorted()进行排序 排序的结果都变成列表对象默认从小到大 若将reverse参数的值设置为True 则排序结果为从大到小
'''
tuple = (2, 3, 1, 5, 4)
print(sorted(tuple)) # [1, 2, 3, 4, 5]
print(sorted(tuple, reverse=True)) # [5, 4, 3, 2, 1]
