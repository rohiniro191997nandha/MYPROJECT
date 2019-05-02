n=input("Enter the sentence:")
c=0
for i in n:
  if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
    c=c+1
    if c==0:
      print("No")
    else:
      print("Yes")
