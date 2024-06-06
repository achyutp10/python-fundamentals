# if x > y syntax error : missing
# if x>y: syntax error indentation program never runs
# print(x)

# Runtime error division by zero
# a = 10
# b=0
# c=a//b
# print(c)

# a=20
# b=7
# c=2
# d=a//(b-c) # if b-c without () is written then logical error occurs
# print(d)

# l = [10,20,30,40,50]
# try:
#   index = int(input('Enter a index: '))
#   print(l[index])
#   print('End of try')
# except:
#   print('Invalid index')
# print('Terminated')

# val = int('abc')
# res = '2'+3

# d= {1: 'a',2:'b'}
# key=int(input('Enter a key: '))
# print(d[key])

# a = int(input('Enter no: '))
# b = int(input('Enter no: '))
# res = a//b
# print(res)

# 6
# l = [10,20,30,40,50]
# try:
#   index = int(input('Enter a index: '))
#   print(l[index])
#   print('End of try')
# except IndexError as msg:
#   print('Invalid index', msg)
# except ValueError as msg:
#   print('Invalid value! Enter integer only', msg)
# except:
#   print('Some error')
# print('Terminated')

# l = [10,20,30,40,50]
# try:
#   index = int(input('Enter a index: '))
#   print(l[index])
#   print('End of try')
# except (IndexError, ValueError) as msg:
#   print(msg)
# print('Terminated')

# ZeroDivisionError
# a = int(input('Enter no: '))
# b = int(input('Enter no: '))
# if b!=0:
#   res = a//b
#   print(res)
# else:
#   print('Cannot divide by zero')

# def div(a,b):
#   if b!=0:
#     c = a//b
#     return c
#   else:
#     raise ZeroDivisionError

# a = int(input('Enter no: '))
# b = int(input('Enter no: '))
# c=div(a,b)
# try: 
#     c=div(a,b)
#     print(c)
# except:
#   print("Zero division")

# print('Before try')

# try:
#   a = int(input('Enter numerator: '))
#   b = int(input('Enter denominator: '))
#   c=a//b
  
#   print('Try block executed successfully')
# except ZeroDivisionError as err:
#   print(err)
# else:
#   print('Division is', c)
# print('Outside try-except-else')


# print('Before try')
# try:
#   a = int(input('Enter numerator: '))
#   b = int(input('Enter denominator: '))
#   c=a//b
  
#   print('Try block executed successfully')
# except ZeroDivisionError as err:
#   print(err)
# else:
#   print('Division is', c)
# finally:
#   print('Finally Block')
# print('Outside try-except-else')

# def div(a,b):
#   try:
#     c=a//b
#     return c
#   except:
#     raise ZeroDivisionError
#   finally:
#     print('Finally block')

# print(div(5,0))

#  10
# class MyError(Exception):
#   def __init__(self, msg):
#     self.msg=msg

#   def __str__(self):
#     # return 'Creating my exception'
#     return self.msg

# try:
#   raise MyError('Some error')
# except MyError as e:
#   print(e)

# try:
#   a = int(input('Enter no: '))
#   try:
#     b = int(input('Enter no: '))
#     try:  
#       c=a//b
#       print(c)
#     except ZeroDivisionError as e:
#       print(e)
#   except ValueError:
#     print('Value Error inner')
# except ValueError:
#   print('Value Error outer')

try:
  a = int(input('Enter no: '))
  b = int(input('Enter no: '))
  c=a//b
  print(c)
except ZeroDivisionError as e:
  print(e)
except ValueError:
  print('Value Error inner')

