a = int(input("Enter a age: "))
b = int(input("Enter b age: "))
c = int(input("Enter c age: "))

if a>b and a>c:
  print('A is older')
elif b>a and b>c:
  print('B is older')
else:
  print('C is older')