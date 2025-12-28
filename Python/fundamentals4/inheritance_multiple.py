class Teacher:
     def __init__(self,salary):
          self.salary = salary

class Student:
     def __init__(self,gpa):
          self.gpa = gpa

class TA(Teacher,Student):
     def __init__(self,salary,gpa,name):
          super().__init__(salary)
          Student.__init__(self,gpa)
          self.name = name 

ta1 = TA(55_000,3.6,"Abhishek Singh")
          
print(ta1.name,ta1.gpa,ta1.salary)          