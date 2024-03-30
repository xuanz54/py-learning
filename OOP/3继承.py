class Person: # 父类
    name=None
    age=None
    def speak(self,content):
        print(f"{self.name}:{content}")
class Animal:
    def eat(self):
        print(f"{self.name}在吃饭")

class Stu(Person,Animal):  # 子类 Stu继承Person Animal 写在前面的优先级高
    name='student' # 复写父类的成员属性
    def speak(self,content):
        print("子曰：：：")
        super().speak() # 调用父类
    def study(self):
        print(f"{self.name}在学习")


stu1=Stu()
stu1.name="xz"
stu1.eat()
stu1.speak("aaaaaaaaa")
