
import random
from higher_lower_game_data import data,logo,vs
from replit import clear

def generate():
  """Get data from random account"""
  return random.choice(data)

def printable(account):
  """Format account into printable format: name, description and country"""
  name=account["name"]
  description=account["description"]
  country=account["country"]
  return (f"{name}, a {description}, from {country}.")

# guess=input("Who has more followers? Type 'A' or 'B' : ")

def compare(guess,A_follwers,B_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if(A_follwers>B_followers):
    return guess == "A"
  else:
    return guess == "B"

def game():
  print(logo)
  score=0
  game_should_continue=True
  
  account_a=generate()
  account_b=generate()

  while (game_should_continue) :
    account_a=account_b
    account_b=generate()
    while(account_a==account_b):
      account_b=generate()
        
    print(f"Compare A: {printable(account_a)}.")
    print(vs)
    print(f"Against B: {printable(account_b)}.")

    guess=input("Who has more followers? Type 'A' or 'B' : ")
    A_followers=account_a["follower_count"]
    B_followers=account_b["follower_count"]
    is_correct=compare(guess,A_followers,B_followers)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()