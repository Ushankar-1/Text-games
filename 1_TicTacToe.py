import time
import random

#Pseudocode:

# Print instructions
# See who goes first (Random pick, maybe a little coin toss thing)
# establish alternating turn system
#
# First, check for winning combinations.
#   If winning combination of computer moves:
#       Print "I win! In your face, ugly primate" message.
#   If winning combination of human moves:
#       Print "You're a lame donut." message.
#
# Second, check if there are no empty spaces left.
#   If true: 
#       Print "It's a tie, and you suck" message.
#
# WHILE false:
# If human move:
#   register move and update board
#
# If computer move:
#   1. Check if there is move that lets computer win this turn
#       If true:
#           occupy that space
#       If true, and multiple values:
#           screw it. pick one at random
#   2. Check if there is move that will let human win next turn
#       If true:
#           occupy that space
#       If true, and multiple values:
#           screw it. pick one at random
#   3. Check if center space is open
#       If true:
#           occupy that space
#   4. Check if diagonal spaces are open
#       if true:
#           occupy it.
#       If true, with multiple values:
#           Pick one adjacent to human-occupied space.
#   5. (Only the side spaces are left.) Pick a square at random
#           Also, sorry computer, but you are doomed.

import time
import random


X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'TIE'
NUM_SQUARES = 9
humansymbol = X
computersymbol = O

def oh_come_on():
    ''' Prints REGULAR game instructions. '''
    
    time.sleep(2)
    print('\nWow. That\'s sad.\n')
    time.sleep(4)
    print('Basically, there\'s a grid, 2 lines by 2 lines, like a hashtag.\n'
          'There are 9 spaces in between the lines.\n')
    time.sleep(6)
    print('The two people (or computers) playing each pick a symbol: "X" or "O".\n')
    time.sleep(6)
    print('One person goes first, and they alternate turns.\n')
    time.sleep(6)
    print('The game ends when either there are no empty spaces left, or one\n'
          'player has three of their symbols in a straight line.')
    time.sleep(7)
    print('That means horizontally, vertically, or diagonally.\n')
    time.sleep(6)
    print('The player with three of their symbols in a straight line wins.')
    time.sleep(8)

def instruction_1():
    ''' Fairly self-explanatory. '''
    
    print('I\'m assuming you already know how to play Tic-Tac-Toe.\n')
    time.sleep(2)
    really = input('If you do, reply "Yes". If by some miracle you don\'t,\n'
                   'reply "No". Also, if you don\'t, God help you. ')
    
    while really != 'Yes' and really != 'yes' and really != 'No' and really != 'no':
        time.sleep(1)
        really = input('\nForget about not knowing how to play Tic-Tac-Toe, God help you\n'
                       'if you can\'t even spell "Yes" or "No" right! Try again. ')

    if really == 'No' or really == 'no':
        oh_come_on()

    time.sleep(2)

    print(
'''

Since we don\'t have a physical board, this is going to be a bit different.

This is our board:
                    0 | 1 | 2
                   -----------
                    3 | 4 | 5
                   -----------
                    6 | 7 | 8

You\'ll make a move by choosing one of
the above numbers to place your symbol.

Which you\'ll be choosing now.
   
''')

def instruction_2():
    '''Part two'''
    
    time.sleep(4)
    symbol = input('Do you want to be "X" or "O"? ')
    while symbol != 'X' and symbol != 'x' and symbol != 'O' and symbol != 'o':
        time.sleep(1)
        symbol = input('Either "X" or "O". I know computers are better with binary\n'
                       'values, but seriously? Try again. ')
        
    if symbol == 'X' or symbol == 'x':
        time.sleep(1)
        symbol == X
        computersymbol = 'O'
        print('Oh. You picked "X". As in the Roman numeral for 10. \n'
              'Which you are on the Ph scale,\n\'cause child, you '
              'basic.')
        time.sleep(4)
        print('\nI\'ll be "O".')
        
    if symbol == 'O' or symbol == 'o':
        time.sleep(1)
        symbol == O
        computersymbol = 'X'
        print('Hmmmm. You picked "O". As in "0". As in what your score will be.')
        time.sleep(3)
        print('\nI\'ll be "X".')

def instruction_3():
    '''Part 3'''

    time.sleep(2)

    print('\nI\'ll toss a coin to decide who goes first.')
    flipguess = input('Heads or tails? ')
    
    while flipguess != 'Heads' and flipguess != 'heads' and flipguess != 'Tails' and flipguess != 'tails':
        flipguess = input('BEEEEP! Wrong answer. Try again. ')

    coin = random.randint(0,1)
    heads = 1
    tails = 0

    time.sleep(2)

    if flipguess == 'Heads' or flipguess == 'heads':
        flipguess = 1
    if flipguess == 'Tails' or flipguess == 'tails':
        flipguess = 0
    
    if coin == heads:
        print('It\'s Heads.')
    else:
        print('It\'s Tails.')
        
    time.sleep(2)
    
    if flipguess == coin:
        print('Take the first turn. You\'ll need it.')
        return h1
    else:
        print('Ha! I go first!')
        return c1
    time.sleep(2)
    print('Let\'s start:')

def instruction():
    instruction_1()
    instruction_2()
    instruction_3()

def new_board():
    ''' Creates new Game Board '''
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    ''' Prints Game Board '''
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t-----------')
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t-----------')
    print('\t', board[6], '|', board[7], '|', board[8])

#def legal_moves(board):
#    ''' Finds legal moves '''
#    possible_moves = []
#    for square in range(NUM_SQUARES):
#        if board[square] == EMPTY:
#           possible_moves.append(square)
#    return possible_moves
            
def winner(board):
    ''' Determine the game winner '''
    WAYS_2_WIN = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for row in WAYS_2_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[1]]
            return winner
        if EMPTY not in board:
            return TIE

      
def humanmove(board):
    mymove = int(input('Which space do you want to occupy? '))
    while mymove < 0 or mymove > 8 or board[mymove] != EMPTY:
        if mymove < 0 or mymove > 8:
            if mymove > 8:
                mymove = int(input('The spaces are numbered from 0 to 8. Not more. Not less. Pick again. '))
            if mymove < 0:
               mymove = int(input('The spaces are numbered from 0 to 8. Not more. Not less. Pick again. '))                
        if board[mymove] == computersymbol:
            mymove = int(input('Nice try, but you can\'t write over my mark. Pick again. '))
        if board[mymove] == humansymbol:
            mymove = int(input('You can\'t pick the same spot twice. Try again. '))
    board[mymove] = humansymbol

instruction()
board = new_board()
display_board(board)
humanmove(board)


def apecomputermove(board):
    putermove = random.randrange(9)
    while board[putermove] != EMPTY:
        putermove = random.randrange(9)
    board[putermove] = computersymbol
