# for i in range(0,5):
#   for j in range(0,5):
#     if i>=j:
#     # print('(',i+j,')', end=',')
#       print("*", end=' ')
#   print('')

# s1 = 'abc'
# s2 = 'xyz'
# for i in s1:
#   for j in s2:
#     print(i,j, end=' ') 
#   print('')

for n in range(1,30+1):
  c = 0
  for i in range(1,n+1):
    if n%i == 0:
      c += 1
  if c==2:
    print(n)