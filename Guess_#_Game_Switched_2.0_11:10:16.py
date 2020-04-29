import time
import random

print('Welcome to the Guess My Number game: 2.0!\n')
time.sleep(2)
print('Yes, I\'m back.')
time.sleep(3)
skip = input('If you don\'t know how to play THIS game, reply "Tell me".\n'
             'Otherwise, reply "Skip". ')

while (skip != 'Tell me' and skip != 'Skip' and skip != 'tell me' and skip != 'skip'):
    skip = input('Either "Skip" or "Tell me".Not that difficult. ')
if skip == 'Tell me'or skip == 'tell me':
    print('\nThis time, we switch places.')
    time.sleep(2)
    print('I try and guess a whole number that you think of.\n')
    time.sleep(3)
    print('And for an extra challenge...')
    time.sleep(1)
    print('(For ME, not you, pipe down already.)\n')
    time.sleep(2)
    print('You pick the maximum number in the range I can choose from.\n'
      'The lowest number is always 0. For example, 0 to 100, 0 to 1000,\n'
      'or even 0 to 1000000000000000000000000000000000000000000000000000.')
    time.sleep(5)
    print('But for both our sakes, don\'t do that last one.\n')
    time.sleep(2)
    print('Also, you can bet on the maximum number of tries '
      'it takes me\nto guess your number. I know the shiny buttons'
      ' on the keyboard are\nhard to resist, but try to not go too crazy.')
      
    time.sleep(6)
    
elif skip == 'Skip' or skip == 'skip':
    time.sleep(2)
    
high = int(input('\nWhat would you like the maximum number to be? '))

while high < 11:
    if high < 1:
        high = int(input('Simple math, human. A maximum cannot equal the minimum,\n'
                         'or be less than it. Do it again. '))
    else:
        high = int(input('Too easy. I\'m smarter than the average rock, you know.'
                         'Do it again. '))
        
unused = int(input('\nOkay. Enter your secret number here: '))
while unused >= high or unused < 0:
    unused = int(input('Nice try. Do it again. '))
    
bet = int(input('\nHow many tries do you bet it will take me\n'
                'to guess your number, maximum? '))
while bet < 1 or bet >= 100:
    if bet < 1:
          bet = int(input('Seriously? Do. It. Again. Properly this time. '))
    else:
          bet = int(input('Wow. Your expectations for me are reassuring. Try something\n'
                          'reasonable this time. '))

    
print('\nDon\'t worry, I didn\'t peek at your number.\n')
y = int(high/2)
low = 0
print('My first guess is',y,'.')
tries = 1

advice = input('Too high, too low, or correct? ')

while y != unused and advice != 'correct':
    if advice == 'too high':
        high = y
        y = int((high + low)/2) 
        print('How about',y,'?')
        tries += 1
    elif advice == 'too low':
        low = y
        y = int((high + low)/2)
        print('How about',y,'?')
        tries += 1
    elif advice != 'too high' and advice != 'too low':
        print('Type it right, human! Either too high, too low, or correct.\n'
              'Case sensitive.')
    advice = input('Too high, too low, or correct? ')

if y == unused and advice != 'correct':
    time.sleep(1)
    print('\nWow. Sore loser.')
    time.sleep(1.5)
elif y ==unused and advice == 'correct':
    time.sleep(1.5)

if tries == 1:
    print('\nI got it on my first try. Try being more creative, human.')
    
elif tries < bet:
    time.sleep(2)
    print('\nI got it in only',tries,'tries!')
    time.sleep(1.5)
    print('Which is less than',bet,'.')
    time.sleep(1.5)
    print('Which means you owe me a virus scan and a processor upgrade. I win!')
    
else:
    time.sleep(2)
    print('\nHmmmpphh. You win the bet. But to be fair, your parameters were\n'
          'ridiculous.')
time.sleep(2)
input('\n\nPress any key to exit.')

