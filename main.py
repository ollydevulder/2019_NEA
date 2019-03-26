import classes
from random import shuffle, randint
from time import sleep
from platform import system as sys
from os import system

def clear(t=0):
    sleep(t)
    try:
        if sys() in ['Linux', 'Darwin']:
            system('clear')
        else:
            system('cls')
    except:
        print('\n'*50)

def options(o, msg):
    ui = -1
    a = len(o)
    while int(ui) not in range(a):
        if type(msg) == str: print(msg)
        else: msg()
        for i in range(a):
            print('[{}] {}'.format(i, o[i]))
        ui = input('#~> ')
        try:
            int(ui)
        except:
            ui = -1
            print('Please enter an integer!')
            clear(0.7)
        clear()
    return int(ui)

def evaluate(f, r):
    ui = False
    while not ui or not f(ui):
        print(r)
        ui = input('#~> ')
        clear()
    return ui

def card_check(n):
    try: n = int(n)
    except: return False
    return n%2==0 and n>=4 and n<=30

def get_cards(f_name='./dogs.txt'):
    with open(f_name) as f:
        names = f.read().split('\n') # read file and split it by lines
    return [classes.card(name) for name in names] # return a list of card classes with names from file

def game():
    global cards
    clear()
    print('Welcome to Celebrity Dogs!')
    choice = options(['Play', 'Help', 'Exit'], 'What do you want to do?')
    if choice == 2: # let the player break the game loop
        return False
    elif choice == 1:
        clear()
        print('\tHelp\n')
        print(classes.HELP_MSG)
        input('\n\tPress enter to return to the main menu...')
        return True
    print('Okay! How many cards shall we play with?')
    n_cards = int(evaluate(card_check, 'Enter an even number between 4 and 30.'))
    shuffle(cards)           # shuffle cards
    deck = cards[:n_cards]   # load the required amount
    user = deck[:n_cards//2] # split for user..
    comp = deck[n_cards//2:] # ..and for computer

    userTurn = True
    roundCounter = 0
    while len(user)>0 and len(comp)>0:
        clear()
        roundCounter+=1
        print('ROUND #{}'.format(roundCounter))
        print('User {} - Computer {}'.format(len(user), len(comp)))

        clear(1.5)
        # either get user to choose category for the round or choose it randomly (for the computer)
        category = options(['ex', 'in', 'fr', 'dr'], user[0].display) if userTurn else randint(0,3) 
        clear(0.7)
        print('USER')
        user[0].display(category)
        print('COMPUTER')
        comp[0].display(category)

        userScore, compScore = user[0].attrs[category], comp[0].attrs[category]
        userTurn = userScore <= compScore if category == 3 else userScore >= compScore # if user won it stays their turn
        diff = abs(userScore-compScore)

        # swap the winners first and last card
        # then pop the losers first card to the back of winners deck

        if userTurn:
            print('User wins by {}.'.format(diff if diff!=0 else 'default'))
            user[0], user[-1] = user[-1], user[0]
            user.append(comp.pop(0))
        else:
            print('Computer wins by {}.'.format(diff))
            comp[0], comp[-1] = comp[-1], comp[0]
            comp.append(user.pop(0))

        input('Press enter to continue...')
    clear()
    print('After {} rounds, {} won!'.format(roundCounter, 'Computer' if len(user) == 0 else 'User'))
    input('Press enter to continue...')
    return True 

if __name__=='__main__':
    cards = get_cards()
    while True:
        if not game(): break
    print('Thanks for playing, Goodbye!')
    clear(1)
    exit()
