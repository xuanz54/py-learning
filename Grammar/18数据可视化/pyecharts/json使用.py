import json
# json可以是字典 也可以是列表(其中列表中的每个元素是字典)
data = [
    {'d': 1},
    {'x': 2},
    {'z': 3},
]
data2={"dai":1}
json_str=json.dumps(data,ensure_ascii=False) # 转换为json数据 ensure_ascii=False设置编码正常显示中文
print(json_str)
print(type(json_str))  #json.loads()把json转换成对于的字典或者列表