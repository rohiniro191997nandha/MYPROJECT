def sum(n,k):
  a=0;
  for i in range(1,n+1):
    a+=(i%k);
  return a;
n=10;
k=2;
print(sum(n,k))
