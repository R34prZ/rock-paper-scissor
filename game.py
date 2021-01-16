# importing the necessary modules

import start
from random import choice
import menu
import score
from time import sleep

# making the possible moves list

t = ["Rock", "Paper", "Scissor"]

# defining the function were all game mechanics are
    
def game():
    # mainloop

    run = True
    while run:

        player_move = str(input("What's your move? "))
        pc_move = choice(t)
        # this piece is my solution to confirm "movement" choice/quit to the menu

        print()
        print("_" * 50)
        print("\t\tContinue? ")
        pause = input("Y/N: ")
        print("_" * 50)
        print()

        if pause == "N":
            sleep(0.5)
            print("Ok leaving to the menu...",)
            menu.menu()
            break
        elif pause == "Y":
            pass

        # what to do if the player choice is the same as the computer one (tie)

        if player_move.lower() == pc_move.lower():
            sleep(1)
            print("Tie!")

        # if computer choose Rock

        elif pc_move == "Rock":
            sleep(1)
            if player_move.lower() == "paper":
                print(f"{start.name} wins! No machine can beat him!")
                score.player_score += 1
            if player_move.lower() == "scissor":
                print(f"Computer Wins! {start.name} loses ;(")
            print(f"score is {score.player_score}")

        # if computer choose Paper

        elif pc_move == "Paper":
            sleep(1)
            if player_move.lower() == "scissor":
                print(f"{start.name} wins! No machine can beat him!")
                score.player_score += 1
            if player_move.lower() == "rock":
                print(f"Computer Wins! {start.name} loses")
            print(f"score is {score.player_score}")

        # if computer choose Scissor

        elif pc_move == "Scissor":
            sleep(1)
            if player_move.lower() == "rock":
                print(f"{start.name} wins! No machine can beat him!")
                score.player_score += 1
            if player_move.lower() == "paper":
                print(f"{start.name} was cutted! PC wins...")
            print(f"score is {score.player_score}")