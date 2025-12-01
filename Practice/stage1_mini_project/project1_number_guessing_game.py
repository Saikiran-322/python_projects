import random

secret = random.randint(1,10)

while True:
    guess = int(input("Enter your guess(1-10): "))

    if guess==secret:
        print("Correct! You guessed it.")
    elif guess < secret:
        print("Too low.")
    else:
        print("Too High.")