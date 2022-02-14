import CoinClass as c

def showCoinStatus (coinObj):
    print ("This side of the coin is up", coinObj.get_sideup())

def flip (coinObj):
    coinObj.toss()

myCoin = c.Coin()
showCoinStatus(myCoin)

for i in range(10):
    flip(myCoin)
    showCoinStatus(myCoin)
