import start
import random
import menu

t = ["Rock", "Paper", "Scissor"]

def game():

    player_move = str(input("What's your move? "))
    pc_move = random.choice(t)

    run = True
    while run:

        if player_move.lower() == pc_move.lower():
            print("Tie!")
            game()
    
        if pc_move == "Rock":
            if player_move.lower() == "paper":
                print(f"{start.name} wins! No machine can beat him!")
            if player_move.lower() == "scissor":
                print(f"Computer Wins! {start.name} loses ;(")
            game()

        if pc_move == "Paper":
            if player_move.lower() == "rock":
                print(f"Computer Wins! {start.name} loses ;(")
            if player_move.lower() == "scissor":
                print(f"{start.name} wins! No machine can beat him!")
            game()

        if pc_move == "Scissor":
            if player_move.lower() == "rock":
                print(f"{start.name} wins! No machine can beat him!")
            if player_move.lower() == "paper":
                print(f"{start.name} was cutted! PC wins...")
            game()

        if player_move.lower() == "menu":
            run = False
            menu.menu()