from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

BOT_TOKEN = 'твой_токен_бота_от_ботфазера'

bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

def start(update, context):
    update.message.reply_text("Привет! Я бот на Django через webhook.")

dispatcher.add_handler(CommandHandler("start", start))
