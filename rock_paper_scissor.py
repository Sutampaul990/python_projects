import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
a=["rock","paper","scissors"]
s=int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors. \n"))
if(a[s]=="rock"):
    print(f"\n{rock}")
elif(a[s]=="paper"):
    print(f"{paper}")
elif(a[s]=="scissors"):
    print(f"{scissors}")
temp=random.randint(0,2)
comp=a[temp]
if(comp=="rock"):
    print(f"Computer chose : \n{rock}")
elif(comp=="paper"):
    print(f"Computer chose : \n{paper}")
else:
    print(f"Computer chose : \n{scissors}")

if(a[s]=="rock"):
    if(comp=="rock"):
        print("Draw Match")
    elif(comp=="paper"):
        print("You Lose")
    else:
        print("You Win")

if(a[s]=="paper"):
    if(comp=="rock"):
        print("You Win")
    elif(comp=="paper"):
        print("Draw Match")
    else:
        print("You Lose")
        
if(a[s]=="scissors"):
    if(comp=="rock"):
        print("You Lose")
    elif(comp=="paper"):
        print("You Win")
    else:
        print("Draw Match")
    
    