import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from ta.trend import SMAIndicator
from ta.momentum import RSIIndicator

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="NeuroTrade AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# NEON UI STYLE
# -----------------------------
st.markdown("""
<style>

body {
    background-color: #050816;
    color: white;
}

.main {
    background-color: #050816;
}

h1 {
    color: #00F5FF;
    text-shadow: 0px 0px 20px #00F5FF;
    text-align: center;
}

.stButton>button {
    background: linear-gradient(90deg, #00F5FF, #A855F7);
    color: white;
    border-radius: 10px;
    border: none;
    font-size: 16px;
    padding: 8px 16px;
}

[data-testid="stSidebar"] {
    background-color: #0B1120;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown(
    "<h1>⚡ NEUROTRADE AI ⚡</h1>",
    unsafe_allow_html=True
)

# -----------------------------
# SIDEBAR CONTROLS
# -----------------------------
st.sidebar.header("Market Controls")

ticker = st.sidebar.text_input("Ticker", "AAPL")
period = st.sidebar.selectbox("Period", ["6mo", "1y", "2y", "5y"])

# -----------------------------
# DATA FETCHING (SAFE)
# -----------------------------
data = yf.download(ticker, period=period)

# FIX 1: Flatten MultiIndex if exists
if isinstance(data.columns, tuple) or hasattr(data.columns, "levels"):
    data.columns = data.columns.get_level_values(0)

# Drop empty data check
if data.empty:
    st.error("No data found. Check ticker symbol.")
    st.stop()

# -----------------------------
# FORCE 1D SERIES (CRITICAL FIX)
# -----------------------------
close = data["Close"].copy().squeeze()
close_series = data['Close'].squeeze()

# -----------------------------
# INDICATORS
# -----------------------------

# SMA
data["SMA20"] = SMAIndicator(
    close=close_series,
    window=20
).sma_indicator()

# EMA
data["EMA20"] = close_series.ewm(span=20, adjust=False).mean()
data["EMA50"] = close_series.ewm(span=50, adjust=False).mean()

# RSI
data["RSI"] = RSIIndicator(
    close=close_series,
    window=14
).rsi()

# -----------------------------
# LATEST VALUES
# -----------------------------
latest_price = float(close.iloc[-1])
latest_rsi = float(data["RSI"].iloc[-1])

# Signal Logic
if latest_rsi > 70:
    signal = "SELL ⚠️"
elif latest_rsi < 30:
    signal = "BUY 🚀"
else:
    signal = "HOLD 📊"

# -----------------------------
# METRICS UI
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Current Price", f"${latest_price:.2f}")
col2.metric("RSI (14)", f"{latest_rsi:.2f}")
col3.metric("Signal", signal)

# -----------------------------
# CANDLESTICK CHART
# -----------------------------
fig = go.Figure()

fig.add_trace(
    go.Candlestick(
        x=data.index,
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        name="Price"
    )
)

fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data["SMA20"],
        mode="lines",
        line=dict(color="#00F5FF", width=2),
        name="SMA20"
    )
)

fig.update_layout(
    template="plotly_dark",
    title=f"{ticker} Market Analysis",
    height=650
)

fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data['EMA20'],
        line=dict(color='#FF00FF'),
        name='EMA20'
    )
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# RSI CHART
# -----------------------------
rsi_fig = go.Figure()

rsi_fig.add_trace(
    go.Scatter(
        x=data.index,
        y=data["RSI"],
        mode="lines",
        line=dict(color="#FF00FF", width=2),
        name="RSI"
    )
)

rsi_fig.add_hline(y=70, line_dash="dash", line_color="red")
rsi_fig.add_hline(y=30, line_dash="dash", line_color="green")

rsi_fig.update_layout(
    template="plotly_dark",
    title="RSI Indicator (14)",
    height=350
)

st.plotly_chart(rsi_fig, use_container_width=True)

# -----------------------------
# AI INSIGHTS PANEL
# -----------------------------
st.subheader("🧠 AI Insights")

if latest_rsi > 70:
    st.error("Market is OVERBOUGHT → Possible correction expected.")
elif latest_rsi < 30:
    st.success("Market is OVERSOLD → Potential buying opportunity.")
else:
    st.info("Market is NEUTRAL → No strong signal detected.")

# -----------------------------
# OPTIONAL DEBUG INFO
# -----------------------------
with st.expander("Debug Data"):
    st.write(data.tail())