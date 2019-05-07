m=int(input("Enter how many number:"))
n=int(input("Enter the number:"))
l=[]
c=0
for i in range(m):
  n1=int(input("Enter the number:"))
  l.append(n1)
for j in l:
  if(n==j):
    c=c+1
print(c)
