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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
if choice != "left":
    print("You fell into a hole. \nGame Over")
    raise SystemExit
choice = input("You're standing in front of wide river. What is your choice? Type \"wait\" or \"swim\"\n" )
if choice != "wait":
    print("You were attacked by big trout. \nGame Over")
    raise SystemExit
choice = input("While you wait you spot forest hut with 3 doors. Which doors will you choose? Type \"red\", \"blue\" or \"yellow\"\n" )
if choice =="red":
    print("You were burned by fire. \nGame Over")
elif choice == "blue":
    print("You were eaten by wild beasts. \nGame Over")
elif choice =="yellow":
    print("You found a treasure. \nYou Win!")
else: 
    print("Game Over.")    