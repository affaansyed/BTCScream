
import json
import requests
import time
import os
from datetime import datetime



# base variables
apiKey = 'YOUR_API_KEY'
url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD?apikey=' + apiKey
prevRate = 0

# start up
os.system('omxplayer windows.mp3')

# main functions
def getCurrentRate():
        response = requests.get(url)
        json = response.json()
        price = json['rate']


        return price


def priceDiffCheck():
    currentRate = getCurrentRate()
    currentTime = datetime.now().time() 

    if (prevRate - currentRate) >= 5:
        os.system('omxplayer yousuffer.mp3')
        print('BTC DOWN: (%d)' % currentTime)
        print('BTC RATE = (%d)' % currentRate)

    else: 
        print('BTC UP: (%d)' % currentTime)
        print('BTC RATE = (%d)' % currentRate)


# while loop
while True: 
    prevRate = getCurrentRate()
    time.sleep(1800)
    priceDiffCheck()
