salary = input("Enter the salary: ");
if salary <= 30000:
     tax = (salary * 5)/100
elif salary > 30000 and salary < 70000:
     tax = (salary*15) / 100 
else:
     tax = (salary*25)/100
     
################################################################

def printNumberBetween(a,b):
          for i in range(a,b+1):
               