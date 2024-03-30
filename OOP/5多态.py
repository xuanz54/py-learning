class person: # 含有抽象方法的类为抽象类
    def work(self):  # 含有空实现方法为抽象方法
        pass

class student(person):
    def work(self):
        print("学生在学习")


class teacher(person):
    def work(self):
        print("老师在上课")

def func(identity:person):
    identity.work()

func(student())
func(teacher())
