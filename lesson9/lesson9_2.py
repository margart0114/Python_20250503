import pathlib

# Define the file path. Using an absolute path can make the script more robust
# if its execution location changes relative to the data file.
# The path below is taken from the provided context.
file_path_str = r"c:\Users\Eva\OneDrive\文件\Github\Python_20250503\lesson9\names.txt"
# For cross-platform compatibility and easier path manipulation, pathlib is recommended.
file_path = pathlib.Path(file_path_str)
# Alternatively, if "names.txt" is intended to be relative to the script's current working directory:
# file_path = pathlib.Path("names.txt")

try:
    # 使用 with 語法開啟檔案，確保讀取完後自動關閉檔案
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()  # 一次讀取全部內容，回傳字串
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please ensure the path is correct.")
except IOError as e:
    print(f"Error: An I/O error occurred while reading '{file_path}': {e}")
except Exception as e: # Catching other potential unexpected errors
    print(f"An unexpected error occurred: {e}")

