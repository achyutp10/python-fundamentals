# num = int(input("Enter a number: "))
# for i in range(1,11):
#   print(num, 'X', i, '=', num*i)

# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1,n+1):
#   fact = fact*i
# print(fact)

# a = int(input("Enter 1st term: "))
# d = int(input("Enter common difference: "))
# count = int(input("How many terms?: "))
# for i in range(a,a+count*d,d):
#   print(i)

a = int(input("Enter 1st term: "))
b = int(input("Enter 2nd term: "))
d = int(input("How many: "))

for i in range(d):
  print(a)
  c=a+b
  a=b
  b=c

