"""
app.py

依據 lesson17_2.ipynb 處理方式，建立 CLI 應用程式主架構。
"""
import pandas as pd
import argparse
import os

def process_tips(input_file: str, output_excel: str):
    """
    讀取CSV或Excel檔案，建立樞紐表，並輸出為Excel檔案。
    參考 lesson17_2.ipynb 的資料處理流程。
    """
    ext = os.path.splitext(input_file)[1].lower()
    if ext == '.csv':
        tips_df = pd.read_csv(input_file)
    elif ext in ['.xls', '.xlsx']:
        tips_df = pd.read_excel(input_file)
    else:
        raise ValueError('僅支援CSV或Excel檔案作為輸入')
    tips_df.columns = ['總票價', '小費', '吸煙者', '日期', '時間', '大小']
    tips_df['小費比例'] = tips_df['小費'] / tips_df['總票價']
    grouped = tips_df.groupby(by=['吸煙者','日期'])
    functions = [('數量','count'),('平均','mean'),('最大值','max')]
    tips_df3 = grouped[['小費','總票價']].agg(functions)
    tips_df3.to_excel(output_excel)
    print(f"已將樞紐表輸出至 {output_excel}")

def main():
    """主程式入口，處理命令列參數與檔案處理。"""
    parser = argparse.ArgumentParser(description="CSV/Excel 樞紐表轉 Excel 工具")
    parser.add_argument('--csv', '--excelin', dest='input_file', required=True, help='輸入的CSV或Excel檔案路徑')
    parser.add_argument('--excel', required=True, help='輸出的Excel檔案路徑')
    args = parser.parse_args()
    process_tips(args.input_file, args.excel)

if __name__ == "__main__":
    main()

