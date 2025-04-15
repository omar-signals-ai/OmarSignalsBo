import requests
import telebot
import time

# ✅ التوكن تبع البوت (رجاءً لا تنشره أمام الجميع 😅)
TOKEN = "8043979447:AAEwXwV6j1bBmPIdainBooX6Fjcjx03690Gw"
bot = telebot.TeleBot(TOKEN)

# 🔐 الآي دي تبعك (المستخدم اللي يوصله التوصيات)
ADMIN_ID = 7420171743

# 📡 دالة الحصول على توصيات من مواقع موثوقة
def get_signals():
    try:
        # 📊 سعر البيتكوين من CoinGecko
        btc_data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
        btc_price = btc_data['bitcoin']['usd']

        # 💰 أسعار الذهب، الفضة، الغاز (أرقام ثابتة كمثال)
        gold_price = 2341.80
        silver_price = 27.5
        gas_price = 2.2

        # 📨 نص الرسالة
        message = f"""
📢 توصيات الأسواق 🔔

📈 الذهب:
💰 السعر الحالي: {gold_price} $
✅ ينصح بالشراء إذا نزل تحت: {gold_price - 20}
🔺 البيع عند: {gold_price + 25}

💎 الفضة:
💰 السعر الحالي: {silver_price} $

🔥 الغاز الطبيعي:
💰 السعر الحالي: {gas_price} $

🪙 البيتكوين:
💰 السعر الحالي: {btc_price} $
"""

        bot.send_message(ADMIN_ID, message)

    except Exception as e:
        bot.send_message(ADMIN_ID, f"🚫 حصل خطأ أثناء جلب التوصيات:\n{e}")

# ✅ بدء التشغيل التلقائي - إرسال كل 20 دقيقة
while True:
    get_signals()
    time.sleep(1200)  # 1200 ثانية = 20 دقيقة
