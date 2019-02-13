
import random

def makeBoard(board):
    # ftiaxnei pinaka

    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])

def PlayerLetter():
    # dialegeis gramma

    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Dialeje X h O')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def First():
    # seira
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def Winner(b, le):
    # dinei true an kapoios kerdise
    return ((b[1] == le and b[2] == le and b[3] == le) or
    (b[4] == le and b[5] == le and b[6] == le) or 
    (b[7] == le and b[8] == le and b[9] == le) or
    (b[1] == le and b[4] == le and b[7] == le) or
    (b[2] == le and b[5] == le and b[8] == le) or
    (b[3] == le and b[6] == le and b[9] == le) or
    (b[3] == le and b[5] == le and b[7] == le) or
    (b[1] == le and b[5] == le and b[9] == le))

def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('Poia 8a einai h epomenh sou kinhsh? (1-9)')
        move = input()
    return int(move)

def chooseRMove(board):
    possibleMoves = []
    for i in (1, 2, 3, 4,5 ,6 ,7 ,8 ,9):
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    return chooseRMove(board)

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


while True:
    # adoiazei ton pinaka
    theBoard = [' '] * 10
    playerLetter, computerLetter = PlayerLetter()
    turn = First()
    print('To ' + turn + ' paizei prwto')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            makeBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if Winner(theBoard, playerLetter):
                makeBoard(theBoard)
                print('Kerdises')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    makeBoard(theBoard)
                    print('To paixnidi einai isopalia')
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if Winner(theBoard, computerLetter):
                makeBoard(theBoard)
                print('Mpravo kataferes na xaseis apo ena programma pou apla epilegei tyxaies 8eseis')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    makeBoard(theBoard)
                    print('To paixnidi einai isopalia')
                    break
                else:
                    turn = 'player'

    print('8es na janapaijeis ? (nai h oxi)')
    if not input().lower().startswith('n'):
        break
