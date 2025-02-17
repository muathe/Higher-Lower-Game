from game_data import data
import random
from art import logo, vs
from replit import clear
print(logo)


def call_random():
  return random.choice(data)

def format_data(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name} a {account_description} is from {account_country}"

def follower_count(guess, followers_a, followers_b):
  if followers_a > followers_b:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print("Who has a higher follower count?")
  score = 0
  game_over = False
  account_a = call_random()
  account_b = call_random()
  
  while game_over == False:
    
    account_a = account_b
    account_b = call_random()

    while account_a == account_b:
      account_b = call_random()

    
    print(f"{format_data(account_a)}")
    print (vs)
    print(f"{format_data(account_b)}")
    
    guess = input("Please enter 'A' or 'B':   ").lower()
    
    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]
    
    compare = follower_count(guess, followers_a, followers_b)
    clear()
    
    if compare:
      score += 1
      print(f"Nice, your score is now {score}")
    else:
      game_over = True
      print(f"Sorry you lose, Final score:  {score}")

game()
  
  
# cell 19




