import random
random_number = random.randint(1, 9)
try:
    guess = int(input("Guess a number between 1 and 9: "))
    if guess < 1 or guess > 9:
        print("This number is not between 1 and 9.")
    elif guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed it exactly right!")
except ValueError:
    print("This is an invalid response.")
