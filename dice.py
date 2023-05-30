import random

# User enters the number of dice
dice = int(input("Dice: "))

if dice <= 0:
    print("Must have at least one die!")
    quit()

# User enters the number of sides
sides = int(input("Sides: "))

if sides <= 0:
    print("Must have at least one side!")
    quit()

for _ in range(1000):
    roll = []

    for i in range(dice):
        # Gives random number 
        face = random.randint(1, sides)
        roll.append(face)

    print(roll)

