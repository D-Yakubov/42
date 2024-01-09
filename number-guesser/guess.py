import random

number = random.randint(0, 10)
guess = int(input("Guess a number between 0 and 10: "))

while True:
    
    if number == guess:
        print("Topdingiz!")
        break
