import qrcode as qr 

img= qr.make("https://in.tradingview.com/")
img.save("trading_view_code.png")
