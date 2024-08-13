import sys

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice = input("Where Do you go Left or Right?\n").lower()
coins = 0

if choice == "right":
    print("In life you are not always the right one!\n\n Game Over! \n")

if choice == "left":
    coins += 1
    print("""
    You found a coin!
    You are now facing a pond. This pond looks green for some reason. You also see bubble poping out of the pond.
    At the end of the pond you see a boat unloading passengers.
    You could Swim to cross the pond and save yourself a coin or you can Wait for the boat man.
        """)
    print(f"You have {coins} coins.")
    choice = input("What do you do? Swim? or Wait?\n").lower()

    if choice == "swim":
        print("""
    You start wlaking towards the middle of the pond slowly. 
    The water reached your waist.
    Then you see those bright green eyes looking at you underneath you.
    
    Game Over.
    
              """)
        sys.exit()
    if choice == "wait":
        coins -= 1
        print("""
You gave the boat man your only coin.
He helped you cross the pond.
              """)
        print("""
    After walking for a while you came a across a bridge.
    Weirdly there are three entries to this wooden bridge.
    Three color coated. Red, Blue and Yellew.\n""")
        choice = input("Which bridge do you choose? Red or Blue or Yellow?\n").lower()
        if choice == "red":
            print("What did you expect a red bridge be? Safe? LOL! \n\n Game Over! \n")
            sys.exit()
        elif choice == "blue":
            print("You started to cross the bridge. You hear a bird? o no! its a dragon! \n\n Game Over! \n")
        elif choice == "yellow":
            print("You successfully crossed the bridge. At the end of the bridge you met with your teacher. You won i guess! \n\n Game Over!\n")
        else:
            print("How can you miss the bridge thats right in front of you?\n\nGame Over!\n")