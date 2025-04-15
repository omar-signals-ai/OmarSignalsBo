import telegram

# بيانات البوت
TOKEN = "8043979447:AAEWXwV6jLBmPIdainBooX6FjcjxO3690Gw"
CHAT_ID = 7420171743
bot = telegram.Bot(token=TOKEN)

def send_test_signal():
    message = """
<b><span style="color:#FF7000;">تنبيه تجريبي لتوصيات عمر</span></b>

<b>الذهب:</b> <span style="color:#FFD700;">$2445.12</span>
<b>البيتكوين:</b> <span style="color:#FFA500;">$70982.90</span>
<b>الغاز:</b> <span style="color:#00FFFF;">$2.78</span>
<b>الفضة:</b> <span style="color:#C0C0C0;">$28.32</span>

<b>اشتركوا الآن في توصيات عمر - أقوى إشارات التداول اليومية!</b>
"""
    try:
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=telegram.ParseMode.HTML)
        print("تم إرسال الرسالة التجريبية.")
    except Exception as e:
        print("خطأ أثناء إرسال الرسالة:", e)

send_test_signal()
