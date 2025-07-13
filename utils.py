import os
import requests
import mplfinance as mpf
import pandas as pd
from ta.trend import EMAIndicator

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

def generate_chart(df, symbol):
    mpf.plot(df.tail(100), type='candle', style='charles',
             title=symbol, volume=True, savefig=f"{symbol}.png")
    with open(f"{symbol}.png", "rb") as f:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
        files = {'photo': f}
        data = {"chat_id": CHAT_ID}
        requests.post(url, files=files, data=data)

def detect_patterns(df):
    # Placeholder for real pattern detection logic
    return True if df["close"].iloc[-1] > df["open"].iloc[-1] else False
