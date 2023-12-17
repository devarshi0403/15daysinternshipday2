import random

num=random.randint(0,9)
guess=int(input("Guess the Number:"))
while guess!=num:
  if guess < num:
    print("too low")
    guess = int(input("enter number again : "))
  elif guess > num:
    print("too high")
    guess = int(input("enter number again : "))
  else:
    break
print("you guess right")
  