from ftplib import FTP
import os
import pandas as pd

HOST = "52.172.254.233"
PORT = 21
USER = "pos1"
PASS = "123456"
LOCAL_FILE = "個人網頁.txt"
FTP_FILE = "個人網頁.txt"

ftp = FTP()
ftp.connect(HOST,PORT)
print("連線成功")
ftp.login(USER, PASS)
print("登入成功")
print(ftp.getwelcome())  # 顯示FTP歡迎訊息
ftp.cwd("/pos")

print(ftp.pwd())

files = ftp.nlst()  # 列出當前目錄下的檔案
print(files)


# 上傳檔案 或 下載
if( len(files) == 0):
    print("銷售點尚未上傳營業資訊")
else:
    print("已有銷售檔案開始準備處理:")
    for file in files:
        print(f"檔名: {file}")
        #組合本機存檔路徑,自動處理 / 或 \跨 Windows / Linux 都可以用
        file_path = os.path.join("c:/dw/", file)
        print(f"存檔路徑: {file_path}")
        #FTP 傳輸是 binary mode(最原始0101格式)，讀寫檔案要用二進位模式
        with open(file_path,"wb") as f:
            #FTP 指令：RETR = retrieve 意思：從FTP取得檔案
            ftp.retrbinary(f'RETR {file}', f.write)
ftp.quit()
 