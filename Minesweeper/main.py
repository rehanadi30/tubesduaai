import pygame, sys
import numpy as np

FPS = 60
WIDTH, HEIGHT = 600,600
BOARD_ROWS= 10
BOARD_COLS = 10
#SQUARE_SIZE = WIDTH//ROWS
LINE_WIDTH = 3


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Minesweeper')
screen.fill(BLACK)
board = np.zeros((BOARD_ROWS, BOARD_COLS))
print(board)

cover = pygame.image.load(r'D:\ITB\Semester 5\tugas\ai\png\cover.jpg')
#pygame.draw.line(screen, WHITE, )

def draw_lines():
    pygame.draw.line(screen, WHITE, (50,50), (550,50), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (50,550), (550,550), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (50,50), (50,550), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (550,50), (550,550), LINE_WIDTH)
    #VERTIKAL
    pygame.draw.line(screen, WHITE, (100,50), (100,550), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (150,50), (150,550), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (200,50), (200,550), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (250,50), (250,550), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (300,50), (300,550), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (350,50), (350,550), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (400,50), (400,550), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (450,50), (450,550), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (500,50), (500,550), LINE_WIDTH)
    #horizontal
    pygame.draw.line(screen, WHITE, (50,100), (550,100), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (50,150), (550,150), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (50,200), (550,200), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (50,250), (550,250), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (50,300), (550,300), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (50,350), (550,350), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (50,400), (550,400), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (50,450), (550,450), LINE_WIDTH)
    pygame.draw.line(screen, WHITE, (50,500), (550,500), LINE_WIDTH)

draw_lines()

def images(im, x, y):
    screen.blit(im, (x,y))
 
images(cover, 50, 50)
images(cover, 50, 100)
images(cover, 50, 150)
images(cover, 50, 200)
images(cover, 50, 250)
images(cover, 50, 350)
images(cover, 50, 450)
images(cover, 50, 500)

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        pygame.display.update()
    

main()