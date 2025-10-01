import unittest
import numpy as np
from src.model import CustomLinearRegression

class TestLinearRegression(unittest.TestCase):
    def setUp(self):
        self.model = CustomLinearRegression()
        
    def test_data_generation(self):
        """測試數據生成功能"""
        X, y = self.model.generate_data(slope=2, intercept=1, noise_std=0)
        self.assertEqual(X.shape[0], 100)  # 默認生成 100 個點
        
        # 檢查無雜訊時的完美線性關係
        y_expected = 2 * X.ravel() + 1
        np.testing.assert_array_almost_equal(y, y_expected)
    
    def test_model_fitting(self):
        """測試模型擬合功能"""
        # 生成無雜訊的數據
        X, y = self.model.generate_data(slope=2, intercept=1, noise_std=0)
        
        # 擬合模型
        self.model.fit(X, y)
        
        # 檢查係數
        self.assertAlmostEqual(self.model.slope, 2, places=2)
        self.assertAlmostEqual(self.model.intercept, 1, places=2)
    
    def test_prediction(self):
        """測試預測功能"""
        # 訓練模型
        X, y = self.model.generate_data(slope=2, intercept=1, noise_std=0)
        self.model.fit(X, y)
        
        # 測試預測
        X_test = np.array([[0], [1], [2]])
        y_pred = self.model.predict(X_test)
        y_expected = 2 * X_test.ravel() + 1
        
        np.testing.assert_array_almost_equal(y_pred, y_expected)
    
    def test_metrics(self):
        """測試模型評估指標計算"""
        # 使用無雜訊數據
        X, y = self.model.generate_data(slope=2, intercept=1, noise_std=0)
        self.model.fit(X, y)
        
        # 計算指標
        metrics = self.model.get_metrics(X, y)
        
        # 檢查完美擬合的情況
        self.assertAlmostEqual(metrics['R2'], 1.0, places=5)
        self.assertAlmostEqual(metrics['MSE'], 0.0, places=5)
        self.assertAlmostEqual(metrics['RMSE'], 0.0, places=5)

if __name__ == '__main__':
    unittest.main()