import random

def play_dice_game(rounds):
    print("Welcome to the roll the dice game! Let's roll with it!")

    player1_score = 0
    player2_score = 0

    for i in range(rounds):
        player1_value = random.randint(1, 6)
        player2_value = random.randint(1, 6)
        
        print(f"Player 1 rolled: {player1_value}")
        print(f"Player 2 rolled: {player2_value}")

        if player1_value > player2_value:
            print("Player 1 wins this round.")
            player1_score += 1
        elif player2_value > player1_value:
            print("Player 2 wins this round")
            player2_score += 1
        else:
            print("It's a draw")

        input("Press enter to continue.")  # Wait for user input to proceed.

    # Displaying the overall winner
    if player1_score > player2_score:
        print(f"Player 1 wins with {player1_score} to {player2_score}!")
    elif player2_score > player1_score:
        print(f"Player 2 wins with {player2_score} to {player1_score}!")
    else:
        print("It's a tie game!")

# Let's let the players choose how many rounds they want to play
try:
    rounds = int(input("How many rounds do you want to play? "))
    play_dice_game(rounds)
except ValueError:
    print("Please enter a valid number of rounds.")
