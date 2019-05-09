m=int(input("Enter how many number:"))
n=int(input("Enter the number:"))
l=[]
c=0
for i in range(m):
  num=int(input("Enter the number:"))
  l.append(num)
for j in l:
  if(j%2!=0):
    c=c+1
    if(c==n):
      print(j)
