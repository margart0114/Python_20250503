import yfinance as yf
tw2330 = yf.download('2330.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True)
tw2303 = yf.download('2303.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True)
tw2454 = yf.download('2454.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True)
tw2317 = yf.download('2317.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True)



__name__ == '__main__'