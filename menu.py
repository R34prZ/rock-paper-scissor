import start
import help

def menu():
    print("-" * 50)
    print("Nice! You can choose:")
    print("HELP, START, QUIT")
    print("-" * 50)

    choice = str(input("What you choose? "))

    if choice.lower() == "help":
        help.help()

    elif choice.lower() == "start":
        start.start()

    elif choice.lower() == quit:
        print("Going back to menu...") 