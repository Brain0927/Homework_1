import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import plotly.graph_objects as go
from src.logger import logger, log_execution_time

class CustomLinearRegression:
    def __init__(self):
        self.slope = None
        self.intercept = None
        self.model = LinearRegression()
        logger.info("初始化線性回歸模型")
    
    @log_execution_time(logger)
    def generate_data(self, slope=2, intercept=1, noise_std=1, n_points=100, random_state=42):
        """生成帶有可控制參數的線性回歸數據"""
        logger.info(f"生成數據 - 斜率:{slope}, 截距:{intercept}, 雜訊:{noise_std}, 點數:{n_points}")
        np.random.seed(random_state)
        X = np.linspace(0, 10, n_points).reshape(-1, 1)
        noise = np.random.normal(0, noise_std, n_points)
        y = slope * X.ravel() + intercept + noise
        logger.debug(f"數據生成完成 - X範圍:[{X.min():.2f}, {X.max():.2f}], y範圍:[{y.min():.2f}, {y.max():.2f}]")
        return X, y
    
    @log_execution_time(logger)
    def fit(self, X, y):
        """訓練模型"""
        logger.info("開始訓練模型")
        self.model.fit(X, y)
        self.slope = self.model.coef_[0]
        self.intercept = self.model.intercept_
        logger.info(f"模型訓練完成 - 預測斜率:{self.slope:.4f}, 預測截距:{self.intercept:.4f}")
        return self
    
    @log_execution_time(logger)
    def predict(self, X):
        """進行預測"""
        if self.slope is None or self.intercept is None:
            logger.error("模型尚未訓練，無法進行預測")
            raise ValueError("模型尚未訓練")
        predictions = self.model.predict(X)
        logger.debug(f"進行預測 - 輸入範圍:[{X.min():.2f}, {X.max():.2f}], 預測範圍:[{predictions.min():.2f}, {predictions.max():.2f}]")
        return predictions
    
    @log_execution_time(logger)
    def get_metrics(self, X, y):
        """計算模型評估指標"""
        logger.info("計算模型評估指標")
        y_pred = self.predict(X)
        r2 = r2_score(y, y_pred)
        mse = mean_squared_error(y, y_pred)
        rmse = np.sqrt(mse)
        
        # 計算誤差
        errors = np.abs(y - y_pred)
        # 獲取前5個最大誤差的索引
        top_5_outliers_idx = np.argsort(errors)[-5:][::-1]
        
        metrics = {
            'R2': r2,
            'MSE': mse,
            'RMSE': rmse,
            'Slope': self.slope,
            'Intercept': self.intercept,
            'Top5_Outliers': {
                'X': X[top_5_outliers_idx].ravel().tolist(),
                'Y_actual': y[top_5_outliers_idx].tolist(),
                'Y_pred': y_pred[top_5_outliers_idx].tolist(),
                'Error': errors[top_5_outliers_idx].tolist()
            }
        }
        
        logger.info(f"模型評估結果 - R²:{r2:.4f}, RMSE:{rmse:.4f}")
        return metrics
    
    @log_execution_time(logger)
    def get_plot_data(self, X, y, title="線性回歸分析"):
        """獲取繪圖所需的數據"""
        logger.info("準備繪圖數據")
        y_pred = self.predict(X)
        
        # 計算誤差並找出最大的5個離群值
        errors = np.abs(y - y_pred)
        top_5_outliers_idx = np.argsort(errors)[-5:][::-1]
        
        plot_data = {
            'x_data': X.ravel(),
            'y_data': y,
            'y_pred': y_pred,
            'outliers_x': X[top_5_outliers_idx].ravel(),
            'outliers_y': y[top_5_outliers_idx],
            'title': title
        }
        
        logger.debug("繪圖數據準備完成")
        return plot_data

if __name__ == "__main__":
    import streamlit as st

    st.title("線性回歸分析應用")
    
    # 參數設定
    slope = st.sidebar.slider("斜率", -10.0, 10.0, 2.0)
    intercept = st.sidebar.slider("截距", -10.0, 10.0, 1.0)
    noise_std = st.sidebar.slider("雜訊標準差", 0.0, 10.0, 1.0)
    n_points = st.sidebar.slider("點數", 10, 1000, 100)
    
    # 模型實例化
    regression_model = CustomLinearRegression()
    
    # 數據生成
    X, y = regression_model.generate_data(slope=slope, intercept=intercept, noise_std=noise_std, n_points=n_points)
    
    # 模型訓練
    regression_model.fit(X, y)
    
    # 預測
    y_pred = regression_model.predict(X)
    
    # 模型評估
    metrics = regression_model.get_metrics(X, y)
    
    # 結果顯示
    st.subheader("模型評估指標")
    st.write(metrics)
    
    st.subheader("回歸分析圖")
    fig = regression_model.plot_regression(X, y)
    st.plotly_chart(fig)