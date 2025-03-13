import random

def roll_die():
    return random.randint(1, 6)

def take_turn(player):
    turn_total = 0
    while True:
        roll = roll_die()
        print(f"{player} rolled a {roll}")
        if roll == 1:
            print(f"{player} loses their turn!")
            return 0
        turn_total += roll
        print(f"{player}'s turn total is {turn_total}")
        hold = input(f"{player}, do you want to hold? (y/n): ")
        if hold.lower() == 'y':
            return turn_total

def play_game():
    player1_score = 0
    player2_score = 0
    winning_score = 100

    while player1_score < winning_score and player2_score < winning_score:
        print(f"\nPlayer 1's turn. Current score: {player1_score}")
        player1_score += take_turn("Player 1")
        if player1_score >= winning_score:
            break

        print(f"\nPlayer 2's turn. Current score: {player2_score}")
        player2_score += take_turn("Player 2")

    if player1_score >= winning_score:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

if __name__ == "__main__":
    play_game()

play_game()