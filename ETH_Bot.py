import datetime
from time import sleep, time
from binance.client import Client
import smtplib
import ssl
import math
APIKey = "gizpFmRS4jrXdqYNF90dJfLZrKo6omEpAU4lsGcj0RY2MZ7veF9UfDM4m1o1m1RD"
SecretKey = "Eclk74O1i5Nett8ItHvchfz6PKoOrEl8Fg7BmjBDsXz65VwYnlpRwQtQsk6FGIpB"
client = Client(APIKey, SecretKey)

symbol = 'ETHEUR'
quantity = client.get_asset_balance(asset="ETH")

klines = client.get_historical_klines(symbol, "1m", "1 hours UTC")

Newtime, oldDate = time(), time()
oldBuy = 194.60
oldSell = 0
PCSell = 6
PCBuy = -6
Sell = True

difTOTO = 0
oldklines = float(klines[-1][4])

while True:
    klines = client.get_historical_klines(symbol, "1m", "1 hours UTC")
    if float(klines[-1][4]) != oldBuy and oldklines == float(klines[-1][4]):
        if float(klines[-1][4])-oldBuy > PCSell and Sell:
            order = client.order_limit_sell(
                symbol='ETHEUR',
                quantity=0.09,
                price=klines[-1][4]
            )

            print(
                f"{Newtime-oldDate} ago : {'achat : '+str(oldBuy) if Sell else 'Vente  :'+str(oldSell)}")
            print("Vendu a  : ", klines[-1][4])
            print("difference : ", round(
                float(klines[-1][4])-(oldBuy if Sell else +oldSell), 8))
            print("+")

            difTOTO += round(float(klines[-1][4])-oldBuy, 6)
            oldSell = float(klines[-1][4])
            Sell = False
            oldDate = Newtime
            print(f"recolte : {difTOTO}")
            print("\n\n")
        elif float(klines[-1][4])-oldSell < PCBuy and not Sell:
            order = client.order_limit_buy(
                symbol='ETHEUR',
                quantity=0.09,
                price=klines[-1][4]
            )
            print(
                f"{Newtime-oldDate} ago : {'achat : '+str(oldBuy) if Sell else 'Vente  :'+str(oldSell)}")
            print("Achter a : ", klines[-1][4])
            print("difference : ", round(
                float(klines[-1][4])-(oldBuy if Sell else +oldSell), 8))
            print("-")
            oldBuy = float(klines[-1][4])
            Sell = True
            difTOTO += round(oldSell-float(klines[-1][4]), 6)
            oldDate = Newtime
            print("\n\n")
    oldklines = float(klines[-1][4])
