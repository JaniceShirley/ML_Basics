class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show_details(self):
        return self.name, self.marks
    
    def is_pass(self):
        if self.marks>=50:
            return True
        else:
            return False
        
class ClassMonitor(Student):
    def __init__(self, name, marks, slist=None):
        super().__init__(name, marks)
        self.slist = slist if slist is not None else []

    def add_student(self, student):
        self.slist.append(student)

s1=Student("Arun", 85)
s2=Student("Janice", 45)
s3=Student("Luna", 70)

c1=ClassMonitor("Mia", 90,[s1, s2])
print("Monitor"'=',c1.name)
print(Student.show_details(s1))
print(Student.is_pass(s2))

c1.add_student(s3)
for student in c1.slist:
    print(student.name)