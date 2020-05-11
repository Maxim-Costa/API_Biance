import datetime
from time import sleep, time
from binance.client import Client
import smtplib
import ssl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

APIKey = "YOUR-TOKEN"
SecretKey = "YOUR-TOKEN"
client = Client(APIKey, SecretKey)

symbol = 'XRPEUR'
quantity = '0.05'

klines = client.get_historical_klines(symbol, "1m", "1 hours UTC")

XS = []
YS = []


def test(i):
    klines = client.get_historical_klines(symbol, "1m", "1 hours UTC")
    XS.append(datetime.datetime.now())
    YS.append(float(klines[-1][4]))
    ax1.clear()
    ax1.plot(XS, YS)

    try:
        if old != 0:
            pass
    except:
        oldDate = time()
        old = float(klines[-1][4])

    Newtime = time()
    if float(klines[-1][4]) != old:
        print(f"{Newtime-oldDate} ago : ", old)
        print("now : ", klines[-1][4])
        print("difference : ", round(
            float(klines[-1][4])-old, 8))
        if float(klines[-1][4]) > old:
            print("+")
        elif float(klines[-1][4]) < old:
            print("-")
        print("\n\n")
        oldDate = Newtime
        old = float(klines[-1][4])


style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

ani = animation.FuncAnimation(fig, test, interval=100)
plt.show()
