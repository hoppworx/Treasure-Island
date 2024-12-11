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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input('You\'ve arrived at a crossroad with badly damaged unreadable signs.  Which direction do you want to go? Type "left" or "right". \n').lower()
if choice1 == "left":
          print("You've arrived at a lake.  There is an island in the middle.")
          choice2 = input('Do you want to swim across or wait for a boat? Type "swim" or "wait". \n').lower()
          if choice2 == "swim":
                    print("A giant angry trout attacked you!  Game over.")
          else:
                    print("A boat arrived and safely takes you to the island.  At the center of the island is a house with 3 doors.  One red, one blue and one yellow.")
                    choice3 = input('Which door do you choose? Type "red", "blue", or "yellow". \n').lower()
                    if choice3 == "red":
                              print("The room is on fire and you're badly burned!  Game over.")
                    elif choice3 == "blue":
                              print("Giant beasts await you and make you their next DoorDash food order!  Game over.")
                    else:
                              print("You are immediately greeted with glowing light emerging from an open golden chest full of treasure!  You win!")
          
else:
          print("You fell into a hole!  Game over.")

         