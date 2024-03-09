print('''
 *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* 
''')
print("Welcome to treasure island are you ready for the game? let's go!")
# taking converting it to lower case
direction = input('You\'re at a crossroad,where do you want to go ? type left or right?').lower()
if direction == "right":
    print("You fell into a hole. Game over.")

else:
    print("Good choice keep walking\n")
    lake_wait = input("You end up in front of the lake. Are you waiting for a boat or do you swim? \n"
          "type wait or swim? ").lower()

    if lake_wait == "swim":
        print("A hungry crocodile ate you. Game over!")
    else:
        print(" A white boat with a fisherman just came to give you a lift to the island \n")
        doors = input("You are on the island now. you have the choice between 3 doors \n"
                      "Red, Blue or Yellow? ").lower()
        if doors == "yellow":
            print("Congratulations, the treasure of Greed Island is all yours")
        elif doors == "red":
            print(" This door brings you back to the beginning of the story. Start over! ")
        else:
            print("A monster ate your brain. Game over MUHAHAHAHAHAH!!!")

