class Students:
     college_name="Lovely Professional University";
      
     def __init__(self):
          print("This is a default construcot")
          
     def __init__(self,name,cgpa): # parametrized construcot 
          self.name=name
          self.cgpa = cgpa
     # you can not have more than one construcot in python 
     # the last one will be taken as main construcot in the process    
     def get_cgpa(self):
          return self.cgpa
          

s1= Students("Abhishek",7.4)
s2= Students("Aryan",7.5)
s3=Students("Priyanshu",7.6)
s4=Students("Gaurav",7.9)


print(s1.name)
print(s2.name)
print(s1.get_cgpa())

# instance attributes and class attributes 
print(s1.name) # instance attribute
print(Students.college_name)
print(s1.college_name)
# class attributes can be accessed in both ways
# if both have same name then instance will be dominated
