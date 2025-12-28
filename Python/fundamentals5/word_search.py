# f = open("sample.txt","r") 
# lineNumber =0;
# # l = f.readline()
# word = "Python"

# while True:
#      l= f.readline();
     
#      if not l:
#           break;
#      lineNumber+=1;
#      if word in l:
#           print(f"{word} found in line number {lineNumber}")


# f.close()


data = True;
line = 1;
word="Python"

with open("sample.txt","r") as f:
     # data = f.readline()
     while data:
          data = f.readline()
          if(word in data):
               print(f"{word} and it appeared in {line}")
               break
          line += 1