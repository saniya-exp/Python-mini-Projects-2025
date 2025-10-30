import random

def coin_toss():
    print("🪙 Welcome to the Coin Toss Simulator!")
    while True:
        choice = input("\nPress Enter to toss the coin or type 'q' to quit: ").lower()
        if choice == 'q':
            print("Thanks for playing! Goodbye 👋")
            break
        result = random.choice(["Heads", "Tails"])
        print(f"The coin landed on: {result}!")

if __name__ == "__main__":
    coin_toss()
