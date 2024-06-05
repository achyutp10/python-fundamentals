# list1 = [1,2,3,4,5]
# print(list1[1])
# print(list1[-2])

# l2 = list((1,2,3,4,5))
# print(l2)

# l3 = ['John', 12, 13.4, True, 5+5j]

# li = [12,1,3,4,5,13,16]
# li[1] = 100
# li[2] = 'abc'
# li.append(50)
# print(li)

# l = [1,2,3,4,5,6,7,8,9,10]
# print(l[4])
# print(l[-4])
# l[6] = 15
# x=l[6]
# print(x)
# print(l[:])
# print(l[3:])
# print(l[3:9])
# print(l[3:9:2]) #[start:end:step]
# print(l[0:10:2]) 
# print(l[-1:-11:-1]) 
# print(l[-1:-11:-2]) 
# print(l[::-1]) 
# print(l[::-2]) 

# l[0:3] = [10,20,30]
# l[0:3] = [10,20]
# l[0:3] = [10,20,30,40,50]
# l[::2] = [11,22,33,44,55]
# l[::3] = [11,22,33,44]
# print(l)

# l1 = [1,2,3]
# l2 = [8,9,10]
# print(l1+l2)

# print(l1+[4])

# print(l1.extend([4,5,6]))
# print(l1*2)
# if 2 or 4 in l1:
#   print("Found")
# else:
#   print("Not found")

# l1 = [5,6,7,8,9]
# for i in l1:
#   print(i)

# for i in range(len(l1)):
#   print(l1[i])

# for i in range(2,len(l1)):
#   print(l1[i])

# for i in range(len(l1)-1,-1,-1):
#   print(l1[i])

# for i in range(-1,(len(l1)+1),-1):
#   print(l1[i])

# i = 0
# while i < len(l1):
#   print(l1[i])
#   i=i+1

# l1.pop()
# l1.pop(0)

# del l1[0:2]
# print(l1)

# l1.remove(6)

# l1.clear()

# l1.index(6)
# l1.index(6,2,5)
# l1.count(6)
# l1.reverse()
# l1=['yy','jj','mm','BB','aa','ZZ']
# l1.sort(key=str.lower,reverse=True)

# l1 = [x for x in range(10)]
# l2 = [x**2 for x in range(1,6)]
# l3 = [x for x in (10,5,7,8,12,3) if x%2==2]
# l4 = [x.lower() for x in 'Python']
# l5 = [x for x in 'ab12de-$fg4$hi2' if x.isalpha()]

# data = input("Enter name: ")
# l6 = data.split()
# print(l6)

# l6 = input("Enter Names: ").split()
# print(l6)

l7 = [10,20,['a','b'['c','d']],30,40]

print(l7[0])
print(l7[2][0])
print(l7[2][2][1])

a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[9,8,7],[6,5,4],[3,2,1]]

c=[]
for i in range(len(a)):
  s=[]
  for j in range(len(a[0])):
    s.append(a[i][j]+b[i][j])
  c.append(s)
print(c)