class person:
    pass
class student(person):
    pass
class teacher(person):
    pass
class worker(person):
    pass
class person_factory:
    def get_person(self,type):
        if type=='s':
            return student()
        elif type=='t':
            return teacher()
        else:
            return worker()
pf=person_factory()
stu=pf.get_person('s')
print(type(stu))
teach=pf.get_person('t')
print(type(teach))
wor=pf.get_person('w')
print(type(wor))