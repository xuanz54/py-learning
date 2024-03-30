class Student:
    name=None
    age=None
    gender=None
    # 以__ 开头的魔术方法
    def __init__(self,name,age,gender): # 构造方法
        self.name=name
        self.age=age
        self.gender=gender
    def __str__(self): # 当对象直接被输出时会输出其内存地址 而__str__ 可以转换指定其输出
       return f"名字是{self.name},年龄是{self.age},性别是{self.gender}"
    def __lt__(self, other): #按要求比较两个对象谁更小 less than 返回一个布尔值 注意；le表示小于等于 eq表示相等
       return self.age < other.age
    def __eq__(self, other):
        return self.name==other.name
    def study(self,content='python'):
        print(f"{self.name}在学习{content}")


stu1=Student('xz',20,'男')
stu2=Student('dxz',21,'男')
print(stu1)
print(stu1<stu2) # True
print(stu1==stu2) # False
stu1.study('ai')