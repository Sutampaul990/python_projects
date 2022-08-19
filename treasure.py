from pickle import NONE


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

s1=input("You're at a cross word. Where do you want to go? Type "+'"left"' +" or "+'"right"\n')
if s1=="left":
  s2=input("You come to a lake.There is an island in the middle of the lake.Type "+'"wait"'+" to wait for a boat. Type "+'"swim"'+" to swim across\n")
  if s2=="wait":
    s3=input("You arrive at the island unharmed. There is a house of three door. One red, One yellow and one blue. Which colour do you choose?\n")
    if s3=="red":
      print("You are burned by fire.\nGame Over.")
    elif s3=="yellow":
      print("You get the treasure.\nYou win the game.")
    elif s3=="blue":
      print("You enter a room of beasts.\nGame Over.")
    else:
      print("Invalid Door")
  else:
    print("You are attacked by trout.\nGame Over.")
else:
  print("You fall into a hole.\nGame Over.")
      
      