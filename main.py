import random
# first  I am import random


num = random.randrange(1, 20)

while True:
    userenter = int(input("Guess a Number: "))

    if userenter > num:
        print("Very high number")
    elif userenter < num:
        print("Very low number")
    else:
        print("You guessed the right number!")
        break
