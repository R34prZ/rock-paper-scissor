import menu
    
while True:
    print("-" * 50)
    print("\t\tHello, wanna play?")
    print("\t\t1 for YES 0 for NO")
    print("-" *50)
    game = input("Play? ")

    if game == "1":
        menu.menu()
    
    elif game == "0":
        print("It's sad too say goodbye ;(")
        break