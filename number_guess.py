import random

def play_game():
    player_name = input("Hello, What's your name?")
    print('Okay, ' + player_name)

    difficulty = input("Choose a difficulty (Easy/Medium/Hard): ").lower()
    if difficulty == "easy":
        upper_limit = 10
        max_guesses = 5
    elif difficulty == "medium":
        upper_limit = 20
        max_guesses = 4
    elif difficulty == "hard":
        upper_limit = 50
        max_guesses = 3
    else:
        print("Invalid choice, setting to Easy by default.")
        upper_limit = 10
        max_guesses = 5

    number = random.randint(1, upper_limit)
    number_of_guesses = 0

    print(f'I am guessing a number between 1 and {upper_limit}:')

    while number_of_guesses < max_guesses:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= upper_limit:
                number_of_guesses += 1
                if guess < number:
                    print('Your guess is too low')
                elif guess > number:
                    print('Your guess is too high')
                else:
                    break
            else:
                print(f"Please guess a number between 1 and {upper_limit}.")
        except ValueError:
            print("Please enter a valid number.")

    if guess == number:
        print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('You did not guess the number, The number was ' + str(number))

while True:
    play_game()
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        break
