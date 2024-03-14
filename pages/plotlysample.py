import streamlit as st
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# データの生成
N = st.number_input("データ件数", min_value=100, max_value=10**7, value=1000)
dates = pd.date_range(start="2023-01-01", periods=N, freq="s")
series1 = np.random.randn(N).cumsum()
series2 = np.random.randn(N).cumsum()
series3 = np.random.randn(N).cumsum()

# Plotlyのグラフオブジェクトを作成
fig = go.Figure()

# シリーズ1の追加
fig.add_trace(go.Scatter(x=dates, y=series1, mode="lines+markers", name="Series 1"))

# シリーズ2の追加
fig.add_trace(go.Scatter(x=dates, y=series2, mode="lines+markers", name="Series 2"))

# シリーズ3の追加
fig.add_trace(go.Scatter(x=dates, y=series3, mode="lines+markers", name="Series 3"))

# レイアウトの設定
fig.update_layout(
    title="時系列データのサンプルグラフ",
    xaxis_title="Date",
    yaxis_title="Value",
    legend_title="Legend",
    hovermode="x unified",  # ホバー時に情報を統一して表示
)

# Streamlitでグラフを表示
st.plotly_chart(fig, use_container_width=True)
