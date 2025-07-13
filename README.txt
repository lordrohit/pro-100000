# Pro-Level Crypto Trading Bot

This bot:
- Scans all Binance Futures perpetual symbols
- Detects chart patterns (flag, wedge, head & shoulders)
- Sends alerts with charts to your Telegram
- Runs 24/7 on 15m and 1h timeframes using async logic

## Features
✅ Chart pattern detection  
✅ Take profit, stop loss, and risk/reward logic  
✅ Alerts only in rare profitable setups  
✅ Async scanning for fast performance  
✅ Telegram bot integration

## Setup Instructions

1. Clone this repo
2. Create a `.env` file using `.env.example`
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the bot locally:
```bash
python main.py
```
5. Deploy to Railway for 24/7 uptime (recommended)

---

Built in Python using:
- python-telegram-bot
- mplfinance
- pandas + TA
- asyncio & aiohttp

Contact: Use Telegram bot to type any coin name for on-demand analysis.
