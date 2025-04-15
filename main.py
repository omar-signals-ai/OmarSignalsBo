import requests
import telegram
import time

# بيانات البوت
TOKEN = "توكن_البوت_هنا"
CHAT_ID = 7420171743
bot = telegram.Bot(token=TOKEN)

# دالة جلب الأسعار
def get_prices():
    try:
        gold = requests.get("https://api.metals.dev/v1/latest?api_key=demo&currency=USD").json()["rates"]["XAU"]
        bitcoin = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()["bitcoin"]["usd"]
        return gold, bitcoin
    except Exception as e:
        print("حدث خطأ في جلب الأسعار:", e)
        return None, None

# دالة الإرسال
def send_signal():
    gold, bitcoin = get_prices()
    if gold and bitcoin:
        message = f"""
<b><span style="color:#FFD700;">تنبيه توصيات تداول (ذهــب وبيتـكويـن)</span></b>

<b>سعر الذهب:</b> <span style="color:#FFD700;">${gold}</span>
<b>سعر بيتكوين:</b> <span style="color:#FFA500;">${bitcoin}</span>
"""
        try:
            bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=telegram.ParseMode.HTML)
        except Exception as e:
            print("فشل في إرسال الرسالة:", e)

# إرسال الإشارة كل فترة
send_signal()
