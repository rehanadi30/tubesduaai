#Dependency
#import pygame (Buat GUI)
import random as acak

def MinesweeperMapAndBomb(size, bom):
    papan = [[0 for row in range(size)] for column in range(size)]

    for num in range(bom):
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

def renderNonGui(size):
    papanVisible = [['-' for row in range(size)] for column in range(size)]
    return papanVisible

def isWon(papan):
    for row in papan:
        for cell in row:
            if (cell == '-'): #Masih ada yang belum kebuka
                return False
    return True

def main():
    print("Ini minesweeper")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Game Over")