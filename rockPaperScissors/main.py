import random

def play():
  player = input("What's your choice? (r) Rock, (p) Paper or (s)Scissors?\n")
  computer = random.choice(['r','p','s'])
  print(f"{player} vs {computer}")
  if player == computer:
    print("It's a tie!")
  elif (player == 'p' and computer == 'r') \
    or (player == 'r' and computer == 's') \
    or (player == 's' and computer == 'p'):
    print("you won!")
  else:
    print("you lost")


    
play()