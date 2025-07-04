
import random
from secrets import choice
from unittest import result



def get_choices():
    player_choice= input("Enter a choice(rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    
    computer_choice=random.choice(options)
    choices={"player": player_choice, "computer": computer_choice}
    return choices


def check_winner(player, computer):
    print (f"You chose {player}, computer chose {computer}")
    if player==computer:
        return "It's a tie!"
    
    elif player =="rock":
        if computer =="scissors":
            return "Rock smashes scissors! You win."
        else:
            return "Paper covers Rock! You lose."
        
    elif player =="paper":
        if computer =="rock":
            return "Paper covers Rock! You win."
        else:
            return "Scissors cuts Paper! You lose."

    elif player =="scissors":
        if computer =="paper":
            return "Scissors cuts paper! You win."
        else:
            return "Rock smashes Scissors! You lose."
choices=get_choices()
result=check_winner(choices["player"], choices["computer"])
print (result)
