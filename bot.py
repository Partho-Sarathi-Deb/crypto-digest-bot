import time
import schedule
import requests

# Credentials placeholder for GitHub public repository
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID_HERE"

def get_crypto_prices():
    """Fetches real-time crypto prices from CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    btc_price = data["bitcoin"]["usd"]
    btc_change = data["bitcoin"]["usd_24h_change"]
    
    eth_price = data["ethereum"]["usd"]
    eth_change = data["ethereum"]["usd_24h_change"]
    
    sol_price = data["solana"]["usd"]
    sol_change = data["solana"]["usd_24h_change"]
    
    digest = (
        "📊 *MORNING CRYPTO DIGEST*\n\n"
        f"• *Bitcoin (BTC):* ${btc_price:,.2f} ({btc_change:+.2f}%)\n"
        f"• *Ethereum (ETH):* ${eth_price:,.2f} ({eth_change:+.2f}%)\n"
        f"• *Solana (SOL):* ${sol_price:,.2f} ({sol_change:+.2f}%)\n\n"
        "Have a productive day!"
    )
    
    return digest

def send_telegram_message(message):
    """Sends a text message to your Telegram channel via Webhook."""
    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    requests.post(telegram_url, data=payload)

def job():
    """Task executed by the scheduler."""
    print("Running scheduled morning digest job...")
    digest = get_crypto_prices()
    send_telegram_message(digest)
    print("Digest sent successfully!")

# Schedule the job to run every day at 08:00 AM (24-hour format)
schedule.every().day.at("08:00").do(job)

print("Bot service started successfully. Listening for schedule (Press Ctrl+C to stop)...")

# Keep the script running continuously to check the schedule
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
