# 📊 Automated Crypto & News Digest Bot

An automated Python bot that fetches real-time financial market data via RESTful APIs and pushes a formatted daily summary directly to a Telegram channel via Webhooks.

## Features
- **Real-Time Market Data:** Connects to the CoinGecko API to pull price data and 24-hour trends for major cryptocurrencies.
- **Automated Delivery:** Runs on a scheduled background routine (`python-schedule`) to deliver daily digests.
- **Telegram Webhook Integration:** Formats dynamic JSON payloads into Markdown and delivers instant notifications to a private Telegram chat.

## Built With
- **Python 3.13**
- **Requests** - For handling HTTP GET and POST requests.
- **Schedule** - For managing daily cron-like execution.
- **Telegram Bot API** - For payload delivery via webhooks.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/crypto-digest-bot.git](https://github.com/YOUR_USERNAME/crypto-digest-bot.git)
   cd crypto-digest-bot
   ```

 2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

 3. **Configure Environment Variables:**
   ```
   Update BOT_TOKEN and CHAT_ID inside bot.py with your Telegram credentials from @BotFather and @userinfobot.
   ```
  
  4. **Run the Application:**
    ```bash
    python bot.py
    ```
    