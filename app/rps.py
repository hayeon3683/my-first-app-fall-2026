# RPS game

# organizatioanl strcuture of our python file

# 1. import at the top

import random

# 2. followed by any constants

VALID_OPTIONS = ["rock", "paper", "scissors"]

# 3. functions or classes

def determine_winner(u, c):
    if u == "rock" and c == "rock":
        return("TIE GAME")
    elif u == "rock" and c == "paper":
        return("COMPUTER WINS")
    elif u == "rock" and c == "scissors":
        return("USER WINS")
    elif u == "paper" and c == "rock":
        return("COMPUTER WINS") # OOPS
    elif u == "paper" and c == "paper":
        return("TIE GAME")
    elif u == "paper" and c == "scissors":
        return("USER WINS") # OOPS
    elif u == "scissors" and c == "rock":
        return("COMPUTER WINS")
    elif u == "scissors" and c == "paper":
        return("USER WINS")
    elif u == "scissors" and c == "scissors":
        return("TIE GAME")

# 4. main conditional
 
if __name__ == "__main__":

    # only run the code below
    # if we exectue this fiel from the command line
    # but not if we import from this file

    # ASK USER FOR AN INPUT (R/P/S)

    user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
    print("USER:", user_choice)

    # VALIDATIONS

    if user_choice not in VALID_OPTIONS:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        # exit()
        quit()

    # GENERATE RANDOM COMPUTER CHOICE

    computer_choice = random.choice(VALID_OPTIONS)
    print("COMP:", computer_choice)

    # DETERMINE THE WINNER

    winner = determine_winner(u=user_choice, c=computer_choice)
    print (winner)
    # quick alias to facilitate some copy and pasting
    # we will soon move this into a function anyway
   