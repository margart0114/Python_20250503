import yfinance as yf
from datetime import datetime
import os
import pandas as pd

# --- 設定區 ---
# 設定股票列表和資料夾名稱
STOCKS = ['2330.TW', '2303.TW', '2454.TW', '2317.TW']
TICKER_MAP = {
    '2330.TW': '台積電',
    '2303.TW': '聯電',
    '2454.TW': '聯發科',
    '2317.TW': '鴻海'
}
DATA_DIR = 'data'
START_DATE = '2000-01-01'


def download_data():
    """
    每日下載指定股票的資料，並儲存為CSV檔。

    1. 股票代碼: 2330.TW, 2303.TW, 2454.TW, 2317.TW
    2. 檔案會儲存在 'data' 資料夾內。
    3. 檔案名稱格式為 '代碼_YYYY-MM-DD.csv' (例如: 2330_2023-10-27.csv)。
    4. 如果當日的檔案已存在，則不會重複下載。
    5. 每次成功下載新檔案後，會刪除該股票對應的舊日期檔案，確保只保留最新的一份。
    """
    # 確保資料夾存在
    os.makedirs(DATA_DIR, exist_ok=True)

    # 獲取今天的日期字串
    today_str = datetime.now().strftime('%Y-%m-%d')

    for ticker in STOCKS:
        stock_code = ticker.split('.')[0]
        
        # 組合今天的檔案路徑
        today_filename = f"{stock_code}_{today_str}.csv"
        today_filepath = os.path.join(DATA_DIR, today_filename)

        # 1. 檢查今日檔案是否已存在，若存在則跳過
        if os.path.exists(today_filepath):
            print(f"'{today_filepath}' 今日已下載，跳過。")
            continue

        # 2. 下載資料
        print(f"正在下載 {ticker} 的資料...")
        try:
            data = yf.download(ticker, start=START_DATE, end=today_str, auto_adjust=True)
            if data.empty:
                print(f"警告：找不到 {ticker} 的資料，跳過儲存。")
                continue
            
            # 3. 儲存為今日的檔案
            data.to_csv(today_filepath)
            print(f"成功儲存資料至 '{today_filepath}'")

            # 4. 刪除此股票的舊檔案
            for filename in os.listdir(DATA_DIR):
                # 檢查檔案是否為此股票的舊CSV檔
                if filename.startswith(f"{stock_code}_") and filename.endswith(".csv") and filename != today_filename:
                    old_filepath = os.path.join(DATA_DIR, filename)
                    os.remove(old_filepath)
                    print(f"已刪除舊檔案: {old_filepath}")
        except Exception as e:
            print(f"下載 {ticker} 時發生錯誤: {e}")

def process_and_combine_data():
    """
    讀取下載的CSV檔，整理並合併成一個包含'Close'欄位的DataFrame。

    1. 從 'data' 資料夾讀取最新的CSV檔案。
    2. 僅萃取每個檔案的 'Close' (收盤價) 欄位。
    3. 將四個檔案的 'Close' 欄位組合成一個DataFrame。
    4. 根據 TICKER_MAP 重新命名欄位。
    5. 移除包含NaN的資料列，確保資料完整性。

    Returns:
        pandas.DataFrame: 一個包含四檔股票收盤價的合併後DataFrame，若無資料則返回None。
    """
    all_stock_series = []

    # 確保資料夾存在
    if not os.path.exists(DATA_DIR):
        print(f"錯誤：資料夾 '{DATA_DIR}' 不存在，請先執行 download_data()。")
        return None

    print("\n--- 開始處理與合併資料 ---")
    for ticker in STOCKS:
        stock_code = ticker.split('.')[0]
        
        # 尋找對應的CSV檔案
        file_path = None
        for filename in os.listdir(DATA_DIR):
            if filename.startswith(f"{stock_code}_") and filename.endswith(".csv"):
                file_path = os.path.join(DATA_DIR, filename)
                break
        
        if file_path is None:
            print(f"找不到 {ticker} 的資料檔案，跳過。")
            continue

        # 讀取資料並整理
        df = pd.read_csv(file_path, index_col='Date', parse_dates=True)
        # 萃取 'Close' 欄位並根據TICKER_MAP重新命名
        close_series = df['Close'].rename(TICKER_MAP[ticker])
        all_stock_series.append(close_series)
        print(f"已處理檔案: {file_path}")

    if not all_stock_series:
        print("沒有任何資料可供合併。")
        return None

    # 合併所有股票的'Close'資料，並移除有NaN的資料列
    combined_df = pd.concat(all_stock_series, axis=1).dropna()
    
    print("\n資料合併完成！")
    return combined_df

def main():
    download_data()
    combined_data = process_and_combine_data()
    if combined_data is not None:
        print("\n合併後的資料預覽：")
        print(combined_data.head())
        print("\n...")
        print(combined_data.tail())

if __name__ == '__main__':
    main()