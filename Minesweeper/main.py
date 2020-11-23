#Dependency
import pygame
import random as acak
import numpy as np
from constant import *

FPS = 60



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

def papanMinesweeper(size, bom):
    papan = [[0 for row in range(size)] for column in range(size)]

    for num in range(bom):
        x = acak.randint(0, size-1)
        y = acak.randint(0, size-1)
        while (papan[y][x] == 'X'):
        #Harus ada handle ketika sekelilingnya udah bernilai 4
        #or (papan[y][x+1]==4) or (papan[y][x-1]==4) or (papan[y-1][x-1]==4) or (papan[y-1][x+1]==4) or (papan[y-1][x]==4) or (papan[y+1][x+1]==4) or (papan[y+1][x-1]==4) or (papan[y+1][x]==4)):
            x = acak.randint(0, size-1)
            y = acak.randint(0, size-1)
        papan[y][x] = 'X'
    
        if (x >=0 and x <= size-2) and (y >= 0 and y <= size-1):
            if papan[y][x+1] != 'X':
                papan[y][x+1] += 1 # center right
        if (x >=1 and x <= size-1) and (y >= 0 and y <= size-1):
            if papan[y][x-1] != 'X':
                papan[y][x-1] += 1 # center left
        if (x >= 1 and x <= size-1) and (y >= 1 and y <= size-1):
            if papan[y-1][x-1] != 'X':
                papan[y-1][x-1] += 1 # top left
 
        if (x >= 0 and x <= size-2) and (y >= 1 and y <= size-1):
            if papan[y-1][x+1] != 'X':
                papan[y-1][x+1] += 1 # top right
        if (x >= 0 and x <= size-1) and (y >= 1 and y <= size-1):
            if papan[y-1][x] != 'X':
                papan[y-1][x] += 1 # top center
 
        if (x >=0 and x <= size-2) and (y >= 0 and y <= size-2):
            if papan[y+1][x+1] != 'X':
                papan[y+1][x+1] += 1 # bottom right
        if (x >= 1 and x <= size-1) and (y >= 0 and y <= size-2):
            if papan[y+1][x-1] != 'X':
                papan[y+1][x-1] += 1 # bottom left
        if (x >= 0 and x <= size-1) and (y >= 0 and y <= size-2):
            if papan[y+1][x] != 'X':
                papan[y+1][x] += 1 # bottom center
    return papan

def papanUser(size):
    papanVisible = [['-' for row in range(size)] for column in range(size)]
    return papanVisible

def renderNonGui(map):
    for row in map:
        print(" ".join(str(cell) for cell in row) + "\n")

def isWon(papan):
    for row in papan:
        for cell in row:
            if (cell == '-'): #Masih ada yang belum kebuka
                return False
    return True

def gameStatus(score):
    print("Skor kamu adalah: " + str(score))
    isContinue = input("Coba lagi? (y/n) : ")
    if (isContinue == 'n'):
        return False
    return True

def main():
    GameStatus = True
    while GameStatus:
        ukuranPapan = int(input("Masukkan ukuran papan yang kamu inginkan (panjang sisinya saja): "))
        jumlahBom = int(input("Masukkan jumlah Bom yang kamu inginkan: "))
        while (jumlahBom >= (ukuranPapan*ukuranPapan)):
            print("\nJumlah bom lebih banyak dari tiles yang tersedia!\nMasukkan size papan dan jumlah bom kembali!\n")
            ukuranPapan = int(input("Masukkan ukuran papan yang kamu inginkan (panjang sisinya saja): "))
            jumlahBom = int(input("Masukkan jumlah Bom yang kamu inginkan: "))
        papanReal = papanMinesweeper(ukuranPapan, jumlahBom)
        papanVisible = papanUser(ukuranPapan)
        skor = 0

        while True:
            if isWon(papanVisible) == False:
                print("Mau buka kotak yang mana?")
                x = int(input("X : "))
                y = int(input("Y : "))

                if (papanReal[y][x] == 'X'):
                    print("DUARRRR!!!")
                    renderNonGui(papanReal)
                    GameStatus = gameStatus(skor)
                    break
                elif(papanReal[y][x] == 0):
                    pass
                else:
                    papanVisible[y][x] = papanReal[y][x]
                    renderNonGui(papanVisible)
                    skor += 1
            else:
                renderNonGui(papanVisible)
                print("Hore menang!!")
                GameStatus = gameStatus(skor)
                break
                


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Game Over")

"""
TO DO LISTS:
1. GUI!!
2. Kotak masih bisa bernilai lebih dari 4
3. Bom masih kegenerate random. Harusnya inputan tuple dari pengguna
"""
#Dependency
import pygame
import random as acak

def papanMinesweeper(size, bom):
    papan = [[0 for row in range(size)] for column in range(size)]

    for num in range(bom):
        x = acak.randint(0, size-1)
        y = acak.randint(0, size-1)
        while (papan[y][x] == 'X'):
        #Harus ada handle ketika sekelilingnya udah bernilai 4
        #or (papan[y][x+1]==4) or (papan[y][x-1]==4) or (papan[y-1][x-1]==4) or (papan[y-1][x+1]==4) or (papan[y-1][x]==4) or (papan[y+1][x+1]==4) or (papan[y+1][x-1]==4) or (papan[y+1][x]==4)):
            x = acak.randint(0, size-1)
            y = acak.randint(0, size-1)
        papan[y][x] = 'X'
    
        if (x >=0 and x <= size-2) and (y >= 0 and y <= size-1):
            if papan[y][x+1] != 'X':
                papan[y][x+1] += 1 # center right
        if (x >=1 and x <= size-1) and (y >= 0 and y <= size-1):
            if papan[y][x-1] != 'X':
                papan[y][x-1] += 1 # center left
        if (x >= 1 and x <= size-1) and (y >= 1 and y <= size-1):
            if papan[y-1][x-1] != 'X':
                papan[y-1][x-1] += 1 # top left
 
        if (x >= 0 and x <= size-2) and (y >= 1 and y <= size-1):
            if papan[y-1][x+1] != 'X':
                papan[y-1][x+1] += 1 # top right
        if (x >= 0 and x <= size-1) and (y >= 1 and y <= size-1):
            if papan[y-1][x] != 'X':
                papan[y-1][x] += 1 # top center
 
        if (x >=0 and x <= size-2) and (y >= 0 and y <= size-2):
            if papan[y+1][x+1] != 'X':
                papan[y+1][x+1] += 1 # bottom right
        if (x >= 1 and x <= size-1) and (y >= 0 and y <= size-2):
            if papan[y+1][x-1] != 'X':
                papan[y+1][x-1] += 1 # bottom left
        if (x >= 0 and x <= size-1) and (y >= 0 and y <= size-2):
            if papan[y+1][x] != 'X':
                papan[y+1][x] += 1 # bottom center
    return papan

def papanUser(size):
    papanVisible = [['-' for row in range(size)] for column in range(size)]
    return papanVisible

def renderNonGui(map):
    for row in map:
        print(" ".join(str(cell) for cell in row) + "\n")

def isWon(papan):
    for row in papan:
        for cell in row:
            if (cell == '-'): #Masih ada yang belum kebuka
                return False
    return True

def gameStatus(score):
    print("Skor kamu adalah: " + str(score))
    isContinue = input("Coba lagi? (y/n) : ")
    if (isContinue == 'n'):
        return False
    return True

def main():
    GameStatus = True
    while GameStatus:
        ukuranPapan = int(input("Masukkan ukuran papan yang kamu inginkan (panjang sisinya saja): "))
        jumlahBom = int(input("Masukkan jumlah Bom yang kamu inginkan: "))
        while (jumlahBom >= (ukuranPapan*ukuranPapan)):
            print("\nJumlah bom lebih banyak dari tiles yang tersedia!\nMasukkan size papan dan jumlah bom kembali!\n")
            ukuranPapan = int(input("Masukkan ukuran papan yang kamu inginkan (panjang sisinya saja): "))
            jumlahBom = int(input("Masukkan jumlah Bom yang kamu inginkan: "))
        papanReal = papanMinesweeper(ukuranPapan, jumlahBom)
        papanVisible = papanUser(ukuranPapan)
        skor = 0

        while True:
            if isWon(papanVisible) == False:
                print("Mau buka kotak yang mana?")
                x = int(input("X (1-5) : ")) -1
                y = int(input("Y (1-5) : ")) -1

                if (papanReal[y][x] == 'X'):
                    print("DUARRRR!!!")
                    renderNonGui(papanReal)
                    GameStatus = gameStatus(skor)
                    break
                else:
                    papanVisible[y][x] = papanReal[y][x]
                    renderNonGui(papanVisible)
                    skor += 1
            else:
                renderNonGui(papanVisible)
                print("Hore menang!!")
                GameStatus = gameStatus(skor)
                break
                


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Game Over")

"""
TO DO LISTS:
1. GUI!!
2. Kotak masih bisa bernilai lebih dari 4
3. Jika suatu kotak terpilih bernilai 0 dan sekitarnya juga, buka semua kotak tersebut (gak penting dan sepertinya gak perlu)

"""
