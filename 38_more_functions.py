# Nested functions

# def display(name):
#   print('Hello',name)

# # display()

# d = display
# d('Achyut')

# def outer():
#   def Inner():
#     print('Innter Function, Encapsulated function')

#   Inner()
#   print('Outer Function')
# # Inner() error
# outer()

# def display():
#   print('Hello world')

# def fun(d):
#   d()
# fun(display)

# def add(x,y):
#   print(x+y)

# def sub(x,y):
#   print(x-y)

# def fun(f,x,y):
#   f(x,y)
# fun(add,15,10)
# fun(sub,15,10)

# def outer():
#   def display():
#     print('Hello world')
#   return display
# d = outer()
# d()

# Closure
# def closure():
#   msg = 'hello'
#   def display():
#     print('*'*10)
#     print(msg)
#     print('*'*10)
#   return display
# d = closure()
# d()

# def closure(msg):
  
#   def display():
#     print('*'*10)
#     print(msg)
#     print('*'*10)
#   return display
# d = closure('Welcome')
# d()

# class Dept:
#   def __init__(self):
#     self.depts = {
#       'hr': 'Human Resource',
#       'acc': 'Accounts & Finance',
#       'it': 'Information Technology',
#       'adm': 'Administration'
#     }
#   def __call__(self,dept):
#     return self.depts[dept]
# d = Dept()
# print(d('hr'))

# def Dept():
  
#     depts = {
#       'hr': 'Human Resource',
#       'acc': 'Accounts & Finance',
#       'it': 'Information Technology',
#       'adm': 'Administration'
#     }
#     def dName(dept):
#       return depts[dept]
#     return dName
# d = Dept()
# print(d('hr'))

# Decorators

# def decorators(fun):
#   def wrapper(msg):
#     print('*'*10)
#     fun(msg)
#     print('*'*10)
#   return wrapper

# @decorators
# def display(msg):
#   print(msg)

# # d = decorators(display)
# # d('Hello')
# display('Welcome')

# def miles2km(miles):
#   kms = 1.6*miles
#   return kms
# print(miles2km(10))

# k = lambda miles: 1.6*miles
# print(k(10))  

# def add(a,b):
#   c=a+b
#   return c
# print(add(10,20))

# f = lambda a,b: a+b
# print(f(5,10))

f = lambda a,b: a if a>b else b
print(f(5,10))
print(f(5,10))

