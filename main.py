import requests
import telegram

# بيانات البوت
TOKEN = "8043979447:AAEWXwV6jLBmPIdainBooX6FjcjxO3690Gw"
CHAT_ID = 7420171743
bot = telegram.Bot(token=TOKEN)

def get_prices():
    try:
        gold = requests.get("https://metals-api.com/api/latest?access_key=demo&base=USD&symbols=XAU").json()['rates']['XAU']
        silver = requests.get("https://metals-api.com/api/latest?access_key=demo&base=USD&symbols=XAG").json()['rates']['XAG']
        bitcoin = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd").json()['bitcoin']['usd']
        gas = requests.get("https://commodities-api.com/api/latest?access_key=demo&base=USD&symbols=NG").json()['data']['rates']['NG']
        return gold, silver, bitcoin, gas
    except Exception as e:
        print("حدث خطأ في جلب البيانات:", e)
        return None, None, None, None

def send_signal():
    gold, silver, bitcoin, gas = get_prices()
    if gold and silver and bitcoin and gas:
        message = f"""
<b><span style="color:#FF0700;">توصيات قوية (رؤية حالية):</span></b>

<b>الذهب:</b> <span style="color:#FFD700;">{gold}</span>
<b>الفضة:</b> <span style="color:#C0C0C0;">{silver}</span>
<b>البيتكوين:</b> <span style="color:#FFA500;">{bitcoin}</span>
<b>الغاز:</b> <span style="color:#00FFFF;">{gas}</span>
"""
        try:
            bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=telegram.ParseMode.HTML)
        except Exception as e:
            print("فشل إرسال الرسالة:", e)

send_signal()
