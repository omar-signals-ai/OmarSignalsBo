import requests
import telegram

# بيانات البوت
TOKEN = "توكن_البوت_هنا"
CHAT_ID = 7420171743
bot = telegram.Bot(token=TOKEN)

def get_prices():
    try:
        # أسعار الذهب والفضة (من موقع سريع)
        metals = requests.get("https://api.metals.live/v1/spot").json()
        gold = metals[0]['gold']
        silver = metals[0]['silver']

        # سعر البيتكوين من CoinDesk
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json").json()['bpi']['USD']['rate_float']

        # سعر الغاز الطبيعي من Trading Economics
        gas = requests.get("https://api.tradingeconomics.com/commodities/natural-gas?c=guest:guest")
        gas = gas.json()[0]['Last']

        return gold, silver, bitcoin, gas
    except Exception as e:
        print("حدث خطأ في جلب الأسعار:", e)
        return None, None, None, None

def send_signal():
    gold, silver, bitcoin, gas = get_prices()
    if gold and silver and bitcoin and gas:
        message = f"""
<b><span style="color:#FF7000;">تنبيه توصيات تداول (ذهب - فضة - بيتكوين - غاز)</span></b>

<b>الذهب:</b> <span style="color:#FFD700;">${gold}</span>
<b>الفضة:</b> <span style="color:#C0C0C0;">${silver}</span>
<b>البيتكوين:</b> <span style="color:#FFA500;">${bitcoin}</span>
<b>الغاز:</b> <span style="color:#00FFFF;">${gas}</span>
"""
        try:
            bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=telegram.ParseMode.HTML)
        except Exception as e:
            print("فشل في إرسال الرسالة:", e)

send_signal()
