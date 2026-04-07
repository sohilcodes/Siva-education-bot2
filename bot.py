import os
import time
import telebot
from flask import Flask, request
from telebot.types import ReplyKeyboardMarkup

TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = 6411315434

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

users = {}

# ===== TEXT =====

DISCLAIMER = """⚠️ Disclaimer

This bot is created for educational purposes only.
Trading involves financial risk and may result in loss.
We do not provide financial advice, signals, or guaranteed results.

By continuing, you confirm that you understand and accept this.
"""

WELCOME = """👋 Welcome to Market Learner Bot

This bot is designed to help you understand the basics of trading step by step.

📚 What you will learn:
• What is trading
• How markets work
• Risk management
• Beginner strategies

⚠️ Disclaimer:
This bot is created for educational purposes only.
Trading involves financial risk and may result in losses.
We do not provide financial advice.

“These are projections and not guarantees.”

👇 Choose a lesson to begin:
"""

# ===== LESSONS =====

L1 = """📘 Lesson 1: What is Trading?

Trading means buying and selling financial assets like:
• Stocks
• Forex (currencies)
• Crypto

The goal is simple:
Buy low and sell high.

There are two main types:
• Short-term trading
• Long-term investing

⚠️ Trading is not a guaranteed way to make money.

“These are projections and not guarantees.”
"""

L2 = """📘 Lesson 2: How Markets Work

Markets move based on:
• Supply and demand
• News and global events
• Economic data

📈 Price rises when demand is high  
📉 Price falls when supply is high  

Types of markets:
• Forex
• Stock market
• Cryptocurrency market

“These are projections and not guarantees.”
"""

L3 = """📘 Lesson 3: Trading Platforms

To start trading, you need a platform.

Examples:
• MetaTrader
• Binance
• TradingView

You can:
• Open trades
• Analyze charts
• Manage funds

Always choose reliable platforms.

“These are projections and not guarantees.”
"""

L4 = """📘 Lesson 4: Risk Management

Risk management helps protect your money.

Rules:
• Risk only 1–2% per trade
• Use Stop Loss
• Avoid overtrading

Example:
If you have $100, risk only $1–$2.

“These are projections and not guarantees.”
"""

L5 = """📘 Lesson 5: Beginner Strategy

Simple approach:

1. Identify trend
2. Wait for confirmation
3. Enter trade
4. Set Stop Loss
5. Set Take Profit

Tools:
• Support & Resistance
• Trend lines
• RSI

Stay consistent.

“These are projections and not guarantees.”
"""

FAQ = """❓ Frequently Asked Questions (FAQ)

1. What is this bot about?
Basic trading education.

---

2. Is this financial advice?
No.

---

3. Can I make money?
No guarantee. Risk involved.

---

4. Do I need experience?
No. Beginner friendly.

---

5. Personal guidance?
Not provided.

---

6. Cost?
Basic lessons are free.

---

⚠️ Disclaimer:
Trading involves risk.

“These are projections and not guarantees.”
"""

ADVANCED = """⭐️ Advanced (Optional)

Once you complete all lessons:

Focus on:
• Chart patterns
• Advanced indicators
• Market psychology

Remember:
Learning takes time. Avoid rushing.

“These are projections and not guarantees.”
"""

# ===== MENU =====

def menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📘 Lesson 1", "📘 Lesson 2")
    kb.row("📘 Lesson 3", "📘 Lesson 4")
    kb.row("📘 Lesson 5", "⭐️ Advanced")
    kb.row("❓ FAQ")
    return kb

# ===== START =====

@bot.message_handler(commands=['start'])
def start(msg):
    uid = msg.from_user.id

    if uid not in users:
        users[uid] = True

        bot.send_message(ADMIN_ID, f"🆕 New User\nID: {uid}\nName: {msg.from_user.first_name}")

        d = bot.send_message(msg.chat.id, DISCLAIMER)

        try:
            bot.pin_chat_message(msg.chat.id, d.message_id)
        except:
            pass

    bot.send_message(msg.chat.id, WELCOME, reply_markup=menu())

# ===== LESSON HANDLERS =====

@bot.message_handler(func=lambda m: m.text == "📘 Lesson 1")
def l1(m):
    bot.send_message(m.chat.id, L1)

@bot.message_handler(func=lambda m: m.text == "📘 Lesson 2")
def l2(m):
    bot.send_message(m.chat.id, L2)

@bot.message_handler(func=lambda m: m.text == "📘 Lesson 3")
def l3(m):
    bot.send_message(m.chat.id, L3)

@bot.message_handler(func=lambda m: m.text == "📘 Lesson 4")
def l4(m):
    bot.send_message(m.chat.id, L4)

@bot.message_handler(func=lambda m: m.text == "📘 Lesson 5")
def l5(m):
    bot.send_message(m.chat.id, L5)

@bot.message_handler(func=lambda m: m.text == "⭐️ Advanced")
def adv(m):
    bot.send_message(m.chat.id, ADVANCED)

@bot.message_handler(func=lambda m: m.text == "❓ FAQ")
def faq(m):
    bot.send_message(m.chat.id, FAQ)

# ===== WEBHOOK =====

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
    )
    return "ok", 200

@app.route("/")
def home():
    return "Bot Running"

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=os.environ.get("RENDER_EXTERNAL_URL") + "/" + TOKEN)
    app.run(host="0.0.0.0", port=10000)
