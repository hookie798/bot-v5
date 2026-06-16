import yfinance as yf

def fetch_market():
    qqq = yf.Ticker("QQQ").history(period="5d")["Close"]
    bnd = yf.Ticker("BND").history(period="5d")["Close"]

    return {
        "qqq": float(qqq.iloc[-1]),
        "bnd": float(bnd.iloc[-1]),
        "qqq_dd": (qqq.iloc[-1] - qqq.max()) / qqq.max() * 100
    }