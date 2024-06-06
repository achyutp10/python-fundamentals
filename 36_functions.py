# def add3(a,b,c):
#   r = a+b+c
#   return r
# print(add3(1,2,3))
# res = add3(2,3,4)
# print(res)

# def add3(a,b,c):
#   print('Inside function',id(a),id(b),id(c))
# x,y,z=10,15,5
# print('Outside function',id(x),id(y),id(z))

# print(add3(x,y,z))

# 4
# def net_sal(basic, allowance, deduction):
#   net = basic+allowance-deduction
#   return net

# n=net_sal(15000,6000,1200)
# q=net_sal(deduction=1000,basic=9000,allowance=6000)
# r=net_sal(10000,deduction=1000,allowance=6000)
# print(n)
# print(q)
# print(r)

# def add(a,b,c):
#   return a+b+c

# print(add(10,5,2))
# # print(add(10,5)) error

# def add(a,b=0,c=0):
#   return a+b+c
# print(add(5,7,2))
# print(add(5,7))
# print(add(5))
# print(add(a=10,b=5,c=2))
# # print(add(b=10,c=5,10)) error
# print(add(10,b=10,c=5))

# def additem(item, L=[]):
#   L.append(item)
#   return L
# l1=[1,2,3,4]
# print(additem(5,l1))
# print(additem(25))
# print(additem(29))
# print(l1)
# print(additem(55))

# 6

# def add(a,b,c,d,e,f):
#   return a+b+c+d+e+f
# print(add(1,2,3,4,5,6))
# print(add(f=1,c=2,b=3,e=4,d=5,a=6))

# def add(a,b,/,c,d,e,f):
#   return a+b+c+d+e+f
# print(add(2,5,6,7,9,4))
# print(add(2,5,d=6,f=7,e=9,c=4))
# # print(add(a=2,b=5,d=6,f=7,e=9,c=4)) error

# def add(a,b,/,c,d,*,e,f):
#   return a+b+c+d+e+f
# print(add(2,5,d=6,c=7,e=9,f=4))
# print(add(2,5,6,7,e=9,f=4))
# # print(add(2,5,d=6,c=7,9,3)) error

# def add(a,b,/):
#   return a+b
# print(add(2,5))

# def add(*,a,b):
#   return a+b
# print(add(a=2,b=5))

# Args

# def fun1(*args):
#   print(type(args), args)
# fun1()
# fun1(10,20)
# fun1(10,20,30,40,50,60,70,80,90,100)
# fun1(10,'hello',24.75,True)

# # This also works
# def fun1(*a):
#   print(type(a), a)
# fun1()
# fun1(10,20)
# fun1(10,20,30,40,50,60,70,80,90,100)
# fun1(10,'hello',24.75,True)


# def fun1(a,b,*args):
#   print(a, b, args)

# # fun1() error
# # fun1(11) error
# fun1(11,22)
# fun1(11,22,33,44,55,66)
# # fun1(a=11,b=22,33,44,55,66) error

# def fun1(*args,a,b):
#   print(a, b, args)
# # fun1(11,22,33,44,55,66) error
# fun1(11,22,33,44,a=55,b=66)

# def fun2(a,b,c):
#   print(a,b,c)
# l1 = [11,22,33]
# fun2(l1[0],l1[1],l1[2])
# t1=(10,20,30)
# str1='sky'
# s1 = {21,55,12}
# # fun2(l1) error
# fun2(*l1)
# fun2(*t1)
# fun2(*str1)
# fun2(*s1)

# def fun3(a,b,c):
#   return a+1,b+1,c+1
# x,y,z=fun3(10,20,30)
# print(x,y,z)

# t=fun3(10,20,30)
# print(t, type(t))

# 8

# def fun2(**kwargs):
#   print(kwargs)
#   print(type(kwargs))
# fun2(name='ajay',roll=10,address='nepal')

# def fun2(**kwargs):
#   for x in kwargs:
#     print(x,kwargs[x])
# fun2(name='ajay',roll=10,address='nepal')

# def fun2(a,b,*args,**kwargs):
#   print(a,b,args,kwargs)
# fun2(10,21,100,200,c=12,d=4)

# l=[1,2,3,4,5]
# l=(1,2,3,4,5)
# l={1,2,3,4,5}
# l={1:'A',2:'B',3:'C',4:'D',5:'E'}
# itr = iter(l)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# def days():
#   l=['sun','mon','tue','wed','thur','fri','sat']
#   i=0
#   while True:
#     x=l[i]
#     i=(i+1)%7
#     yield x
# d = days()
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))

# g=10
# def fun1(a,b):
#   c=a+b #local variable
#   print(c)
#   print(g) # global variable
# print(g)
# # print(c) error
# def fun2():
#   print(g*2)

# fun1(4,8)
# fun2()


# g=10
# def fun1():
#   g=20
#   print(g)
# fun1()
# print('global',g)

# g=10
# def fun1():
#   global g
#   g=g+5
#   print('global',g)
# fun1()
# print('global',g)

# a,b,c,d=11,22,33,44
# def fun1(a=15,b=25):
#   x,y,z=1,2,3
#   print(locals())

# fun1()
# # print(globals())

# Recursive function

def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
print(fact(5))

