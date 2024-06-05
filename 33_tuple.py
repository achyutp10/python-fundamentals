# Immutable value cannot be changed

# tuple1 = ('Jack',45,38.6,False,5+6j)
# print(tuple1[2])
# t1 = (1,2,3)
# t2 = (4,)
# t3 = tuple((1,2,3,4))
# t5=1,2,3,4
# print(t5)
# print(type(t5))
# a,b,c,d=t5
# print(a)
# print(b)
# print(c)
# print(d)

# x,y,z='SKY'
# a,b,*c=t5
# print(a)
# print(b)
# print(c)

l1 = [x for x in range(10)]
print(l1)
t1 = tuple(x for x in range(10))
print(t1)
t2 = (*(x for x in range(10)),)
print(t2)
t3 = (*(x for x in range(1,10,2)),)
print(t3)
t4 = (*(x for x in 'python'),)
print(t4)
t5 = (*(x for x in 'PyThOn' if x.islower()),)
print(t5)
t6 = tuple(x for x in 'PyThOn' if x.islower())
print(t6)
t7 = tuple(x**2 for x in (1,3,5,7,9))
print(t7)