d1 = {
  'abacus': 'a calculator',
  'bachelor': 'unmarried person',
  'cable': 'strong rope'
}
d2 = {
  101: 'Smith',
  102: 'John',
  103: 'Mark',
  104: 'David'
}  
# print(d1['abacus'])
# print(d2[102])

# d2[102] = 'Mathew'
# print(d2[102])
# d2[105] = 'Achyut'
# print(d2)

# del d2[105]
# print(d2)
# for i in d2:
#   print(i)

# for i in d2:
#   print(i, d2[i])

# d2 = { 'fruit' : 'apple', 'vegetable ' : 'carrot' , 'dish' : 'salad'}

#  003 Dict comp 1

# d1 = dict()
# # print(type(d1))
# d1['apple']='red' 
# d1['mango']='yellow' 
# # print(d1)

# for x in range(1,6):
#   d1[x]=x*2
# # print(d1)

# d5 = {}
# print(type(d5))

# for x in range(1,6):
#   d5[x]=2*x
# print(d5)

# d2 = dict(((1,2),(2,4),(3,6)))
# print(d2)
# d2 = dict(([1,11],[2,22],[3,33]))
# print(d2)
# d2 = dict((('ab','cd','ef')))
# print(d2)
# d2 = dict(([1,11,12],[2,22,23],[3,33,34])) X
# print(d2)
# l1 = [(1,2),(5,6),(8,9)]
# d2 = dict(l1)
# print(d2)

# l1 = ['A','B','C']
# l2 = ['apple','ball','cat']
# dic2 = dict(zip(l1,l2))
# print(dic2)

# s1 = {7,8,9}
# str1 = 'AJK'
# dic3 = dict(zip(s1,str1))
# print(dic3)

# dic3 = dict(zip([10,20,30],(101,102,103,104,105)))
# print(dic3)

# l1 = ['A','B','C']
# for item in enumerate(l1):
#   print(item)

# dict4 = dict(enumerate(l1))
# print(dict4)

# dict6 = {x:x**2 for x in range(1,5)}
# print(dict6)

# dict6 = {x:x**2 for x in range(1,5)}
# print(dict6)

# dict6 = dict((x,x**2) for x in range(1,5))
# print(dict6)

l1 = [1,2,3]
l2 = ['A','B','C']

# for x,y in zip(l1,l2):
#   print(x,y)

# dict8 = dict((x,y) for x,y in zip(l1,l2))
# print(dict8)

# dict8 = {x:y for x,y in zip(l1,l2)}
# print(dict8)

# for x,y in enumerate(l2):
#   print(x,y)

# dict9={x:y for x,y in enumerate(l2)}
# print(dict9)

# dict9= dict((x,y) for x,y in enumerate(l2))
# print(dict9)

# Looping over a dictionary

# d1 = {
#   101: 'Production',
#   102: 'Accounts',
#   103: 'Sales & Marketing',
#   104: 'Inventory'
# }

# for x in d1:
#   print(x)

# for x in d1:
#   print(x,d1[x])

# for x in d1:
  # print(x,d1.get(x))
  # print(x,d1[106]) # error
  # print(x,d1.get(106)) no error
  # print(x,d1.get(106, 'Invalid key'))
  # print(d1.keys())
  # print(d1.values())

# print(d1.items())

# for k in d1.keys():
#   print(k, d1[k])

# for v in d1.values():
#   print(v)

# for x,y in d1.items():
#   print(x,y)

# Dictionary methods

# d1 = {
#   101: 'Production',
#   102: 'Accounts',
#   103: 'Sales & Marketing',
#   104: 'Inventory'
# }
# d2 = d1.copy()
# print(d2)
# d2[102]='abc'
# d1[103]='xyz'
# print(d1)
# print(d2)

# d2 = {
#   105: 'Designing',
#   106: 'Packaging'
# }
# d1.update(d2)
# print(d1)

# print(d1.get(102))
# print(d1.get(110))
# print(d1.setdefault(102))
# print(d1.setdefault(110))
# d1.setdefault(111,'adv')
# print(d1)

# l1 = [11,22,33,44]
# d3 = {}
# print(d3.fromkeys(l1))
# print(d3.fromkeys(l1,100))
# print(d3.fromkeys(l1,'Hello'))

# d1 = {
#   101: 'Production',
#   102: 'Accounts',
#   103: 'Sales & Marketing',
#   104: 'Inventory'
# }

# d1.pop(101)
# d1.pop(110)
# d1.pop(110,'None')
# print(d1)

# d1[110] = "Adv"

# print(d1)
# print(d1.popitem())
# d1.clear()
# print(d1)
# del d1
# print(d1)

# birthdays = {
#   'Sachin': '03/14/2003',
#   'Carl': '01/17/2001',
#   'Khan': '12/10/2006',
#   'Donald': '06/14/2010',
#   'Rohan': '01/06/2005',
# }

# name = input("Enter your name: ")
# if name not in birthdays:
#   print("Name not found")
# else:
#   print("Mr./Miss {} was born on {}".format(name, birthdays[name]))

# d1 = {
#     'piece': 'a portion of an object or of material, produced by cutting',
#     'patch': 'a small area that is different from the area around it',
#     'area': 'a region or part of a town, a country, or the world',
#     'visit': 'go to see and spend time with',
#     'with': 'accompanied by',
#     'small': 'of a size that is less'
# }

# keys = list(d1.keys())
# values = list(d1.values())

# lens = [len(x) for x in values]
# # print(keys)
# # print(values)
# # print(lens)

# max_lenght = max(lens)
# min_lenght = min(lens)

# max_index = lens.index(max_lenght)
# min_index = lens.index(min_lenght)

# print("Max", keys[max_index], values[max_index])
# print("Min", keys[min_index], values[min_index])

# countries = {
#   # 'A':[ 'America' ,'Alaska' ,'Argentina'],
#   # 'B':['Bhutan','Brazil','Bahrain'],
#   # 'C':['China','Costa Rica','Cuba']
#   }
# for i in range(4):
#   name = input("Enter country name: ")
#   if name[0].upper() not in countries:
#     countries[name[0].upper()] = [name]
#   else:
#     countries[name[0].upper()].append(name)
# print(countries)

# roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# number = input("Enter roman no in upper case: ")
# deci_no=0

# i=0
# while i < len(number):
#   if i+1 < len(number) and roman[number[i]]<roman[number[i+1]]:
#     deci_no += roman[number[i+1]] - roman[number[i]]
#     i+=2
#   else:
#     deci_no += roman[number[i]]
#     i+=1
# print(deci_no)

students = {}

for i in range(3):
  name = input("Enter name: ")
  roll = input("Enter roll: ")
  dept = input("Enter dept: ")
  students[name] = {'Roll':roll, 'Name': name, 'Dept': dept}
print(students)