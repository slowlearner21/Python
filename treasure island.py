print("Welcome to the treasure island. Your mission is to find the treasure")

#directions
choice1 = input("You\'re at a crossroad where do you want to go. choose 'Left' or 'Right'").lower()
if choice1 == "left":
    print("Youve moved on to the next stage")
    choice2 = input("you\'re safe now choose the next move. do you want to 'swim' or 'wait' ").lower()
        
    if choice2 == "wait":
        print("You've moved on to the next stage.")
        choice3 = input("Now you\'ve to chose a door 'Blue' or 'Yellow' or 'Red'.Choose one ").lower()
        
    if choice3 == "yellow":
                print("You win. Congratulations")
    if choice3 == "red":
                print("Game over. You died")
    if choice3 == "blue":
                print("Game over. You died")
    else:
        print("Choice not read. Kindly choose from the provided options ")
else:
    print("command not read.")