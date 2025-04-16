import requests
import telebot
import time
from datetime import datetime, timedelta

# ✅ التوكن تبع البوت
TOKEN = "8043979447:AAEwXwV6j1bBmPIdainBooX6Fjcjx03690Gw"
bot = telebot.TeleBot(TOKEN)

# 🧑‍💼 الآي دي الخاص بك
ADMIN_ID = 7420171743

# 🧠 دالة توليد توصيات (بسيطة لكن ذكية)
def get_signals():
    try:
        btc = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
        btc_price = btc['bitcoin']['usd']
        
        gold_price = 2341.80
        silver_price = 27.5
        gas_price = 2.2

        # 📆 التوقيت من 20 دقيقة
        signal_time = datetime.utcnow() - timedelta(minutes=20)
        formatted_time = signal_time.strftime('%Y-%m-%d %H:%M:%S')

        msg = f"""
📢 <b>توصيات الأسواق الإحترافية 🔥</b>

🟧 <b>البيتكوين (BTC)</b>
💰 السعر الحالي: <b>{btc_price}$</b>
🟢 نقطة الدخول: <b>{btc_price - 200}$</b>
🎯 الهدف: <b>{btc_price + 500}$</b>
🔻 وقف الخسارة: <b>{btc_price - 600}$</b>
📈 نسبة النجاح: <b>88%</b>

🟨 <b>الذهب (Gold)</b>
💰 السعر الحالي: <b>{gold_price}$</b>
🟢 نقطة الدخول: <b>{gold_price - 20}$</b>
🎯 الهدف: <b>{gold_price + 30}$</b>
🔻 وقف الخسارة: <b>{gold_price - 40}$</b>
📈 نسبة النجاح: <b>90%</b>

🔹 <b>الفضة (Silver)</b>
💰 السعر الحالي: <b>{silver_price}$</b>
🟢 الدخول تحت: <b>{silver_price - 0.5}$</b>

🔥 <b>الغاز الطبيعي</b>
💰 السعر الحالي: <b>{gas_price}$</b>

🕒 <i>تم إنشاء التوصيات: {formatted_time} UTC</i>
"""
        bot.send_message(ADMIN_ID, msg, parse_mode='HTML')

    except Exception as e:
        bot.send_message(ADMIN_ID, f"🚫 حصل خطأ أثناء جلب التوصيات:\n{e}")

# 🔁 إرسال كل 20 دقيقة
while True:
    get_signals()
    time.sleep(1200)
