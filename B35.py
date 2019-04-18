str=raw_input("Enter the string and digits:")
count=0
for i in str:
  if(i.isdigit()):
    count=count+1
print(count)
