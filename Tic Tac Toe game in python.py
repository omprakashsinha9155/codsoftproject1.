# Tic Tac Toe game in python

#Creating a game

board = [' ' for x in range(10)]

# insertLetter()
# This function is going to take two parameters: letter & pos. It is simply going to insert the given letter at the given position.

def insertLetter(letter, pos):
    board[pos] = letter

# SpacelsFree(pos)
# This function will simply tell us if the given space is free. Meaning it does not already contain a letter. It has one parameter, pos, which will be an integer from 1-9.

def spaceIsFree(pos):
    return board[pos] == ' '

# printBord(board)
# This function takes the board as a parameter and will display it to the console.

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# isWinner()
# This function will tell us if the given letter has won based on the current board. It has two parameters: bo(board) & le(letter). The letter must be a “X” or an “O”. We will simply check each possible winning line on the board and see if it is populated by the given letter.

def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

# playerMove()
# In this function we will be asking the user to input a move and validating it. If the move is valid we will add that letter to the board. Otherwise we will continue to ask the user for input.

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

# compMove()
# Now time for the AI! This function will be responsible for making the computers move. It will examine the board and determine which move is the best to make. The algorithm we will follow to do this is listed below.
# If the current step cannot be completed proceed to the next.
# If there is a winning move take it.
# If the player has a possible winning move on their next turn move into that position.
# Take any one of the corners. If more than one is available randomly decide.
# Take the center position.
# Take one of the edges. If more than one is available randomly decide.
# If no move is possible the game is a tie.
# def compMove():
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

# selectRandom()
# This function will randomly decide on a move to take given a list of possible positions.

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

# isBoardFull()
# This function takes board as parameter and will simply return True if the board is full and False if it is not.

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

# main()
# This function is what we will call to start the game. It will be calling all of the different functions in our program and dictate the flow of the program.

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

# Starting the Game
# Now that we have all our functions completed all that’s left to do is start the game. If we just wanted to run the game once all we would have to do is call main. However, in our case we want the game to keep running until the user doesn’t want to play anymore, so we will create a small while loop in the main line.

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break


