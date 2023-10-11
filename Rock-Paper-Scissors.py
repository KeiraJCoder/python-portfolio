from random import randint

# Create a list of play options
t = ["rock", "paper", "scissors"]

# Assign a random play to the computer
computer = t[randint(0, 2)]

# Set initial scores
player_score = 0
computer_score = 0

while True:
    # Get the player's choice
    player = input("Rock, Paper, Scissors? Or type 'exit' to end the game: ").lower()
    
    # Exit the game if the player types "exit"
    if player == "exit":
        print(f"Final Scores: Player: {player_score} | Computer: {computer_score}")
        break

    # Determine the outcome
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
            computer_score += 1
        else:
            print("You win!", player, "smashes", computer)
            player_score += 1
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cuts", player)
            computer_score += 1
        else:
            print("You win!", player, "covers", computer)
            player_score += 1
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
            computer_score += 1
        else:
            print("You win!", player, "cuts", computer)
            player_score += 1
    else:
        print("That's not a valid play. Check your spelling!")
        continue  # Continue to the next iteration without updating the computer's play

    # Display current scores
    print(f"Scores: Player: {player_score} | Computer: {computer_score}")
    
    # Reset the computer's play
    computer = t[randint(0, 2)]
