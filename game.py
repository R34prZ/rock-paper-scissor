# importing the necessary modules

import start
import random
import menu
import time

# making the possible moves list

t = ["Rock", "Paper", "Scissor"]

# defining the function were all game mechanics are

def game():

    # player movement, computer movement and score

    player_move = str(input("What's your move? "))
    pc_move = random.choice(t)
    global score
    score = 0

    # mainloop

    run = True
    while run:

        # this piece is my solution to confirm "movement" choice/ quit to the menu

        print()
        print("_" * 50)
        print("\t\tContinue? ")
        pause = input("Y/N: ")
        print("_" * 50)
        print()

        if pause == "N":
            time.sleep(0.5)
            print("Ok leaving to the menu...",)
            menu.menu()
            break
        elif pause == "Y":
            pass

        # what to do if the player choice is the same as the computer one (tie)

        if player_move.lower() == pc_move.lower():
            time.sleep(1)
            print("Tie!")
            game()
    
        # if computer choose Rock

        if pc_move == "Rock":
            time.sleep(1)
            if player_move.lower() == "paper":
                print(f"{start.name} wins! No machine can beat him!")
                score += 1
            if player_move.lower() == "scissor":
                print(f"Computer Wins! {start.name} loses ;(")
            print(f"score is {score}")
            game()

        # if computer choose Paper

        if pc_move == "Paper":
            time.sleep(1)
            if player_move.lower() == "scissor":
                print(f"{start.name} wins! No machine can beat him!")
                score += 1
            if player_move.lower() == "rock":
               print(f"Computer Wins! {start.name} loses")
            print(f"score is {score}")
            game()

        # if computer choose Scissor

        if pc_move == "Scissor":
            time.sleep(1)
            if player_move.lower() == "rock":
                print(f"{start.name} wins! No machine can beat him!")
                score += 1
            if player_move.lower() == "paper":
                print(f"{start.name} was cutted! PC wins...")
            print(f"score is {score}")
            game()

# as you can see after the possible events functions there is a call to the "game()" function, this is made so you can choose
# Rock, Paper or Scissor every turn
# probably i could make that inside the loop without calling the funtion (i think in the actual state it is "recursive") but 
# i was to lazy to trie it