import sys
from random import choice

valid_plays = ['rock', 'paper', 'scissors']

player1 = input("Player One: ").lower()
if player1 not in valid_plays:
        print("Error prompting player1")
        sys.exit()

player2 = choice(valid_plays)

if player1 == player2:
        print("It's a tie")
elif player1 == "rock":
        if player2 == "scissors":
                print("Player 1 wins")
        elif player2 == "paper":
                print("Player 2 wins")
elif player1 == "paper":
        if player2 ==  "rock":
                print("Player 1 wins")
        elif player2 == "scissors":
                print("Player 2 wins")
elif player1 == "scissors":
        if player2 == "paper":
                print("Player 1 wins")
        elif player2 == "rock":
                print("Player 2 wins")
else:
        print("Something went wrong")
