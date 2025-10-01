"""
日誌工具模組
提供統一的日誌記錄功能
"""

import logging
import os
from datetime import datetime
from functools import wraps
import time

class Logger:
    def __init__(self, name, log_dir='logs'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # 確保日誌目錄存在
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        # 設定日誌檔案名稱（包含日期）
        log_file = os.path.join(log_dir, f'{name}_{datetime.now().strftime("%Y%m%d")}.log')
        
        # 檔案處理器
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        
        # 控制台處理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # 設定日誌格式
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # 添加處理器
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def debug(self, message):
        """記錄除錯訊息"""
        self.logger.debug(message)
    
    def info(self, message):
        """記錄一般訊息"""
        self.logger.info(message)
    
    def warning(self, message):
        """記錄警告訊息"""
        self.logger.warning(message)
    
    def error(self, message):
        """記錄錯誤訊息"""
        self.logger.error(message)
    
    def critical(self, message):
        """記錄嚴重錯誤訊息"""
        self.logger.critical(message)

def log_execution_time(logger):
    """裝飾器：記錄函數執行時間"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            logger.debug(f"函數 {func.__name__} 執行時間: {execution_time:.4f} 秒")
            return result
        return wrapper
    return decorator

# 創建默認logger實例
logger = Logger('linear_regression')