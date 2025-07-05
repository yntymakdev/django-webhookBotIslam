from botapp.bot import bot

WEBHOOK_URL = 'https://your-app.onrender.com/webhook/'

def set_webhook():
    s = bot.set_webhook(WEBHOOK_URL)
    if s:
        print("Webhook установлен успешно")
    else:
        print("Ошибка установки webhook")

if __name__ == "__main__":
    set_webhook()
