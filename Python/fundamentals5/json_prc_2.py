import json 
with open("prc.json","r") as f:
     py_obj=json.load(f)
     print(py_obj)
     

student = {
    "name": "Abhishek Singh",
    "age": 22,
    "isTeacher": False,
    "skills": ["Python", "Machine Learning"],
    "gpa": 3.8
}
with open("student.json","w") as f:
     json.dump(student,f,indent=4,sort_keys=True)