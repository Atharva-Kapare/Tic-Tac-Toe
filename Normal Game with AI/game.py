import sys, pygame, random
pygame.init()

size = width, height = 600, 600
offset = 50

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

human = 'O'
ai = 'X'

grid = [[[], [], []],
        [[], [], []],
        [[], [], []]]

def check_winning_states(player, grid):
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

def map(p, a, b, c, d):
    q = ((p-a)*(d-c)//(b-a))+c
    return q

def drawNaughts(x, y):
    pygame.draw.circle(screen, (255,255,255), (x,y), int(width/6 - offset), 2)

def drawCrosses(x,y):
    pygame.draw.line(screen, (255,255,255), ((x-width/6 + offset) , (y+height/6 - offset)), ((x+width/6 - offset), (y-height/6 + offset)), 2)
    pygame.draw.line(screen, (255,255,255), ((x+width/6 - offset), (y+height/6 - offset)), ((x-width/6 + offset), (y-height/6 + offset)), 2)

def aiMove(grid):
    for i in range(3):
        for j in range(3):
            if not grid[i][j]:
                return (i,j)

running = True

naughts = random.choice([True, False])
crosses = not naughts
print(naughts, crosses)

while 1:
    
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

    if running:
        if check_winning_states(ai, grid):
            print("Player X wins!")
            running = False
        elif check_winning_states(human, grid):
            print("Player O wins!")
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
                i = map(x, 0, width, 0, 3)
                j = map(y, 0, height, 0, 3)

                if not grid[j][i]:
                    if naughts:
                        grid[j][i] = human
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
