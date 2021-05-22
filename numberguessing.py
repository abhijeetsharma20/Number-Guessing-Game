import random
a = random.randrange(1,20)

chance = 5

while chance > 0:
    guess = int(input("Guess the number : "))
    if guess > a:
        print("your number is big!")
    elif guess < a:
        print("your number is small!")
    else:
        print("you won!")
        break
    chance-=1

if chance == 0:
    print("You Lose!")


