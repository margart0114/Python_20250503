import yfinance as yf
def download_data():
    """
    1.下載yfinance的4檔股票資料,股票有: 2330.TW,2303.TW,2454.TW,2317.TW
    2. 在目前目錄下
    """
    tw2330 = yf.download('2330.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True)
    tw2303 = yf.download('2303.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True)
    tw2454 = yf.download('2454.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True)
    tw2317 = yf.download('2317.TW',start='2024-01-01',end='2024-06-01',auto_adjust=True)

def main():
    download_data()

if __name__ == '__main__':
    main()