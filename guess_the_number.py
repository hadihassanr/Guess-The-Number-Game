import random
number_to_guess = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100:)"))
if guess < number_to_guess:
    Print("Too low!")
elif guess > number_to_guess:
    print("Too high!")
else:
    print("You guessed it!")
while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("You guessed it!")

guess = None
guess_count = 0

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))
    guess_count += 1 

    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print(f"You guessed it in {guess_count} tries!")