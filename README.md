# 線性回歸互動實驗室

這是一個基於 Streamlit 的互動式線性回歸學習平台，遵循 CRISP-DM 方法論開發。

## 功能特色

- 🎯 自定義模型參數（斜率、截距）
- 🎲 控制數據生成（雜訊、數據點數量）
- 📊 即時視覺化結果
- 📈 模型評估指標
- 🔮 預測工具

## 安裝說明

1. 克隆專案：
```bash
git clone <repository-url>
cd Homework_1
```

2. 建立虛擬環境（建議）：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows
```

3. 安裝依賴套件：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 啟動應用：
```bash
streamlit run app.py
```

2. 在瀏覽器中打開顯示的網址（通常是 http://localhost:8501）

3. 使用側邊欄調整參數：
   - 調整實際斜率 (a in y=ax+b)
   - 調整實際截距 (b in y=ax+b)
   - 設定雜訊程度
   - 更改數據點數量

4. 觀察結果：
   - 查看模型預測的參數
   - 比較與實際參數的差異
   - 觀察視覺化圖表
   - 使用預測工具進行預測

## 專案結構

```
Homework_1/
├── src/
│   └── model.py          # 核心模型實現
├── data/                 # 數據文件夾
├── docs/
│   └── CRISP-DM.md      # 專案文檔
├── app.py               # Streamlit 應用
├── requirements.txt     # 依賴套件
└── README.md           # 本文件
```

## CRISP-DM 方法論

本專案嚴格遵循 CRISP-DM 方法論開發，詳細文檔請查看 [docs/CRISP-DM.md](docs/CRISP-DM.md)。

## 技術棧

- Python 3.8+
- Streamlit
- NumPy
- scikit-learn
- Matplotlib

## 作者

[您的名字]

## 授權

MIT License