import random

score = 0

sides = ['h', 't']

print("Welcome to CoinFlip Simulation.")

rounds = int(input("Enter number of flips: "))

for x in range(rounds):

    result = random.choice(sides)
    choice = input("Choose heads or tails (h or t): ")

    if choice[0].lower() == result:
        score += 1
        print("You chose right!")
    else:
        print("You chose wrong!")

print(f"The final score is {score} out of {rounds}.")
