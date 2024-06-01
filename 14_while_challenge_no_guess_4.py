import random
n=random.randint(1,10)
guess = 0
print("Enter a number between 1 and 10")
while guess !=n:
  guess=int(input("Enter no: "))
  if guess<n:
    print("It is less")
  elif guess>n:
    print("It is more")
  else:
    print("Congratulations! You have guessed correct")


