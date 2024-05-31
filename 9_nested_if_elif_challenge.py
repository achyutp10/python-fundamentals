# amount = int(input("Enter a amount: "))

# if amount<=1000:
#   discount = amount * 10/100
# elif amount>1000 and amount<=5000:
#   discount = amount * 20/100
# elif amount>5000 and amount <=10000:
#   discount = amount * 30/100
# elif amount>10000:
#   discount = amount * 50/100
# price = amount - discount

# print ("The final price is :",price)

# day = int(input("Enter day: "))

# if day == 1:
#   print("Sunday")
# elif day == 2:
#   print("Monday")
# elif day == 3:
#   print("Tuesday")
# elif day == 4:
#   print("Wednesday")
# elif day == 5:
#   print("Thursday")
# elif day == 6:
#   print("Friday")
# elif day == 7:  
#   print("Saturday")
# else:
#   print('Invalid day')

date = int(input("Enter year: "))

if date % 100 == 0 and date % 400 == 0:
  print('Leap year')
elif date % 4 == 0 and date % 100 != 0:
  print('leap year')
else:
  print('Not Leap year')