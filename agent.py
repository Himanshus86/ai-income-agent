import datetime
import random

# === MASTER AI EARNING AGENT ===

def get_affiliate_products():
    products = [
        {"name": "Smart Neck Fan", "price": 599, "link": "https://example.com/product1"},
        {"name": "Mini Tripod Stand", "price": 249, "link": "https://example.com/product2"},
    ]
    selected = random.choice(products)
    return f"🛍️ *Affiliate Product:* {selected['name']}\n💰 Price: ₹{selected['price']}\n🔗 Buy Link: {selected['link']}\n📲 Pay via UPI: sagarthegame@okicici"

def get_dropship_listing():
    item = {
        "name": "Waterproof Sling Bag",
        "price": 349,
        "order_text": "To order, pay ₹349 to sagarthegame@okicici and send screenshot here."
    }
    return f"📦 *Dropship Item:* {item['name']}\n💰 ₹{item['price']}\n📲 {item['order_text']}"

def get_freelance_task():
    gigs = [
        {"title": "₹1000 for data entry", "platform": "Worknhire"},
        {"title": "₹2000 for 2-page website", "platform": "Freelancer"},
    ]
    chosen = random.choice(gigs)
    return f"💼 *Freelance Gig Applied:* {chosen['title']}\n🌐 Platform: {chosen['platform']}"

def get_stock_tip():
    stocks = ["Tata Motors", "HDFC Bank", "Infosys", "Adani Power"]
    pick = random.choice(stocks)
    return f"📈 *Stock Pick of the Day:* {pick}\n🕐 Suggestion: Watch for swing/intraday opportunity."

def generate_whatsapp_message():
    return "🔥 Don't miss out! Viral products now available.
Pay via UPI: sagarthegame@okicici
DM screenshot after payment."

def main():
    now = datetime.datetime.now()
    print(f"=== AI EARNING AGENT REPORT [{now}] ===")
    print(get_affiliate_products())
    print(get_dropship_listing())
    print(get_freelance_task())
    print(get_stock_tip())
    print("📲 WhatsApp Message:
" + generate_whatsapp_message())
    print("🔁 Agent will re-run in 10 minutes...")

if __name__ == "__main__":
    main()
