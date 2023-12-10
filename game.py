import random

print("Write your number from 1 to 99:")
answer = input()

d = True
a = 1
b = 99

guess = random.randint(a, b)

while d: 
    print("Is your number bigger or smaller than " + str(guess))
    indicator = input()
    if(indicator == "bigger"):
        a = guess
        guess = random.randint(a, b)
    elif(indicator == "smaller"):
        b = guess
        guess = random.randint(a, b)
    elif(indicator == "correct"):
        print("Boom!")
        d = False
    else:
        print("Invalid input, only write bigger, smaller or correct!")
