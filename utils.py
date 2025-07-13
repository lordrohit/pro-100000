import os
import aiohttp
import mplfinance as mpf
import pandas as pd

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    async with aiohttp.ClientSession() as session:
        await session.post(url, data=data)

async def generate_chart(df, symbol):
    mpf.plot(df.tail(100), type='candle', style='charles',
             title=symbol, volume=True, savefig=f"{symbol}.png")
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    data = {"chat_id": CHAT_ID}
    with open(f"{symbol}.png", "rb") as photo:
        files = {"photo": photo}
        async with aiohttp.ClientSession() as session:
            await session.post(url, data=data, files=files)

def detect_patterns(df):
    return True if df["close"].iloc[-1] > df["open"].iloc[-1] else False
