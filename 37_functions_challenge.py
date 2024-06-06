# def difference(a,b):
#   dif = abs(a-b)
#   if dif <= 5:
#     print(True)
#   else:
#     print(False)

# difference(15,10)

# def maxi(a,b,c):
#   if a>b and a>c:
#     print(a, 'is greater')
#   elif b>a and b>c:
#     print(b, 'is greater')
#   else:
#     print(c, 'is greater')
# maxi(15,10,9)

# def posArg(a,b,/):
#   print('My name is '+a+', I am a '+b+'')
# posArg('Achyut', 'Student')

# def planet(id):
#   planets = {
#     1: 'Mercury',
#     2: 'Venus',
#     3: 'Earth',
#     4: 'Mars',
#     5: 'Jupiter',
#     6: 'Saturn',
#     7: 'Uranus',
#     8: 'Neptune'
#   }
#   return planets[id]
# id = int(input("Enter planet id: "))
# if id < 1 or id > 8:
#   print('Invalid input')
# else:
#   print(planet(id))

# def sumZero(scores):
#   sum = 0
#   for i in scores:
#     if i%10==0:
#       sum += i
#   print(sum)
# scores = [200,456,300,100,234,678]
# sumZero(scores)


# def invert(d):
#   newd = {}
#   for k,v in d.items():
#     newd[v] = k
#   return newd

# d1 = {'a':10,'b':20,'c':30,}

# print(invert(d1))

# alp = 'the quick brown fox jumps over the lazy dog'

# def paragram(phrase):
#   letter = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
#   phrase = set(phrase)
#   if phrase >=letter:
#     return True
#   else:
#     return False
# print(paragram('the quick brown fox jumps over the lazy dog'))

#   for i in letter:
#     if i in phrase:
#       print(True)
#     else:
#       print(False)

# print(paragram('the quick brown fox jumps over the lazy dog'))

# 23

# def count(string):
#   countLower = 0
#   countUpper = 0
#   for i in string:
#     if i.islower():
#       countLower += 1
#     elif i.isupper():
#       countUpper += 1
#   return countLower,countUpper

# print(count('Leo MEssi'))

# def minimum(*val, low_limit=None):
#   if low_limit is None:
#     return min(val)
#   else:
#     l = [x for x in val if x>=low_limit]
#     return min(l)
# print(minimum(1,2,5,6,9,3,-5,-9,-23,1,0,8,25,10, low_limit=10))

# Pascal's Triangle
# def pascal(n):
#   r=[1]

#   for i in range(n):
#     print(r)
#     tr = [0]+r
#     r=r+[0]
#     nr = [x+y for x,y in zip(r,tr)]
#     r=nr
# pascal(6)

#  flatten a nested sequence
def flatten(l):
  for e in l:
    if hasattr(e,'__iter__'):
      yield from flatten(e)
    else:
      yield e
print(set(flatten([[1,2,3],[4,5,6],[7,8,9,[5,6],5],10])))