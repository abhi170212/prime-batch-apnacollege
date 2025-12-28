class student:
     subject="Python"
     college="ABC"
     year="4th year"
     def __init__(self):
          print("this is the constructor")

stu1= student()
stu2= student()

print("this is the address of the object_1" , stu1)
print(stu1.subject)
print(type(stu1));