import start
import help
import score
from random import choice
from time import sleep

# and here it is! The menu() function, it's the "center" of all this little game
# here i manage some events and "navigate" through game options, excpet it's not that interesting and complicated

def menu():

    # so i'm also defining the score variable here in order to try to save the score even after quiting to the menu

    print("-" * 50)
    print("Nice! You can choose:")
    print("HELP, START, QUIT, SCORE")
    print("-" * 50)

    global HINTS
    HINTS = ["If you type anything other than Y or N in game you can continue playing.",
             "Don't underestimate the computer...it starts with ties...",
             "I don't really know how to make a good score option lol",
             "I made a score thingy hehe boi",
             "You can type MENU to go back to the...ãhhh...menu? ",
             "Actually typing MENU doesn't really work lol",
             "Don't use the score option before setting a name",
             "You can type the commands in lower case",
             "Actually, the menu command now works hehe"
            ]

    p_choice = str(input("What you choose? "))

    if p_choice.lower() == "help":
        help.help()

    elif p_choice.lower() == "start":
        print("HINT:" + " " + choice(HINTS))
        start.start()

    elif p_choice.lower() == "quit":
        print("Quitting to main panel...") 
        print("HINT:" + " " + choice(HINTS))
        sleep(0.5)

    
    elif p_choice.lower() == "score":
        if score.player_score > 0:
            print("Ok computing the score...")
            sleep(1)
            print(f"{start.name} score is {score.player_score}")
            print("Going back to menu...")
            sleep(1)
            menu()
        else:
            print("You don't have a score yet, try that after playing!")
            sleep(0.5)
            print("Going back to menu...")
            sleep(0.5)
            menu()