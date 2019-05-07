from array import *
x=array('i',[])
a=int(input("Enter the number:"))
for i in range(a):
  b=int(input("Enter the number:"))
  x.append(b)
print(min(x))
