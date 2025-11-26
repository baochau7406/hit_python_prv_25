class STU:
    def __init__(self, name, yob, grade):
        self.name= name
        self.yob=yob
        self.grade=grade
    def describe(self):
        print(f"Name: {self.name}, yob:{self.yob}, grade: {self.grade}")
class TEACHER:
    def __init__(self, name, yob, subject):
        self.name= name
        self.yob=yob
        self.subject=subject
    def describe(self):
        print(f"Name: {self.name}, yob:{self.yob}, subject: {self.subject}")
class DOCTOR:
    def __init__(self, name, yob, specialist):
        self.name= name
        self.yob=yob
        self.specialist=specialist
    def describe(self):
        print(f"Name: {self.name}, yob:{self.yob}, specialist: {self.specialist}")
class WARD:
    def __init__(self,name, person= None):
        self.name=name
        if person is None:
            self.person= []
        else:
            self.person=person
    def add_person (self, person):
        self.person.append(person)
    def describe(self):
        print (f"ward name:{self.name}")
        for p in self.person:
            p.describe()
    def countDoc(self):
        d=0
        for p in self.person:
            if type(p)== DOCTOR:
                d+=1
        print("So luong doctor: ", d)
    def sx_age(self):
        self.person.sort(key= lambda p: p.yob, reverse=True)
        for p in self.person:
            p.describe()
    def avr_tea_age(self):
        tong=0
        d=0
        for p in self.person:
            if type(p)== TEACHER:
                d+=1
                tong+= p.yob
        if (d==0):
            print("Khong co teacher")
            return
        print("Trung binh nam sinh teacher: ", tong/d)
stu1= STU("Chau", 2006, 12)
tea1= TEACHER("Anh", 2006, "Toan")
tea2= TEACHER("Linh", 2010, "Anh")
doc1= DOCTOR("Chi", 2006, "Tam ly")
doc2= DOCTOR("Diep", 2006, "Mat")

w1 = WARD("Ward1")
w1.add_person(stu1)
w1.add_person(tea1)
w1.add_person(tea2)
w1.add_person(doc1)
w1.add_person(doc2)
w1.describe()
w1.countDoc()
w1.sx_age()
w1.avr_tea_age()
    


