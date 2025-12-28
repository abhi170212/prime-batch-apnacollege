#operator overloading -> + -> string concatation as well as addition

#function overriding & duck typing 

class Employee:
     def get_designation(self):
          print("Designation = Employee")

class Teacher(Employee):
     def get_designation(self):
          print("Designation = Teacher")
     
t1 = Teacher()
t1.get_designation()