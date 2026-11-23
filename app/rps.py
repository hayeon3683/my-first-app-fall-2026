# RPS game

# organizational structure of our python file

# 1. imports at the top
import random

# 2. followed by any constants
VALID_OPTIONS = ["rock", "paper", "scissors"]

# 3. functions or classes
def generate_random_choice():
    return random.choice(VALID_OPTIONS)


def determine_winner(u, c):
    if u == "rock" and c == "rock":
        return "TIE GAME"
    elif u == "rock" and c == "paper":
        return "COMPUTER WINS"
    elif u == "rock" and c == "scissors":
        return "USER WINS"
    elif u == "paper" and c == "rock":
        return "USER WINS"
    elif u == "paper" and c == "paper":
        return "TIE GAME"
    elif u == "paper" and c == "scissors":
        return "COMPUTER WINS"
    elif u == "scissors" and c == "rock":
        return "COMPUTER WINS"
    elif u == "scissors" and c == "paper":
        return "USER WINS"
    elif u == "scissors" and c == "scissors":
        return "TIE GAME"


# 4. main conditional
if __name__ == "__main__":
    # only run the code below if we execute this file from the command line
    user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
    print("USER:", user_choice)

    if user_choice not in VALID_OPTIONS:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        quit()

    computer_choice = generate_random_choice()
    print("COMP:", computer_choice)

    winner = determine_winner(u=user_choice, c=computer_choice)
    print(winner)
