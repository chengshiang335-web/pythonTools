import configparser

def load_db_config(config_path: str = 'db_config.ini') -> dict:
    """
    讀取指定的 INI 設定檔，並回傳 [DATABASE] 區段的設定值，回傳格式為字典 (dict)。
    如果檔案不存在或欠缺 [DATABASE] 區段，則回傳 None。
    """
    config = configparser.ConfigParser()
    config.read(config_path, encoding='utf-8')
    

    if 'DATABASE' not in config:
        print(f"設定檔 {config_path} 中缺少 [DATABASE] 區段，無法載入資料庫設定。")
        return None

    db_config = config['DATABASE']
    
    return {
        'db_server': db_config.get('DB_SERVER', 'sa'),
        'user': db_config.get('DB_USER', 'sa'),
        'password': db_config.get('DB_PASSWORD', ''),
        'database': db_config.get('DB_NAME', 'testdb'),
        'table_name': db_config.get('TABLE_NAME', 'feed_data')
    }
 