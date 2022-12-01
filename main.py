print("ROCK, PAPER, SCISSORS")
print()
from getpass import getpass as input

player_1 = input("Enter your move R , P, or S:")
player_2 = input("Enter your move R,P, or S:")


if player_1  == player_2:
    print(f"Both players selected It's a tie!")

elif player_1 == "r":
    if player_2 == "s":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player_1 == "p":
    if player_2 == "r":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player_1 == "s":
    if player_2 == "p":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
  
