n=int(input("Enter the number:"))
a=n//10*10
b=a+10
if(n-a > b-n):
  print(b)
else:
  print(a)
