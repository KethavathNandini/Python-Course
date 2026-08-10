import random
print("Welcome to the game of rolling dice 🎲🎲🎲.")

while True:
    choice = input("press 'Enter' to roll the dice or q to quit.").strip()
    if choice == 'q':
        print("Thanks for playing the game☺️, bye!")
        break
    elif choice == '':
        number = random.randint(1, 6)
        print(f"your number {number}")
    else:
        print("invalid input!")