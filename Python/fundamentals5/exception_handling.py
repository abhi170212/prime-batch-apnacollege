try:
     x = int(input("enter x: "))
     ans = 10/x
     
except ZeroDivisionError:
     print(f"Division by 0 is not possible")
     
except ValueError:
     print(f"Invalid Input")
     
else:
     print(f"ans = {ans}")
finally :
     print(f"this is the end of our programme")