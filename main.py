import requests
import telegram
import time

# توكن البوت ومعرفك
TOKEN = "7417533427:AAFiHzYJRluoH7q1jkzoR9SqKZeovUzBrME"
CHAT_ID = 7420171743
bot = telegram.Bot(token=TOKEN)

def get_prices():
    try:
        gold = requests.get("https://api.metals.live/v1/spot/gold").json()[0]['gold']
        silver = requests.get("https://api.metals.live/v1/spot/silver").json()[0]['silver']
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json").json()['bpi']['USD']['rate']
        bitcoin = float(bitcoin.replace(',', ''))
        gas = requests.get("https://api.tradingeconomics.com/commodities/natural-gas?c=guest:guest").json()[0]['Last']
        return float(gold), float(silver), bitcoin, gas
    except Exception as e:
        print("خطأ في جلب البيانات:", e)
        return None, None, None, None

def send_signal():
    gold, silver, bitcoin, gas = get_prices()

    if gold and silver and bitcoin and gas:
        message = f"""
<b>توصيات اليوم (الأسعار الحقيقية):</b>

شراء <b><span style="color:#FFD700;">الذهب</span></b>: {gold} دولار
شراء <b><span style="color:#1E90FF;">الغاز</span></b>: {gas} دولار
شراء <b><span style="color:#FFA500;">البيتكوين</span></b>: {bitcoin} دولار
بيع <b><span style="color:#FFFFFF;">الفضة</span></b>: {silver} دولار
"""
        try:
            bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=telegram.ParseMode.HTML)
            print("تم إرسال التوصيات بنجاح.")
        except Exception as e:
            print("فشل إرسال الرسالة:", e)

send_signal()
