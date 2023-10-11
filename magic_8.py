import random
import time

answers = [
    'It is certain', 'It is decidedly so', 'Without a doubt', 
    'Yes – definitely', 'You may rely on it', 'As I see it, yes', 
    'Most likely', 'Outlook good', 'Yes, signs point to yes', 
    'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 
    'Cannot predict now', 'Concentrate and ask again', 'Don’t count on it', 
    'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful'
]

def display_title():
    print('  __  __          _____ _____ _____    ___  ')
    print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
    print(' | \  / |  /  \ | |  __  | || |      | (_) |')
    print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
    print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
    print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
    print('')
    print('')
    print('')
    print('Hello World, I am the Magic 8 Ball, What is your name?')

def Magic8Ball():
    print('Ask me a question (type and press Enter):')
    question = input().strip()  # Removing any leading/trailing white spaces
    
    # Check if question is empty
    if not question:
        print("Looks like you didn't ask anything. Please ask a question!")
        return Magic8Ball()
    
    print("Thinking...")
    time.sleep(2)  # Pause for 2 seconds to simulate thinking
    print(answers[random.randint(0, len(answers)-1)])
    print('I hope that helped!')
    Replay()

def Replay():
    print('Do you have another question? [Y/N]')
    reply = input().strip().lower()
    
    if reply in ['y', 'yes']:
        Magic8Ball()
    elif reply in ['n', 'no']:
        print("Goodbye! Don't hesitate to return if you have more questions!")
        exit()
    else:
        print('I apologize, I did not catch that. Please repeat.')
        Replay()

display_title()
name = input().strip()
print('Hello, ' + name + "!")
Magic8Ball()
