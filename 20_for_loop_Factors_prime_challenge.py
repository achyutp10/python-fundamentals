n = int(input("Enter a no: "))
c=0
for i in range(1,n+1):
  if n%i == 0:
    c += 1
if c==2:
  print("prime no")
else:
  print("not prime")

