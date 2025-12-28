squares = []

for i in range(6):
     squares.append(i*i)
     
print(squares)
# [ output iterable condition]

sq = [i*i for i in range(6)]
print(sq)

s1 = [i*i for i in range(6) if i%2 != 0]
print(s1)

negativeList = [-2,-4,5,3,2,-1]
newList = [0 if val<0 else val for val in negativeList]
print(newList);

words = ["hello","python","javascript","typescript"]
words = [w.upper() for w in words]
print(words)