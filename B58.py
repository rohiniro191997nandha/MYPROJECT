n=int(input("Enter how many number:"))
m=int(input("Enter the number:"))
l=[]
c=0
for i in range(n):
  num=int(input("Enter the number:"))
  l.append(num)
for x in l:
  if(x==m):
    c=c+1
if(c==0):
  print("No")
else:
  print("Yes")
