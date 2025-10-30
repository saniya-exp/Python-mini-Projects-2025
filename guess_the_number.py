import random

print("🎯 Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 50...")

# Generate a random number between 1 and 50
number = random.randint(1, 50)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {number} in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")
