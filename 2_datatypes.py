# Numeric
x=10 #int
y=10.5 #float
z=True #bool
a=x+2*y #complex

# Sequence
list_nums=[x, y, z] #list--> mutable means can be changed
tuple_nums=(x, y) #tuple--> immutable means cannot be changed
str_num='Hello World!' #string
set_nums={x, y} #set --> unique value --> mutable
dict_nums={'x': x, 'y': y} #dictionary
seq_obj = str(str_num)  #sequence object

p=0
q=1
print(p.__sizeof__())
print(q.__sizeof__())

import math
print(0.12592)
print(12591e-2)
print(math.pi)

# Complex
f=3+5j
print(type(f))
# g=3+5i
# type(g)
g=1.22+3.55J
print(type(g))
b=complex(12,9)
c=complex(12)

print(a.real, a.imag)

print(a)
print(0b1010)
print(0o12)
print(0xA)
# print(0b125)
# print(0b111.0b11)
print(0b101+6j)

# price=int(input("enter price"),2) #0b101
# print(price)

h='123'
# h='abc'
print(int(h))