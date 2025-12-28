class Employee:
     start_time="10AM"
     end_time="6PM"
     _university_name="Lovely professional University"
 
     
class Teacher(Employee):
     def __init__(self,subject):
          self.subject=subject


class AdminStaff(Employee):
     def __init__(self,role):
          self.role = role


class Accountant(AdminStaff):
     def __init__(self,salary,role):
          super().__init__(role) # parent class invoked
          self.salary=salary
          
          
          



p1= Teacher("Operating System")
print(p1.end_time)
print(p1._university_name)
