from clips import Environment

def addKotak(x,y,val):
    # dipanggil diawal (sebelum memanggil start)
    # di loop untuk semua komponen papan
    # val bernilai 0-8
    # untuk bom val bernilai -1
    env.build('(defrule buka-kotak-'+str(10*x+y)
    + ' ?lama <- (kotak-tertutup (location-x '+str(x)+') (location-y '+str(y)+'))'
    + ' ?akanbuka <- (akan-buka-kotak (location-x '+str(x)+') (location-y '+str(y)+'))'
    + '   =>'
    + ' (assert (kotak-terbuka (location-x '+str(x)+') (location-y '+str(y)+') (contain '+str(val)+')))'
    + ' (retract ?lama)'
    + ' (retract ?akanbuka)'
    + ' )')
    new_fact = env.find_template('kotak-tertutup').new_fact()
    new_fact['location-x'] = x
    new_fact['location-y'] = y
    new_fact.assertit()

def bukaKotak(x,y):
    # dipanggil untuk membuka kotak
    # engine hanya boleh membuka kotak yang 'chain dari pembukaan kotak yang val-nya 0'
    # untuk melihat list kotak yang terbuka gunakan getKotakTerbuka(size)
    new_fact = env.find_template('akan-buka-kotak').new_fact()
    new_fact['location-x'] = x
    new_fact['location-y'] = y
    new_fact.assertit()

def printAllFact():
    # dipanggil internal untuk debugging clips
    # kalau engine mau pakai silahkan aja
    for i in env.facts():
        print(i)

def getKotakTerbuka(size):
    # dipanggil untuk get kotak yang terbuka
    # format keluaran berupa matriks[size][size]
    # elemen matriks bernilai False jika kotak belum dibuka
    # jika ada kotak yang belum dibuat (belum addKotak), nilainya juga False
    # elemen matriks bernilai True jika kotak sudah dibuka
    papan = [[False for row in range(size)] for column in range(size)]
    for i in env.facts():
        if(i.template.name=='kotak-terbuka'):
            papan[i['location-x']][i['location-y']] = True
    return papan


env = Environment()
env.load('miner.clp')

# addKotak(0,0,3)
# bukaKotak(0,0)

def start():
    env.run()

start()
