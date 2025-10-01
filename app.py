import streamlit as st
import numpy as np
from src.model import CustomLinearRegression

def main():
    st.set_page_config(page_title="Hw1_史福隆_線性回歸TEST", page_icon="📈", layout="wide")
    
    st.title("📈 Hw1_史福隆_線性回歸TEST_251001")
    
    # 側邊欄參數設置
    st.sidebar.header("模型參數設置")
    
    true_slope = st.sidebar.slider(
        "實際斜率 (a in y=ax+b)", 
        min_value=-5.0, 
        max_value=5.0, 
        value=2.0, 
        step=0.1
    )
    
    true_intercept = st.sidebar.slider(
        "實際截距 (b in y=ax+b)", 
        min_value=-5.0, 
        max_value=5.0, 
        value=1.0, 
        step=0.1
    )
    
    noise_level = st.sidebar.slider(
        "雜訊程度", 
        min_value=0.0, 
        max_value=3.0, 
        value=1.0, 
        step=0.1
    )
    
    n_points = st.sidebar.slider(
        "數據點數量", 
        min_value=10, 
        max_value=1000, 
        value=100
    )
    
    # 建立模型和數據
    model = CustomLinearRegression()
    X, y = model.generate_data(
        slope=true_slope,
        intercept=true_intercept,
        noise_std=noise_level,
        n_points=n_points
    )
    
    # 訓練模型
    model.fit(X, y)
    
    # 獲取評估指標
    metrics = model.get_metrics(X, y)
    
    # 繪製圖形
    st.write("### 線性回歸視覺化")
    
    # 獲取繪圖數據
    plot_data = model.get_plot_data(X, y, "線性回歸分析圖")
    
    # 使用 Streamlit 的 plotly 圖表
    import plotly.graph_objects as go
    
    fig = go.Figure()
    
    # 添加實際數據點
    fig.add_trace(go.Scatter(
        x=plot_data['x_data'],
        y=plot_data['y_data'],
        mode='markers',
        name='實際數據',
        marker=dict(color='blue', size=8, opacity=0.6)
    ))
    
    # 添加回歸線
    fig.add_trace(go.Scatter(
        x=plot_data['x_data'],
        y=plot_data['y_pred'],
        mode='lines',
        name='回歸線',
        line=dict(color='red', width=2)
    ))
    
    # 添加離群值點
    fig.add_trace(go.Scatter(
        x=plot_data['outliers_x'],
        y=plot_data['outliers_y'],
        mode='markers',
        name='離群值',
        marker=dict(color='red', size=12, symbol='circle')
    ))
    
    # 更新圖表布局
    fig.update_layout(
        title=plot_data['title'],
        xaxis_title='X 值',
        yaxis_title='Y 值',
        showlegend=True,
        hovermode='closest',
        template='plotly_white'
    )
    
    # 顯示圖表
    st.plotly_chart(fig, use_container_width=True)

    # 顯示模型結果
    st.write("### 模型結果")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("預測斜率", f"{metrics['Slope']:.3f}")
        st.metric("實際斜率", f"{true_slope:.3f}")
    
    with col2:
        st.metric("預測截距", f"{metrics['Intercept']:.3f}")
        st.metric("實際截距", f"{true_intercept:.3f}")
    
    with col3:
        st.metric("R² 分數", f"{metrics['R2']:.3f}")
        st.metric("RMSE", f"{metrics['RMSE']:.3f}")
    
    # 顯示離群值分析
    st.write("### 離群值分析 (Top 5)")
    st.write("下表顯示了與預測值偏差最大的5個數據點：")
    
    outliers = metrics['Top5_Outliers']
    outlier_data = []
    
    for i in range(5):
        outlier_data.append({
            'X 座標': f"{outliers['X'][i]:.3f}",
            'Y 實際值': f"{outliers['Y_actual'][i]:.3f}",
            'Y 預測值': f"{outliers['Y_pred'][i]:.3f}",
            '誤差': f"{outliers['Error'][i]:.3f}"
        })
    
    st.table(outlier_data)
    
    # 顯示模型公式
    st.write("### 回歸方程式")
    st.latex(f"y = {metrics['Slope']:.3f}x + {metrics['Intercept']:.3f}")
    
    # 數據分析
    st.write("### 數據分析")
    st.write(f"""
    - 模型預測的斜率與實際斜率的差異: {abs(metrics['Slope'] - true_slope):.3f}
    - 模型預測的截距與實際截距的差異: {abs(metrics['Intercept'] - true_intercept):.3f}
    - 模型解釋度 (R²): {metrics['R2']:.3f}
    - 均方根誤差 (RMSE): {metrics['RMSE']:.3f}
    """)
    
    # 新增預測功能
    st.write("### 預測工具")
    x_input = st.number_input("輸入 X 值進行預測:", value=0.0)
    if st.button("進行預測"):
        prediction = model.predict(np.array([[x_input]]))
        st.success(f"預測結果: y = {prediction[0]:.3f}")

if __name__ == "__main__":
    main()