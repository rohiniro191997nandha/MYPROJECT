l=[]
n=int(input("Enter how many number:"))
for i in range(n):
  num=int(input("Enter the number:"))
  l.append(num)
for x in l:
  if(x%2!=0):
    print(x)
