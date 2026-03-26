import datetime
import os
import json
import pymssql
import sys

# 將上一層目錄加入系統路徑，以讀取 configLoader
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from configLoader.config_loader import load_db_config

def load_env():
    if not os.getenv("DB_USER"):
        try:
            with open("local.settings.json") as f:
                data = json.load(f)
                for k, v in data["Values"].items():
                    os.environ[k] = v
        except:
            pass

load_env()

def insert_to_db(df):
    """
    寫回 SQL
    """
    #print(f"準備寫入 {len(records)} 筆資料...")
# 取得專案根目錄，並精準定位 db_config.ini 的絕對路徑
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, 'configLoader', 'db_config.ini')

    # 正確載入 INI 檔轉換成 Dictionary
    db_config = load_db_config(config_path)

    if not db_config:
        return "錯誤: 讀不到 db_config.ini 設定檔"

    server = db_config['db_server']
    database = db_config['database']    
    user = db_config['user']
    password = db_config['password']    
    #table_name = db_config['table_name'] 
 
    print(f"從環境變數讀取資料庫連線資訊: server={server}, database={database}, user={user}, password={'*' * len(password) if password else None}") 

    if not all([server, database, user, password]):
        return "錯誤: 環境變數未設置"
    
    INS_SQL = """
        INSERT into dbo.News(uid, title, link, published) 
        VALUES (
            %s,
            %s,
            %s,
            %s
        )
    """
    try:
        connect = pymssql.connect(server, user, password, database)
        cursor = connect.cursor()
        print("資料庫連線成功")


        # 將 DataFrame 轉 list of tuples
        records = df[['md5Key', 'title', 'link', 'published']].values.tolist()
        records_tuples = [tuple(x) for x in records]

        print(f"準備寫入 {len(records_tuples)} 筆資料到資料庫...")

        # 寫入資料
        
        cursor.executemany(INS_SQL, records_tuples)
        connect.commit()

        print("資料寫入完畢")
    finally:
        cursor.close()
        connect.close()
