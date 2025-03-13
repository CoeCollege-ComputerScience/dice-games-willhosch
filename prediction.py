def rollDice():
    import random
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    dice5 = random.randint(1, 6)
    dice6 = random.randint(1, 6)
    dice7 = random.randint(1, 6)
    dice8 = random.randint(1, 6)
    dice9 = random.randint(1, 6)
    dice10 = random.randint(1, 6)
    return str(str(dice1)+str(dice2)+str(dice3)+str(dice4)+str(dice5)+str(dice6)+str(dice7)+str(dice8)+str(dice9)+str(dice10))

def takeTurn(player):
    while True:
        diceNums = rollDice()
        prediction = input(f"{player}, what is your prediction? Enter a number between 1 and 6: ")
        print (diceNums)
        if diceNums.count(prediction) >= 2:
            print(f"{player} has guessed correctly!")
            return 1
        else:
            return 0

def playGame():
    players = ["Player 1", "Player 2", "Player 3"]
    while len(players) > 1:
        for player in players:
            print(f"\n{player}'s turn.")
            if takeTurn(player) == 0:
                players.remove(player)
                print(f"{player} has been eliminated!")
    print(f"{players[0]} wins!")

playGame()