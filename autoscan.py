import asyncio
import aiohttp
import pandas as pd
from utils import detect_patterns, generate_chart, send_telegram_message

async def fetch_klines(session, symbol):
    url = f"https://fapi.binance.com/fapi/v1/klines?symbol={symbol}&interval=15m&limit=100"
    async with session.get(url) as response:
        data = await response.json()
        df = pd.DataFrame(data, columns=[
            "timestamp", "open", "high", "low", "close", "volume",
            "close_time", "quote_asset_volume", "number_of_trades",
            "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
        ])
        df = df.astype({"open": float, "high": float, "low": float, "close": float, "volume": float})
        return df

async def scan_all_symbols():
    async with aiohttp.ClientSession() as session:
        url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
        async with session.get(url) as resp:
            data = await resp.json()
            symbols = [s["symbol"] for s in data["symbols"] if s["contractType"] == "PERPETUAL"]
        
        tasks = [process_symbol(session, symbol) for symbol in symbols]
        await asyncio.gather(*tasks)

async def process_symbol(session, symbol):
    try:
        df = await fetch_klines(session, symbol)
        if detect_patterns(df):
            generate_chart(df, symbol)
            send_telegram_message(f"🚀 Pattern detected on {symbol}")
    except Exception as e:
        print(f"Error processing {symbol}: {e}")
