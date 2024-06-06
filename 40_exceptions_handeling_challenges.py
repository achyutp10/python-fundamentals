# class NegativeAgeException(Exception):
#   pass

# age = int(input('Enter age: '))
# def stage(age):
#     if age < 0:
#       raise NegativeAgeException('Age should be +ve')  
#     elif age < 13 and age > 0:
#       print('Kid')
#     elif age <= 19 and age >= 13:
#       print('Teen')
#     elif age <= 50 and age > 19:
#       print('Young')
#     elif age > 50:
#       print('Old')

# try:
#   stage(age)
# except NegativeAgeException as e:
#   print(e)

# balance = 10000
# class AccountBalanceException(Exception):
#   pass

# def withdraw(amt):
#   global balance
#   if balance-amt < 5000:
#     raise AccountBalanceException('Balance should not be less than 5000')
#   else:
#     balance = balance-amt
#     print('Balance after withdraw:', balance)
     
# try:
#   withdraw(6000)
# except AccountBalanceException as e:
#   print(e)

class InvalidFormulaException(Exception):
  pass

def evaluate(formula):
  f = formula.split()
  if len(f) < 3:
    raise InvalidFormulaException('Formula should have spaces')

  if f[1] == '+' or f[1] == '-' or f[1] == '*' or f[1] == '/':
    op1 = int(f[0])
    op2 = int(f[2])
    if f[1] == '+':
      res = op1+op2
    elif f[1] == '+':
      res = op1+op2
    elif f[1] == '-':
      res = op1-op2
    elif f[1] == '*':
      res = op1*op2
    else:
      res = op1/op2
    return res
  else:
    raise InvalidFormulaException('Invalid formula')
  
try: 
  formula = input('Enter the formula, Ex: 10 - 4: ')
  print(evaluate(formula))
except InvalidFormulaException as e:
  print(e)