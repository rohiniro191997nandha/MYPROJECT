year=int(input("Enter the Year:"))
if(Year%400==0)or(Year%4==0)and(Year%100!=0):
  print("Yes")
 else:
  print("No")
