f = open("sample.txt","r") # file object
 
data = f.read()
line = f.readline();
print(type(data))
print(data);

f.close(); 