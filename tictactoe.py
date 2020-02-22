
#------------------------Empty tictactoe board--------------------------
def displayBoard(b):
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     0 | 1 | 2")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     3 | 4 | 5")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     6 | 7 | 8")
  print("\n")

#Check if any three consicutive row, colomn or a diagonal matches
def checkWin(b, m):
    return ((b[0] == m and b[1] == m and b[2] == m) or  # H top
            (b[3] == m and b[4] == m and b[5] == m) or  # H mid
            (b[6] == m and b[7] == m and b[8] == m) or  # H bot
            (b[0] == m and b[3] == m and b[6] == m) or  # V left
            (b[1] == m and b[4] == m and b[7] == m) or  # V centre
            (b[2] == m and b[5] == m and b[8] == m) or  # V right
            (b[0] == m and b[4] == m and b[8] == m) or  # LR diag
            (b[2] == m and b[4] == m and b[6] == m))  # RL diag

#Check if no match
def check_if_Draw(b):
    return ' ' not in b

# Make duplicate of the board for testing without affecting the actual board
def getBoardCopy(b):
    dupeBoard = []
    for j in b:
        dupeBoard.append(j)
    return dupeBoard

# b stands for the board
# mark is either 0 or X
# i to check for win
def testWinMove(b, mark, i):
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    return checkWin(bCopy, mark)


def testForkMove(b, mark, i):
    # Determines if a move opens up a fork
    bCopy = getBoardCopy(b)
    bCopy[i] = mark
    winningMoves = 0
    for j in range(0, 9):
        if testWinMove(bCopy, mark, j) and bCopy[j] == ' ':
            winningMoves += 1
    return winningMoves >= 2

# Generates responses after analizing
def getComputerMove(b):
    
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, 'X', i):
            return i
    
    for i in range(0, 9):
        if b[i] == ' ' and testWinMove(b, '0', i):
            return i
    
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, 'X', i):
            return i
    
    playerForks = 0
    for i in range(0, 9):
        if b[i] == ' ' and testForkMove(b, '0', i):
            playerForks += 1
            tempMove = i
    if playerForks == 1:
        return tempMove
    elif playerForks == 2:
        for j in [1, 3, 5, 7]:
            if b[j] == ' ':
                return j
    # Pick Center, corner or side
    if b[4] == ' ':
        return 4
    
    for i in [0, 2, 6, 8]:
        if b[i] == ' ':
            return i
    
    for i in [1, 3, 5, 7]:
        if b[i] == ' ':
            return i

# To keep the game running
Playing = True
while Playing:
    InGame = True
    board = [' '] * 9
    print('Would you like to go first or second? (1/2)')
    if input() == '1':
        playerMarker = '0'
    else:
        playerMarker = 'X'
    displayBoard(board)

    while InGame:
        if playerMarker == '0':
            print('Player go: (0-8)')
            move = int(input())
            if board[move] != ' ':
                print('Invalid move!')
                continue
        else:
            move = getComputerMove(board)
        board[move] = playerMarker
        if checkWin(board, playerMarker):
            InGame = False
            displayBoard(board)
            if playerMarker == '0':
                print('Noughts won!')
            else:
                print('Crosses won!')
            continue
        if check_if_Draw(board):
            InGame = False
            displayBoard(board)
            print('It was a draw!')
            continue
        displayBoard(board)
        if playerMarker == '0':
            playerMarker = 'X'
        else:
            playerMarker = '0'

#start the loop again if y(for yes) is the input
    print('Type y to keep playing')
    inp = input()
    if inp != 'y' and inp != 'Y':
        Playing = False        