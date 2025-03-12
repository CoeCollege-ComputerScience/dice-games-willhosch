
import random

def rollDice():
    return random.randint(1,6) + random.randint(1,6)

def craps():

    roll = rollDice()
    print(roll)
    if roll in (7,11):
        result = "Win"
    elif roll in (2,3,12):
        result = "Lose"
    else:
        point = roll
        print(f"Point: {point}")
        roll = rollDice()
        print(roll)
        while roll not in (point, 7):
            roll = rollDice()
            print(roll)
        if roll == point:
            result = "Win" 
        else:
            result = "Lose"
    return result

def main():
    print(craps())

main()
