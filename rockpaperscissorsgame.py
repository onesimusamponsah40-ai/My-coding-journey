import random

while True:
    game_round = 5
    player_score = 0
    computer_score = 0
    tie_score = 0
    while game_round > 0:
        
        computer_choice = random.choice(["ROCK","PAPER","SCISSORS"])
        player_choice = input("Rock,Paper or scissors: ").upper()
        print(computer_choice)
        if player_choice not in ("ROCK","PAPER","SCISSORS"):
            print("it has to be ROCK,PAPER,SCISSORS")
            continue
        game_round -= 1
        if player_choice == "ROCK" and computer_choice == "SCISSORS":
            print("You Win!")
            player_score += 1
        elif player_choice == "SCISSORS" and computer_choice == "PAPER":
            print("You Win!")
            player_score += 1
        elif player_choice == "PAPER" and computer_choice == "ROCK":
            print("You Win!")
            player_score += 1
        elif player_choice == computer_choice:
            print("It's a tie")
            tie_score += 1
        else:
            print("Bot Wins!")
            computer_score += 1
    print("player: ", player_score,"\n","Bot score: ", computer_score,"\n","ties: ", tie_score)
    if player_score > computer_score:
        print("Player wins!")
    elif player_score < computer_score:
        print("Bot wins")
    else:
        print("it's a tie")

    play_again = input("play again(y/n): ")
    if play_again.lower() != "y":
        print("Thank you for playing")
        break









