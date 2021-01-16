import menu
from time import sleep

# this is the help() function, it contains just the basic game rules for now

def help():
    print("-" * 50)
    print("Rules:\n1. Rock crushes Scissor, \n2. Scissor cuts Paper, \n3. Paper covers Rock.")
    print("You can go back to menu typing MENU, or view all the hints with HINTS")
    print("-" * 50)

    go_back = str(input("Go back? "))

    if go_back.lower() == "hints":
        for hint in menu.HINTS:
            print(hint)
            sleep(1)
        help()
            
    if go_back.lower() == "menu":
        menu.menu()