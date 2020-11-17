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

def papanUser(size):
    papanVisible = [['-' for row in range(size)] for column in range(size)]
    return papanVisible

def renderNonGui(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))
        print("")

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
        ukuranPapan = -1
        jumlahBom = 1000
        while (jumlahBom > (ukuranPapan*ukuranPapan)):
            print("Masuk ke ukuran dan bom")
            ukuranPapan = int(input("Masukkan ukuran papan yang kamu inginkan (panjang sisinya saja): "))
            jumlahBom = int(input("Masukkan jumlah Bom yang kamu inginkan: "))
        papan = MinesweeperMapAndBomb(ukuranPapan, jumlahBom)
        papanVisible = papanUser(ukuranPapan)
        skor = 0

        while True:
            if isWon(papanVisible) == False:
                print("Mau buka kotak yang mana?")
                x = int(input("X (1-5) : ")) -1
                y = int(input("Y (1-5) : ")) -1

                if (papan[y][x] == 'X'):
                    print("DUARRRR!!!")
                    renderNonGui(papan)
                    GameStatus = gameStatus(skor)
                    break
                else:
                    papanVisible[y][x] = papan[y][x]
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