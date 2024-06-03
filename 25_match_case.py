day = int(input('Enter day number: '))

match day:
  case 1:
    print("Sunday")
  case 2:
    print("Monday")
  case 3:
    print("Tueday")
  case 4:
    print("Wednesday")
  case 5:
    print("Thursday")
  case 6:
    print("Friday")
  case 7:
    print("Saturday")
  case _:
    print("Invalid Day Number")