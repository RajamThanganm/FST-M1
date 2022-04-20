"""

    Make a two-player Rock-Paper-Scissors game.
    Remember the rules:
        Rock beats scissors
        Scissors beats paper
        Paper beats rock

"""
player1 = input("enter player 1 name")
player2 = input("enter player 2 name")

player1_choice = input("choose rock,paper or scissors for player1")
player2_choice = input("choose rock,paper or scissors for player2")

player1_choice_lower = str(player1_choice).lower()
print(player1_choice_lower)
player2_choice_lower = str(player2_choice).lower()
print(player2_choice_lower)

if player1_choice_lower == player2_choice_lower:
    print ("Its  a tie, Repeat the game")
elif player1_choice_lower == "rock":
    if player2_choice_lower == "paper":
        print("Paper beats rock") 
    elif player2_choice_lower == "scissors":
        print("Rock beats scissors")
elif player1_choice_lower == "paper":
    if player2_choice_lower == "rock":
       print("Paper beats rock") 
    elif player2_choice_lower == "scissors":
       print("Scissors beats paper")
elif player1_choice_lower == "scissors":
    if player2_choice_lower == "rock":
       print("Rock beats Scissor")
    elif player2_choice_lower == "paper":
       print("Scissors beats paper")

