import requests
import tkinter
from datetime import datetime

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")

    labelPrice.config(text = str(price) + "$")
    labelTime.config(text= "Updated at:" + time)

    canvas.after(1000, trackBitcoin)

canvas= tkinter.Tk()
canvas.geometry("400x500")
canvas.title("BITCOIN TRACKER")



f1 =("poppins" , 24,"bold")
f2 =("poppins" , 22,"bold")
f3 =("poppins" , 18,"normal")

label = tkinter.Label(canvas, text = "BITCOIN PRICE", font = f1)
label.pack(pady =20)

labelPrice = tkinter.Label(canvas, font = f2)
labelPrice.pack(pady = 20)

labelTime = tkinter.Label(canvas, font = f3)
labelTime.pack(pady = 20)

trackBitcoin()

canvas.mainloop()

