import random

def roll_dice():
    print("🎲 Dice Rolling Simulator 🎲")
    while True:
        dice = random.randint(1, 6)
        print(f"\nYou rolled a {dice}!")

        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    roll_dice()
