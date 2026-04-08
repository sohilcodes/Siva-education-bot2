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

DISCLAIMER = """ ⚠️ Disclaimer

This bot is created for educational purposes only.
Trading involves financial risk and may result in losses.

We do not provide financial advice, signals, or guaranteed outcomes.

All content is for learning and informational use only.
These are projections and not guarantees.

By continuing, you confirm that you understand and accept this."""

WELCOME = """👋 Welcome to Learn About Market

This bot provides structured educational content to help you understand how markets work step by step.

📚 What you will learn:
• What trading is and how it works  
• How price movement happens  
• Basic chart concepts  
• Risk awareness principles  

Each lesson is designed to be simple, clear, and easy to follow.

⚠️ Disclaimer:
This content is for educational purposes only.
We do not provide financial advice.

These are projections and not guarantees.

👇 Choose a lesson to begin:
"""

# ===== LESSONS =====

L1 = """📘 Lesson 1: What is Trading?

Trading is the process of buying and selling financial assets based on changes in price over time.

These assets can include:
• Stocks (shares of companies)  
• Forex (currency pairs)  
• Crypto (digital assets)  

📊 Key Idea:
Prices in any market move because of supply (selling pressure) and demand (buying interest).

📌 Example:
If more people want to buy an asset, demand increases and the price may rise.  
If more people want to sell, supply increases and the price may fall.

🧠 Why it matters:
Understanding how and why prices move is the foundation for learning any market concept.

There are different approaches:
• Short-term trading (focused on quick price changes)  
• Long-term investing (focused on gradual growth over time)

⚠️ This content is for educational purposes only.
We do not provide financial advice.

These are projections and not guarantees.

👉 Continue to Lesson 2 to learn how markets move.
"""

L2 = """📘 Lesson 2: How Markets Work

Financial markets move based on the interaction between buyers and sellers.

📊 Key Idea:
The price of an asset changes depending on supply (selling pressure) and demand (buying interest).

When demand is higher than supply, prices may rise 📈  
When supply is higher than demand, prices may fall 📉  

📌 What influences markets:
• Economic data (interest rates, inflation, employment)  
• Global news and events  
• Market sentiment (how traders feel about the market)  

📌 Example:
If positive economic news is released, more buyers may enter the market → demand increases → price may rise.  
If negative news appears, more sellers may enter → supply increases → price may fall.

🧠 Why it matters:
Understanding what moves the market helps you interpret price behavior instead of guessing.

Types of markets include:
• Forex (currency exchange)  
• Stock market (company shares)  
• Cryptocurrency market (digital assets)  

⚠️ This content is for educational purposes only.
We do not provide financial advice.

These are projections and not guarantees.

👉 Continue to Lesson 3 to learn about price movement patterns.
"""

L3 = """📘 Lesson 3: Trading Platforms

A trading platform is a digital tool that allows users to view market data and interact with financial markets.

These platforms are commonly used to:
• Monitor price movements  
• View charts and market trends  
• Practice understanding how markets behave  

📊 Key Idea:
A platform acts as an interface between the user and the market, providing tools to observe and analyze price activity.

📌 Example:
A user can open a chart on a platform to study how prices move over time and identify patterns in market behavior.

🧠 Why it matters:
Choosing a well-known and reliable platform helps ensure a smoother and more secure learning experience.

There are different types of platforms available, each designed for various markets such as currencies, stocks, or digital assets.

⚠️ This content is for educational purposes only.
We do not provide financial advice or platform recommendations.

These are projections and not guarantees.

👉 Continue to Lesson 4 to learn about risk awareness.”
"""

L4 = """📘 Lesson 4: Risk Awareness

Risk awareness is the process of understanding and managing potential losses when observing or participating in financial markets.

📊 Key Idea:
Every market activity involves uncertainty, and outcomes cannot be predicted with certainty.

📌 Important Concepts:
• Exposure: the amount involved in a decision  
• Loss control: limiting potential downside  
• Consistency: avoiding emotional or impulsive actions  

📌 Example:
If a person allocates a small portion of their total capital to a single idea, the overall impact of a negative outcome may be reduced.

🧠 Why it matters:
Understanding risk helps build discipline and encourages a more structured approach to learning about markets.

Developing awareness of risk is essential before exploring more advanced concepts.

⚠️ This content is for educational purposes only.
We do not provide financial advice.

These are projections and not guarantees.

👉 Continue to the next section to strengthen your learning foundation. l
""

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
