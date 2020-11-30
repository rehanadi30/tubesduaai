from clips import Environment

def addKotak(x,y,val):
    env.build('(defrule buka-kotak-'+str(10*x+y)
    + ' ?lama <- (kotak-tertutup (location-x '+str(x)+') (location-y '+str(y)+'))'
    + ' ?akanbuka <- (akan-buka-kotak (location-x '+str(x)+') (location-y '+str(y)+'))'
    + '   =>'
    + ' (assert (kotak-terbuka (location-x '+str(x)+') (location-y '+str(y)+') (contain '+str(val)+')))'
    + ' (retract ?lama)'
    + ' (retract ?akanbuka)'
    + ' )')
    print(val)
    new_fact = env.find_template('kotak-tertutup').new_fact()
    new_fact['location-x'] = x
    new_fact['location-y'] = y
    new_fact.assertit()

def bukaKotak(x,y):
    new_fact = env.find_template('akan-buka-kotak').new_fact()
    new_fact['location-x'] = x
    new_fact['location-y'] = y
    new_fact.assertit()

def printAllFact():
    for i in env.facts():
        print(i)

def getKotakTerbuka(size):
    papan = [[0 for row in range(size)] for column in range(size)]
    for i in env.facts():
        if(i.template.name=='kotak-terbuka'):
            papan[i['location-x']][i['location-y']] = 1
    return papan


env = Environment()
env.load('miner.clp')

addKotak(0,0,1)
bukaKotak(0,0)
addKotak(1,0,3)
bukaKotak(1,0)

def start():
    getAllFact()
    env.run()
    getAllFact()
    print(getKotakTerbuka(2))


start()
