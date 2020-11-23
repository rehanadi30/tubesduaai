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

def bersihkanKosong(papanUser, papanAsli, x, y, size):
    print("Masuk Fungsi")
    if((0 <= x < size) and (0 <= y < size)):
        if (papanAsli[y][x+1]==0):
            papanUser[y][x+1] = 0
            bersihkanKosong(papanUser, papanAsli, x+1, y, size)
        if (papanAsli[y][x-1]==0):
            papanUser[y][x-1] = 0
            bersihkanKosong(papanUser, papanAsli, x-1, y+1, size)
        if (papanAsli[y-1][x-1]==0):
            papanUser[y-1][x-1] = 0
            bersihkanKosong(papanUser, papanAsli, x-1, y-1, size)

        if (papanAsli[y-1][x+1]==0):
            papanUser[y-1][x+1] = 0
            bersihkanKosong(papanUser, papanAsli, x+1, y-1, size)
        if (papanAsli[y-1][x]==0):
            papanUser[y-1][x] = 0
            bersihkanKosong(papanUser, papanAsli, x, y-1, size)

        if (papanAsli[y+1][x+1]==0):
            papanUser[y+1][x+1] = 0
            bersihkanKosong(papanUser, papanAsli, x+1, y+1, size)
        if (papanAsli[y+1][x-1]==0):
            papanUser[y+1][x-1] = 0
            bersihkanKosong(papanUser, papanAsli, x-1, y+1, size)
        if (papanAsli[y+1][x]==0):
            papanUser[y+1][x] = 0
            bersihkanKosong(papanUser, papanAsli, x, y+1, size)
        #BASIS  
        else:
            papanUser[y][x] = papanAsli[y][x]
    else:
        pass
    

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
                else:
                    if (papanReal[y][x] == 0):
                        bersihkanKosong(papanVisible, papanReal, x-1, y-1, ukuranPapan)
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
    except KeyboardInterrupt:
        print("Game Over")

"""
TO DO LISTS:
1. GUI!!
2. Kotak masih bisa bernilai lebih dari 4
3. Bom masih kegenerate random. Harusnya inputan tuple dari pengguna
"""
