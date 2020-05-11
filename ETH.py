import datetime
from time import sleep, time
from binance.client import Client
import smtplib
import ssl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

APIKey = "gizpFmRS4jrXdqYNF90dJfLZrKo6omEpAU4lsGcj0RY2MZ7veF9UfDM4m1o1m1RD"
SecretKey = "Eclk74O1i5Nett8ItHvchfz6PKoOrEl8Fg7BmjBDsXz65VwYnlpRwQtQsk6FGIpB"
client = Client(APIKey, SecretKey)

symbol = 'ETHEUR'

klines = client.get_historical_klines(symbol, "1m", "1 hours UTC")

XS = []
YS = []
XS.append(datetime.datetime.now())
YS.append(float(klines[-1][4]))


def test(i):
    global XS, YS, YS2
    klines = client.get_historical_klines(symbol, "1m", "1 hours UTC")
    histo = client.get_all_orders(symbol='ETHEUR')[-1]
    XS.append(datetime.datetime.now())
    YS.append(float(klines[-1][4]))

    XS = XS[-800:]
    YS = YS[-800:]

    if XS[-1] > XS[-2]:
        color = "green"
    elif XS[-1] < XS[-2]:
        color = 'red'
    else:
        color = 'gray'

    plt.cla()
    plt.plot(
        XS, YS, label=f'Binance Graph : {YS[-1]} \n{histo["side"]} : {float(histo["price"])}', color=color)
    plt.legend()


style.use('fivethirtyeight')
ani = animation.FuncAnimation(plt.gcf(), test, interval=1000)
plt.show()

