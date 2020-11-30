#Dependency
import pygame
import random as acak
import sys
import clipsIO

sys.setrecursionlimit(1500)

def papanMinesweeper(size, bom, listBomX, listBomY):
    papan = [[0 for row in range(size)] for column in range(size)]

    for num in range(bom):
        x = listBomX[num]
        y = listBomY[num]
        papan[y][x] = 'X'
        
        """
        x = acak.randint(0, size-1)
        y = acak.randint(0, size-1)
        while (papan[y][x] == 'X'):
        #Harus ada handle ketika sekelilingnya udah bernilai 4
        #or (papan[y][x+1]==4) or (papan[y][x-1]==4) or (papan[y-1][x-1]==4) or (papan[y-1][x+1]==4) or (papan[y-1][x]==4) or (papan[y+1][x+1]==4) or (papan[y+1][x-1]==4) or (papan[y+1][x]==4)):
            x = acak.randint(0, size-1)
            y = acak.randint(0, size-1)
        papan[y][x] = 'X'
        """
    
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

def renderNonGui(papan):
    for row in papan:
        print(" ".join(str(cell) for cell in row) + "\n")

def bersihkanKosong(papanUser, papanAsli, x, y, size):
    #print("Masuk Fungsi")

    if(papanAsli[y][x] == 0):
        papanUser[y][x] = papanAsli[y][x]
        papanAsli[y][x] = -999
        if ((y >=0 and y <= size-2) and (x >= 0 and x <= size-1)):
            if (papanAsli[x][y+1] == 0):
                bersihkanKosong(papanUser, papanAsli, x, y+1, size)
        if ((y >=1 and y <= size-1) and (x >= 0 and x <= size-1)):
            if (papanAsli[x][y-1] == 0):
                bersihkanKosong(papanUser, papanAsli, x,y-1, size)
        if ((y >= 1 and y <= size-1) and (x >= 1 and x <= size-1)):
            if (papanAsli[x-1][y-1] == 0):
                bersihkanKosong(papanUser, papanAsli, x-1,y-1, size)
        if ((y >= 0 and y <= size-2) and (x >= 1 and x <= size-1)):
            if (papanAsli[x-1][y+1] == 0):
                bersihkanKosong(papanUser, papanAsli, x-1,y+1, size)
        if ((y >= 0 and y <= size-1) and (x >= 1 and x <= size-1)):
            if (papanAsli[x-1][y] == 0):
                bersihkanKosong(papanUser, papanAsli, x-1,y, size)
        if ((y >=0 and y <= size-2) and (x >= 0 and x <= size-2)):
            if (papanAsli[x+1][y+1] == 0):
                bersihkanKosong(papanUser, papanAsli, x+1,y+1, size)
        if ((y >= 1 and y <= size-1) and (x >= 0 and x <= size-2)):
            if (papanAsli[x+1][y-1] == 0):
                bersihkanKosong(papanUser, papanAsli, x+1,y-1, size)
        if ((y >= 0 and y <= size-1) and (x >= 0 and x <= size-2)):
            if (papanAsli[x+1][y] == 0):
                bersihkanKosong(papanUser, papanAsli, x+1,y, size)
        papanAsli[y][x] = 0
        papanUser[y][x] = 0     

    else:
        #print("masuk else")
        papanUser[y][x] = papanAsli[y][x]

def isWon(papanAsli,size):
    papan = clipsIO.getKotakTerbuka(size)
    for row in range(size):
        for cell in range(size):
            isbom = papanAsli[row][cell]=='X'
            if (not papan[row][cell]): #Masih ada yang belum kebuka
                if (not isbom):
                    return False
            else:
                if (isbom):
                    return False
    return True

def gameStatus(score):
    print("Skor kamu adalah: " + str(score))
    isContinue = input("Coba lagi? (y/n) : ")
    if (isContinue == 'n'):
        return False
    return True

def main():
    #KONSTANTA
    arrBomX = []
    arrBomY = []

    #ALGORITMA
    f = open("input.txt","r")
    line = f.readline()
    ukuranPapan = int(line)
    print("Ukuran Papan = " + str(ukuranPapan))
    line = f.readline()
    jumlahBom = int(line)

    for i in range(jumlahBom):
        line = f.readline()
        bomX, bomY = tuple(map(int,line.split(',')))
        arrBomX.append(bomX)
        arrBomY.append(bomY)

    GameStatus = True
    while GameStatus:
        papanReal = papanMinesweeper(ukuranPapan, jumlahBom, arrBomX, arrBomY)
        papanVisible = papanUser(ukuranPapan)
        for i in range(ukuranPapan):
            for j in range(ukuranPapan):
                clipsIO.addKotak(i, j, papanReal[j][i])
        skor = 0
        renderNonGui(papanReal)

        while True:
            if isWon(papanVisible, ukuranPapan) == False:
                print("Mau buka kotak yang mana?")
                x = int(input("X : "))
                y = int(input("Y : "))

                if (papanReal[y][x] == 'X'):
                    print("DUARRRR!!!")
                    renderNonGui(papanReal)
                    GameStatus = gameStatus(skor)
                    break
                else:
                    if (papanReal[y][x] == 0):
                        bersihkanKosong(papanVisible, papanReal, x, y, ukuranPapan)
                        renderNonGui(papanVisible)
                        skor += 1
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
        #clipsIO.addKotak(0,0,3)
        #clipsIO.bukaKotak(0,0)
        #clipsIO.start()
    except KeyboardInterrupt:
        print("Game Over")

"""
TO DO LISTS:
1. GUI!!
4. IsWon nya salah
"""
