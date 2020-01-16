

import sys, pygame
pygame.init()

size = width, height = 600, 600

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Naughts and Crosses")

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #This is drawing the lines that you need to make the 3x3 grid
    pygame.draw.line(screen, (255,255,255), (width/3,0), (width/3,height))
    pygame.draw.line(screen, (255,255,255), (2*width/3,0), (2*width/3,height))

    pygame.draw.line(screen, (255,255,255), (0,height/3), (width,height/3))
    pygame.draw.line(screen, (255,255,255), (0,2*height/3), (width,2*height/3))

    

    #This call is needed to referesh the game screen and hence to display any changes that have been made to the display
    pygame.display.update()
    