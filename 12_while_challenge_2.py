# c = 0
# while c<5:
#   print(c, 'Hello')
#   c = c+1

# n = 1245

# while n>0:
#   r=n%10
#   n=n//10
  
#   print(r)

# a = 54
# print(a//10) #--> 5
# print(a/10) #--> 5.4

# n = int(input("Enter a number: "))
# c = 1
# while c<=10:
#   print(n, 'x', c, '=', n*c)
#   c=c+1

# n = int(input("Enter a number: "))
# c = 0
# while n>0:
#   n=n//10
#   c+=1
# print(c)

# n = int(input("Enter a number: "))
# sum = 0
# while n>0:
#   r = n%10
#   n=n//10
#   sum = sum+r
# print(sum)

# n = int(input("Enter a number: "))
# rev = 0
# while n>0:
#   r = n%10
#   n=n//10
#   rev = rev*10+r
# print(rev)

n = int(input("Enter a number: "))
m=n
rev = 0
while n>0:
  r = n%10
  n=n//10
  rev = rev*10+r
if  m==rev:
  print("Palindrome")
else:
  print('Not Palindrome')
