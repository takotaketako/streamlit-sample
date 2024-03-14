import streamlit as st
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.palettes import Spectral4
import pandas as pd
import numpy as np

# デモデータの生成

N = st.number_input("データ件数", min_value=100, max_value=10**7, value=1000)
dates = pd.date_range("2023-01-01", periods=N, freq="s")
data = pd.DataFrame(
    {
        "date": dates,
        "series1": np.random.randn(N).cumsum(),
        "series2": np.random.randn(N).cumsum(),
        "series3": np.random.randn(N).cumsum(),
    }
)

# ColumnDataSourceを作成
source = ColumnDataSource(data)

# フィギュアの作成
p = figure(width=800, height=400, x_axis_type="datetime", title="時系列データのサンプルグラフ")

# ツールチップの設定
p.add_tools(
    HoverTool(
        tooltips=[
            ("Date", "@date{%F}"),
            ("Value", "@$name{0.2f}"),  # $nameは、グラフに表示される線の名前（series1など）に自動的に置き換わります。
        ],
        formatters={
            "@date": "datetime",  # dateをdatetimeとしてフォーマット
        },
        mode="vline",  # 垂直線でツールチップを表示
    )
)

# 線を描画 & 判例を設定
for name, color in zip(["series1", "series2", "series3"], Spectral4):
    p.line(x="date", y=name, source=source, legend_label=name, color=color, name=name)

p.legend.title = "シリーズ"
p.legend.location = "top_left"
p.legend.click_policy = "hide"  # 凡例をクリックしたときに表示・非表示を切り替える

# Streamlitで表示
st.bokeh_chart(p, use_container_width=True)
