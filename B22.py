from array import *
a=array('i',[])
n=int(input("Enter the number:"))
for i in range(n):
  num=int(input("Enter the number:"))
  a.append(num)
print(max(a))
