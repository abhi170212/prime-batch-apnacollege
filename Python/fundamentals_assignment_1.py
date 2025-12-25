name=input("enter your name: ");
age = int(input("Enter your age: "));
print(f"Hello {name} , you are {age} years old");


#######################################################


num_1 = int(input("Enter the first number: "));
num_2 = int(input("Enter the second number: "));
print(num_1+num_2)
print(num_1-num_2)
print(num_1*num_2)
print(num_1/num_2)


#########################################################


floatNum=float(input("Enter the float number: "))
intNum= int(input("Enter the number: "))
intNum2 = int(input("Enter the second number: "))

average = (floatNum+intNum+intNum2) / 3 ;
print(f"their avergae is {average}")

##########################################################

enterNumber = input("Enter a number: ");
print(int(enterNumber),type(int(enterNumber)));
print(float(enterNumber),type(float(enterNumber)));
print(str(enterNumber),type(str(enterNumber)));


############################################################

x = 10+3*2**2 
print(x);

############################################################

a = int(input("Enter the first number: "));
b = int(input("Enter the second value: "));

temp = a 
a = b 
b = temp 

print(a,b);

#############################################################

tempCel = input("Enter the temperature in celsius: ");
tempCel = float(tempCel);
fahrenheitvalue = ((tempCel*9)/5)+32;
print(fahrenheitvalue);

##############################################################

rad = int(input("Enter the radius: "));
print(3.14 * rad*rad);

##############################################################

p = float(input("Enter the principal amount: "));
r = float(input("Enter the rate: "));
t = float(input("Enter the time: "));

i = (p*r*t) / 100 ;
print(i);

#############################################################

decimal = float(input("Enter the decimal: "));
integerPart = int(decimal);
decimlNumber = decimal - integerPart ; 
print(f"The integer part is {integerPart} and decimal part is {decimal}");

