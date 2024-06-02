# num = int(input("Enter a number: "))
# for i in range(1,11):
#   print(num, 'X', i, '=', num*i)

n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
  fact = fact*i
print(fact)