import asyncio
from utils import send_telegram_message, detect_patterns, generate_chart
from autoscan import scan_all_symbols

async def main():
    await send_telegram_message("Crypto bot started ✅")
    while True:
        await scan_all_symbols()
        await asyncio.sleep(900)  # 15 minutes

if __name__ == "__main__":
    asyncio.run(main())
