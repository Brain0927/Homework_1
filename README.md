# 線性回歸互動實驗室

## 📊 專案概述

這是一個基於 Streamlit 開發的互動式線性回歸視覺化工具，旨在幫助用戶理解線性回歸的原理和應用。使用者可以通過調整各種參數，即時觀察線性回歸模型的變化。

## ✨ 主要特點

- 🎛️ **互動式參數調整**：可調整斜率、截距、雜訊程度和數據點數量
- 📈 **即時視覺化**：實時更新的回歸線和數據點展示
- 🎯 **離群值分析**：自動識別和標記主要離群值
- 📊 **完整評估指標**：包括 R² 分數、RMSE 等模型評估指標
- 🔮 **預測功能**：支援輸入新的 X 值進行預測

## 🚀 快速開始

### 環境準備
```bash
# 克隆專案
git clone [repository_url]

# 安裝依賴
pip install -r requirements.txt

# 運行應用
streamlit run app.py
```

### 線上演示
[應用連結]

## 📖 使用指南

1. 使用側邊欄調整參數：
   - 調整斜率和截距
   - 設置雜訊程度
   - 更改數據點數量

2. 觀察模型變化：
   - 查看回歸線的變化
   - 分析離群值分布
   - 評估模型性能

3. 進行預測：
   - 輸入 X 值
   - 獲得預測結果

## 🛠️ 技術實現

- **前端框架**：Streamlit
- **數據處理**：NumPy, scikit-learn
- **視覺化**：Plotly
- **版本控制**：Git
- **部署平台**：Streamlit Cloud

## 📂 專案結構

```
Homework_1/
├── app.py              # 主應用程式
├── src/
│   ├── model.py       # 模型實現
│   └── logger.py      # 日誌記錄
├── docs/              # 文檔
│   ├── devLog.md      # 開發日誌
│   └── technical_docs.md  # 技術文檔
└── requirements.txt   # 依賴套件
```

## 📝 文檔

- [開發日誌](docs/devLog.md)
- [技術文檔](docs/technical_docs.md)

## 🔜 未來計劃

- [ ] 支援多變量線性回歸
- [ ] 添加更多機器學習模型
- [ ] 實現數據上傳功能
- [ ] 優化移動端顯示
- [ ] 添加模型持久化功能

## 👥 貢獻

歡迎提出建議和改進意見！

## 📄 授權

MIT License

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

[史福隆]

## 授權

MIT License