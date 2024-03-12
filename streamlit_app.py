import streamlit as st

import plotly.express as px
import pandas as pd
import streamlit as st
import plotly.express as px
import pandas as pd

# Streamlitアプリケーションの設定
st.title("Interactive Overview + Detail")

# データの読み込み
df = pd.read_csv("https://raw.githubusercontent.com/vega/vega/main/docs/data/sp500.csv")
df["date"] = pd.to_datetime(df["date"])

# overview (holder)
overview_holder = st.empty()

# range slider
tmp = df["date"].dt.to_pydatetime()
s, e = tmp[0], tmp[-1]
v_from, v_to = st.slider("slider", s, e, (s, e))

# overview
df_yearly = df.groupby(df["date"].dt.year).max()
overview = px.line(df_yearly, x="date", y="price", title="S&P 500 Overview")
overview.add_vrect(
    x0=v_from,
    x1=v_to,
    line_width=0,
    fillcolor="rgba(30,144,255,0.3)",
)

overview_holder.plotly_chart(overview)

# detail
detail = px.line(df, x="date", y="price", title="S&P 500 Detail")
detail.update_traces(marker=dict(size=5))
detail.update_xaxes(range=[v_from, v_to])
st.plotly_chart(detail)
