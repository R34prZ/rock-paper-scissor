import start
import help
import random

# and here it is! The menu() function, it's the "center" of all this little game
# here i manage some events and "navigate" through game options, excpet it's not that interesting and complicated

def menu():
    print("-" * 50)
    print("Nice! You can choose:")
    print("HELP, START, QUIT")
    print("-" * 50)

    HINTS = ["If you type anything than Y or N in game you can continue playing.",
             "Don't underestimate the computer...it starts with ties...",
             "I don't really know how to make a good score option lol"
            ]

    choice = str(input("What you choose? "))

    if choice.lower() == "help":
        help.help()

    elif choice.lower() == "start":
        start.start()
        print(random.choice(HINTS))

    elif choice.lower() == "quit":
        print("Going back to menu...") 
        print(random.choice(HINTS))