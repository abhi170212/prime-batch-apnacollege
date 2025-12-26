number =int(input("Enter a  number: "));
if( number % 5 == 0 ) :
     print("Multiple of 5")
else:
     print("Not multiple of 5");
     
     
if(number % 2== 0):
     print("Even Number");
else:
     print("odd number");
     
#############################################################

color = input("Enter the color: ").strip();
match color:
     case "red":
          print("Stop");
     case "yellow":
          print("Look");
     case "green":
          print("Go");
     case _:
          print("not a default in the system of the traffic light")
          
          
          
################################################################

i =1 
while(i<=5):
     print(i);
     i+=1;
     
#################################################################

for i in range(3):
     print(i)
     
for i in range(1,6):
     print(i)

for i in range(2,10,3):
     print(i)
     

#################################################################

def sum(a,b):
     print(a+b)
sum(1,4)



def avg(a,b,c):
     return (a+b+c)/3 ;
print(avg(1,3,5))


def factorial(a):
     ans = 1;
     for i in range(1,a+1):
          ans = ans*i;
     return ans;

print(factorial(2));


################################################################

square = lambda x:x*x;
print(square(2));

