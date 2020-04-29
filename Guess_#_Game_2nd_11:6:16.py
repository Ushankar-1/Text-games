import time
import random

print('Welcome to the "Guess My Number" game!\n')
time.sleep(3)
print('I am your artificially intellgent, computer-controlled opponent.')
time.sleep(3)
print('I\'m not used in most games due to some... errr... personality issues.\n\n')
time.sleep(4)
print('Never mind that. Anyways, I\'m thinking of a number between or\n'
      'including 1 and 100. Try to guess it in as few attempts as possible.\n')

number = random.randint(1,1)
guess = int(input('Take a guess: '))
attempts = 1
while guess != number:
    if guess < number:
            print('Higher...')
    if guess > number:
            print('Lower...')
    guess = int(input('Take a guess: '))
    attempts += 1

time.sleep(3)
print('\nCongratulations!\n')
time.sleep(3)
if attempts != 1:
    print('You guessed the number in',attempts,'tries.\n')
    time.sleep(3)
    print('Good job! We\'re all proud of you, so sit back and enjoy your victory.')
    time.sleep(3)
    print('\nNot.')
    time.sleep(4)
    print('\nThat was the warm up.')
elif attempts == 1:
    print('You guessed the number in',attempts,'try! You must be very lucky.')
    time.sleep(2)
    print('Let\'s test that.\n')
time.sleep(2)
print('Time for level numero uno: one number in one thousand.')
time.sleep(2)
print('Good luck.\n')
time.sleep(2)

NUMBER = random.randint(1,1)
GUESS = int(input('Take a guess: '))
ATTEMPTS = 1
while GUESS != NUMBER:
    if GUESS < NUMBER:
            print('Higher...')
    if GUESS > NUMBER:
            print('Lower...')
    GUESS = int(input('Take a guess: '))
    ATTEMPTS += 1
time.sleep(2)

print('\nAwwwwww... you actually did it.\n')
time.sleep(3)
if ATTEMPTS != 1:
    print('Whatever. It took you',ATTEMPTS,'tries.')
elif attempts == 1 and ATTEMPTS == 1:
    print('So you managed to pull it off again. Big deal.')
elif ATTEMPTS == 1:
    print('Whatever. So it only took you one try. Big deal.')   
time.sleep(3)
print('\nThis was really easy anyways.')
time.sleep(4)
print('\n*hmmpphh*.')
time.sleep(3)
print('\nLevel two: Ten Thousand!')
time.sleep(3)
print('You do know that statistically, you have a 1% chance of winning\n'
      'within 100 tries, right?\n')

time.sleep(2)
NUMBE = random.randint(1,1)
GUES = int(input('Take a guess: '))
ATTEMPT = 1
while GUES != NUMBE:
    if GUES < NUMBE:
            print('Higher...')
    if GUES > NUMBE:
            print('Lower...')
    GUES = int(input('Take a guess: '))
    ATTEMPT += 1

time.sleep(2)
if attempts == 1 and ATTEMPTS == 1 and ATTEMPT == 1:
    print('\nAs usual, you took the odds and threw them back in its face.\n'
          'How rude of you. Just what did those odds ever do to you?')
    time.sleep(5)
    print('\nJust so you know, you\'ll have a harder time doing that with this\n'
          'next level.')
    time.sleep(3)
    print('\nIt has 100,000 options. And you have 15 tries.\nGood luck.\n')
elif ATTEMPT == 1:
    print('How cute. It\'s almost like you think I don\'t know you''re cheating.')
    time.sleep(3)
    print('(You are cheating, right? RIGHT?!?)')
    time.sleep(3)
    print('For level 3, you will have 100,000 options and 15 tries.\n'
          'Good luck. You\'ll need it.\n')
elif ATTEMPT <= 100:
    print('So you managed to beat the odds.',ATTEMPT,'tries.')
    time.sleep(3)
    print('You now have 15 tries to complete the next level.'
          '\nAnd 100,000 options. Have fun!\n')
else:
    print(ATTEMPT,'tries.',ATTEMPT,'.')
    time.sleep(3)
    print('Okay, NOW I want to see how you do with 15 tries -\n')
    time.sleep(1)
    print('- and one hundred thousand options!\n')

time.sleep(2)
NUM = random.randint(1,1)
GU = int(input('Take a guess: '))
ATTEM = 1
while GU != NUM:
    if GU < NUM:
            print('Higher...')
    if GU > NUM:
            print('Lower...')
    GU = int(input('Take a guess: '))
    ATTEM += 1

time.sleep(2)
if attempts == 1 and ATTEMPTS == 1 and ATTEMPT == 1 and ATTEM == 1:
    print('Remember how I implied earlier that getting everything in one try was\n'
          'a big deal? Well, it\'s not.\n')
    time.sleep(3)
    print('Plenty of people have done it before.')
    time.sleep(2)
    print('For example, [INSERT RIVAL\'S NAME HERE] has done it at least 20 times.\n')
    time.sleep(6)
    print('That wasn\'t supposed to give you an incentive, by the way.\n')
    time.sleep(3)
    print('Just so you know.\n')
    time.sleep(2)
elif ATTEM == 1:
    print('So you actually made it in one try. I suppose that the odds have to\n'
          'cave in at some point.\n')
elif ATTEM <= 15:
    print('So you actually made my bet.',ATTEM,'tries.\n')
else:
    print('Hmmmm. So you could only do it in',ATTEM,'tries\n.')
time.sleep(3)
print('Moving on. Level four, 1,000,000!\n')
time.sleep(2)
print('And if you get THIS one in twenty or less tries, I will seriously blow a fuse.\n')

NUMB = random.randint(1,1)
GUE = int(input('Take a guess: '))
ATTEMP = 1
while GUE != NUMB:
    if GUE < NUMB:
            print('Higher...')
    if GUE > NUMB:
            print('Lower...')
    GUE = int(input('Take a guess: '))
    ATTEMP += 1
    
if ATTEMP == 1:
    time.sleep(4)
    print('\nOne in a million.')
    time.sleep(4)
    print('\nONE IN A MILLION.')
    time.sleep(3)
    if attempts == 1 and ATTEMPTS == 1 and ATTEMPT == 1 and ATTEM == 1:
        print('\nTHIS')
        time.sleep(2)
        print('\n//AGAIN//')
        time.sleep(3)
    print('\nAAARRRRGGGHHH I SWEAR I\'M GOING TO')
    time.sleep(1)
    print('*fizzle*')
    time.sleep(3)
    print('\n...')
    print('\n')
    time.sleep(6)
    print('\n\nError Code 19: Processor overload.')
    time.sleep(1.5)
    print('Please consult a computer technician for assistance.\n\n\n')
    
elif ATTEMP <= 20:
    time.sleep(3)
    print('*sizzle*')
    time.sleep(3)
    print('*pop*')
    time.sleep(2)
    print(ATTEMP,'guesses.')
    time.sleep(3)
    print('A 3-Gigahertz processor and 256GB RAM,'
          'and I\'m beaten by a primate.')
          
else:
    print('Well, at least you tried.',ATTEMP,'times.')
    time.sleep(2)
    print('I\'m actually pretty impressed that you finished this game.')
    time.sleep(2)
    print('Which is sad, because I\'m the computer.')






            

            





       
       
       



