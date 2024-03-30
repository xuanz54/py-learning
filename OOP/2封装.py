# 定义私有成员变量和成员方法 无法被类对象访问 只能被类成员访问
class Student:
    __name=None
    __age=None


    def __learn(self):
        print(f"{self.__name}在学习")

stu1=Student()