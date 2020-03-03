#It is assumed that the AI is always the maximising player and the human is always the minimising player

import sys, pygame, random, math
sys.setrecursionlimit(999999999)
pygame.init()

size = width, height = 600, 600
offset = 50

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

human = 'O'
ai = 'X'

grid = [['', '', ''],
        ['', '', ''],
        ['', '', '']]

players = ['X', 'O']

def check_winning_states(grid, player):
    if (grid[0][0] == player and grid[1][0] == player and grid[2][0] == player):
        return True
    elif (grid[0][1] == player and grid[1][1] == player and grid[2][1] == player):
        return True
    elif (grid[0][2] == player and grid[1][2] == player and grid[2][2] == player):
        return True
    elif (grid[0][0] == player and grid[0][1] == player and grid[0][2] == player):
        return True
    elif (grid[1][0] == player and grid[1][1] == player and grid[1][2] == player):
        return True
    elif (grid[2][0] == player and grid[2][1] == player and grid[2][2] == player):
        return True
    elif (grid[0][0] == player and grid[1][1] == player and grid[2][2] == player):
        return True
    elif (grid[2][0] == player and grid[1][1] == player and grid[0][2] == player):
        return True
    else:
        return False

def boardValue(board, depth):
    if (check_winning_states(board, ai)):
        return 10 - depth
    elif (check_winning_states(board, human)):
        return -10 + depth
    elif checkTie(board):
        return 0

def checkTie(board):
    avail = 0
    for i in range(3):
        for j in range(3):
            if grid[i][j] == ai or grid[i][j] == human:
                avail += 1

    if (avail == 9) and (check_winning_states(board, ai) == False) and (check_winning_states(board, human) == False):
        #print("Tie state")
        return True
    else:
        return False

def map(p, a, b, c, d):
    q = ((p-a)*(d-c)//(b-a))+c
    return q

def drawNaughts(x, y):
    pygame.draw.circle(screen, (255,255,255), (x,y), int(width/6 - offset), 2)

def drawCrosses(x,y):
    pygame.draw.line(screen, (255,255,255), ((x-width/6 + offset) , (y+height/6 - offset)), ((x+width/6 - offset), (y-height/6 + offset)), 2)
    pygame.draw.line(screen, (255,255,255), ((x+width/6 - offset), (y+height/6 - offset)), ((x-width/6 + offset), (y-height/6 + offset)), 2)

def aiMove(board):
    return bestMove(board)

def endState(board):
    if checkTie(board) or check_winning_states(board, 'X') or check_winning_states(board, 'O'):
        return True
    else:
        return False

def minimax(boardState, depth, isMaxPlayer):
    #return 1
    #print(boardState)
    state = boardState
    if endState(state) or depth == 9:
        #print("Test Return Minimax")
        return boardValue(state, depth)
        #return 1


    if isMaxPlayer:
        #print("MAX")
        bestValue = -999999
        for i in range(3):
            for j in range(3):
                if (state[i][j] == ''):
                    state[i][j] = ai

                    value = minimax(state, depth + 1, False)
                    state[i][j] = ''
                    bestValue = max(value, bestValue)
        return bestValue

    elif isMaxPlayer == False:
        #print("MIN")
        bestValue = 99999999
        for i in range(3):
            for j in range(3):
                if (state[i][j] == ''):
                    state[i][j] = human
                    
                    value = minimax(state, depth + 1, True)
                    state[i][j] = ''
                    bestValue = min(value, bestValue)

        return bestValue



def bestMove(board):
    bestVal = -999999999
    bestMoveX = -1
    bestMoveY = -1
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                board[i][j] = ai
                #print(board)
                moveValue = minimax(board, 0, False)
                board[i][j] = ''

                if (moveValue > bestVal):
                    bestVal = moveValue
                    bestMoveX = i
                    bestMoveY = j
    return (bestMoveX, bestMoveY)
    

running = True

naughts = random.choice([True, False])
crosses = not naughts


while 1:
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

    if running:
        if (check_winning_states(grid, ai)):
            print("Player X wins!")
            running = False
        elif (check_winning_states(grid, human)):
            print("Player O wins!")
            running = False
        elif (checkTie(grid)):
            print("Tie!")
            running = False

        #This is drawing the lines that you need to make the 3x3 grid
        pygame.draw.line(screen, (255,255,255), (width/3,0), (width/3,height))
        pygame.draw.line(screen, (255,255,255), (2*width/3,0), (2*width/3,height))

        pygame.draw.line(screen, (255,255,255), (0,height/3), (width,height/3))
        pygame.draw.line(screen, (255,255,255), (0,2*height/3), (width,2*height/3))

        # if crosses:
        #     aiMove(grid)
        if crosses and running:
            

            a = aiMove(grid)
            grid[a[0]][a[1]] = ai
            # grid[j][i] = ai
            crosses = False
            naughts = True

        if event.type == pygame.MOUSEBUTTONDOWN and running:
            if event.button == 1:
                (x,y) = pygame.mouse.get_pos()
                i = map(y, 0, height, 0, 3)
                j = map(x, 0, width, 0, 3)

                if grid[i][j] == '':
                    if naughts:
                        grid[i][j] = human
                        naughts = False
                        crosses = True
                    # elif crosses:
                    #     a = aiMove(grid)
                    #     grid[a[0]][a[1]] = ai
                    #     # grid[j][i] = ai
                    #     crosses = False
                    #     naughts = True

        for row in range(3):
            for col in range(3):
                if grid[row][col] == 'X':
                    drawCrosses(int((width/3*col) + width/6), int((height/3*row) + height/6))
                elif grid[row][col] == 'O':
                    drawNaughts(int((width/3*col) + width/6), int((height/3*row) + height/6))

        #This call is needed to referesh the game screen and hence to display any changes that have been made to the display
        pygame.display.update()
