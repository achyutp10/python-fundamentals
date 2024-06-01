# n=int(input("Enter num_of_nos: "))
# sum = 0
# c = 0
# while c<n:
#   d = int(input("Enter a number:" ))
#   sum = sum+d
#   c=c+1
# print(sum)

# n=int(input("Enter num_of_nos: "))
# sump = 0
# sumn = 0
# c = 0
# while c<n:
#   d = int(input("Enter a number:" ))
#   if d<0:
#     sumn = sumn+d
#   else:
#     sump = sump + d
#   c=c+1
# print(sumn)
# print(sump)

# n=int(input("Enter num_of_nos: "))
# sumo = 0
# sume = 0
# c = 0
# while c<n:
#   d = int(input("Enter a number:" ))
#   if d%2 == 0:
#     sume = sume+d
#   else:
#     sumo = sumo + d
#   c=c+1
# print(sumo)
# print(sume)

# n=int(input("Enter num_of_nos: "))
# max = int(input("Enter a number: "))
# c = 0
# while c<n-1:
#   d = int(input("Enter a number:" ))
#   if d>max:
#     max = d
#   else:
#     max=max
#   c=c+1
# print(max)

# n=int(input("Enter num: "))
# bin = 0
# while n>0:
#   r = n%2
#   n=n//2
#   bin = bin*10+r
# print(bin)
# rev = 0
# while bin>0:
#   r=bin%10
#   bin=bin//10
#   rev = rev*10+r
# print(rev)

n=int(input("Enter num: "))
bin = ''
while n>0:
  r = n%2
  n=n//2
  bin = str(r)+bin
print(bin)


