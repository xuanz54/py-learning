# 集合(set) 元素不能重复,且元素无序,允许修改
my_set={1,True,'a',1.1,'a'}
print(my_set) # 只有一个'a'
print(type(my_set))
my_set.add('b') #添加一个元素
my_set.remove('a') #移除一个元素
my_set.pop() # 由于不支持索引 表示随机移除一个，返回值为该移除的元素

set1={1,2,3}
set2={3,4,5}
print(set1.difference(set2)) # {1,2}  返回一个新集合（集合1-集合2），原集合均不变
set1.difference_update(set2) # 在集合1中删除和集合2中元素相同的元素，集合1该改变，集合2不变
print(set1) # {1,2}
print(set1.union(set2)) # {1,2,3,4,5} 合并两个集合(并去重) 返回一个新集合
print(len(set1)) # 2
print("----------------------------------")
# 集合由于没有索引，固不支持while遍历 只能使用for遍历
for ele in set2 :
    print(ele)