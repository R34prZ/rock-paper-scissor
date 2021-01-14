import menu

def help():
    print("-" * 50)
    print("Rules:\nRock crushes Scissor, \nScissor cuts Paper, \nPaper covers Rock.")
    print("You can go back to menu typing MENU")
    print("-" * 50)

    go_back = str(input("Go back? "))
    if go_back.lower() == "menu":
        menu.menu()