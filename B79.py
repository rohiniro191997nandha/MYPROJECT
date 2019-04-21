import math
n=int(input("Enter the number:"))
m=int(input("Enter the number:"))
c=n*m
root=math.sqrt(c)
if int(root+0.5)**2==c:
  print("Yes")
else:
  print("No")
