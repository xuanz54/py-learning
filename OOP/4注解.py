# 类型注解
my_dict :dict[str,int]={
   "name":1,
    "age":2
}
year1:str ="1111111111"
year2="11111111111" # type: str

# 函数注解
def add(x:int,y:int) ->int: # 返回值也是int
    return (x+y)
result = add(1, 1)

# Union联合注解
from typing import Union
new_dict:dict[str,Union[str,int]] ={ # 描述多种类型(值为str或者int)
    "name":"dxz",
    "age":20
}
def func(data:Union[str,int]): # data可以是str或者int
    pass


