# Sort the letters
# str = 'bghtyxsyuoinaf'
# ss = sorted(str)
# print(ss)

# str2=''.join(ss)
# print(str2)

# product=str(input("Enter product name: "))
# price=str(input("Enter price: "))
# total_len = len(product)+len(price)

# dots = '.'*(25-total_len)
# displayable = product+dots+price
# print(displayable)

# cp = input('Enter confirm password: ')
# if p1 == cp:
#   print('Password matched')
# else:
#   if p1.casefold() == cp.casefold():
#     print("Check cases")
#   else:
#     print('Password not matched')

# cn = input('Enter card no: ')

# if len(cn) == 16:
#   sliced = cn[13:16]
#   four = "*"*4+' '
#   dispno = four*3+sliced
   
#   print(dispno)

  # (s.rjust(10,'*')

# pos=cn.find('@')
# user = cn[:pos]
# domain = cn[pos+1:]
# print(user,domain)

# s1 = input('Enter String: ')
# rev = s1[::-1]

# if s1 == rev:
#   print('Palindrome')
# else:
#   print('Not palindrome')

#   print(s1+rev)


# date = input('Enter date in dd/mm/yyy: ')
# l= date.split('/')
# print('day:', l[0])
# print('month:', l[1])
# print('year:', l[2])

# s1 = input('Enter 1st string: ')
# s2 = input('Enter 2nd string: ')

# if len(s1) != len(s2):
#   print('Not Anagram')
# else:
#   for i in s1:
#     if i not in s2:
#       print('Not Anagram')
#       break
#   else:
#     print('Anagram')

# s1 = input('Enter a string: ')
# low=''
# upp=''
# for i in s1:
#   if i.islower():
#     low += i
#   elif i.isupper():
#     upp += i
# print(low, upp)
punct = '''!()-[]{}:;'"\,<>./?`~@#$%^&*&_-=+'''

s1 = input('Enter a string: ')
s2=''
for x in s1:
  if x not in punct:
    s2=s2+x
print(s2)

