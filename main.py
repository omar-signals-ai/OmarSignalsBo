import requests
import telebot
import time

# ✅ توكن البوت تبعك (سري، لا تعطيه لحدا)
TOKEN = "8043979447:AAEWxW6jLBmPIdainBooX6Fjcjx03690Gw"
bot = telebot.TeleBot(TOKEN)

# 🧍‍♂️ معرف المستخدم الوحيد المسموح له
ADMIN_ID = 7420171743

# 📈 دالة للحصول على توصيات من مواقع موثوقة
def get_signals():
    try:
        # 🟡 مثال: أسعار من CoinGecko (بتكوين)
        btc_data = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()
        btc_price = btc_data['bitcoin']['usd']

        # 🟡 مثال: سعر الذهب من موقع GoldAPI (موقع مدفوع - مؤقتاً سنستخدم سعر ثابت تجريبي)
        gold_price = 2341.80
        silver_price = 27.5
        gas_price = 2.2

        # 📢 رسالة التوصيات
        message = f"""
📢 توصيات الأسواق 🔔

💰 الذهب:
✅ السعر الحالي: {gold_price} $
🎯 التوصية: شراء
🛑 وقف الخسارة: {gold_price - 20}
📈 الهدف: {gold_price + 25}

🥈 الفضة:
✅ السعر الحالي: {silver_price} $
🎯 التوصية: شراء
🛑 وقف الخسارة: {silver_price - 0.4}
📈 الهدف: {silver_price + 0.6}

🔥 الغاز الطبيعي:
✅ السعر الحالي: {gas_price} $
🎯 التوصية: بيع
🛑 وقف الخسارة: {gas_price + 0.2}
📈 الهدف: {gas_price - 0.2}

₿ بتكوين:
✅ السعر الحالي: {btc_price} $
🎯 التوصية: شراء حذر
🛑 وقف الخسارة: {btc_price - 1000}
📈 الهدف: {btc_price + 1500}

#توصيات #ذهب #بتكوين #فضة #غاز
"""
        return message

    except Exception as e:
        return f"🚫 فشل في جلب التوصيات: {e}"

# 📤 إرسال التوصيات كل ساعة
def send_signals():
    while True:
        text = get_signals()
        bot.send_message(ADMIN_ID, text)
        time.sleep(3600)  # كل ساعة

# 🚀 أمر /start لبدء البوت يدوياً
@bot.message_handler(commands=['start'])
def welcome(message):
    if message.chat.id == ADMIN_ID:
        bot.reply_to(message, "✅ بوت التوصيات يعمل الآن تلقائياً.\nسيتم إرسال توصيات كل ساعة.")
    else:
        bot.reply_to(message, "🚫 لا تملك صلاحية استخدام هذا البوت.")

# 📦 ابدأ الإرسال التلقائي بالتوازي مع الاستقبال
import threading
threading.Thread(target=send_signals).start()

# 🟢 تشغيل البوت
bot.polling()
