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

first_step=input('You are at a crossroad, where do u want to go? type "left" or "right".\n')
if first_step=="left":
  second_step=input('You\ve come to a lake, type "wait" to wait for a boat or type "swim" to swim across \n')
  if second_step=="wait":
    third_step=input('You arrived at the island, there is a house with three colour doors.Type "red" or "yellow" or "blue".\n')
    if third_step=="red":
      print("its a room full of fire,Game over")
    elif third_step=="blue":
      print("You entered a room of beasts,Game Over")
    elif third_step=="yellow":
      print("You found the treasure..!You Win")
    else:
      print("You chosed a door that does'nt exist,Game Over")
  else:
    print("You got attack ,Game Over")
else:
  print("You fell into a hole,Game Over")



