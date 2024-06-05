# wh = [int (x) for x in input('Enter hours per day, separated by space: ').split()]
# hw = int(input('Enter salary per hr: '))
# print(sum(wh)*hw)

# list1 = [int (x) for x in input('Enter datas with spaces: ').split()]
# l2 = []
# for i in list1:
#   if i not in l2:
#     l2.append(i)
# print(l2)

# list1 = [int (x) for x in input('Enter datas with spaces: ').split()]
# l2 = ''
# for i in list1:
#   l2 += str(i)
# print(int(l2))

# fav1 = ['pizza','nuggets','hotdog','noodles','pasta','burger']
# fav2 = ['burger','hotdog','noodles','pasta','nuggets','pizza']
# index1 = 10
# index2 = 10

# for i in range(len(fav1)):
#   indx = fav2.index(fav1[i])

#   if i + indx< index1+index2:
#     index1 = i
#     index2 = indx
# print(fav1[index1], index1+index2)

# l1 = [10,15,6,9,12,8,4]
# l2 = [14,6,19,4,7,10,11]
# l3 = []
# for i in l1:
#   if i in l2:
#     l3.append(i)
# print(l3)

# l1 = ['A','D','C','B','C','C','A','B','D','E','A','E']
# result=[]
# for i in l1:
#   if i not in result:
#     result.append(i)
#     count = l1.count(i)
#     result.append(count)
# print(result)

# codes  = ['._' , '_…' , '_._.' , '_..' , '.' , '.._.' , '__.' , '….' , '..' , '.___']

# text = 'deface'

# morse_str=''

# for x in text:
#     morse_str += codes[ord(x)-97] + " "

# print(morse_str)

# l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# l2 = [[5,6,7,8],[5,6,7,8],[5,6,7,8]]
# l3=[]
# for i in range(len(l1)):
#   sum=[]
#   for j in range(4):
#     r=(l1[i][j]+l2[i][j])
#     sum.append(r) 
#   l3.append(sum)
# print(l3)

# l1 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# l2=[]
# for i in range(4):
#   s=[]
#   for j in range(3):
#     s.append(l1[j][i])
#   l2.append(s)
# print(l2)

food = ['pizza','nuggets','hotdog','noodles','pasta','burger']
letter = input('Enter letter: ')
for i in food:
  if i.startswith(letter):
    print(i)