import json
import logging
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from telegram import Bot
from django.conf import settings

# Настроим логирование
logger = logging.getLogger(__name__)

# Обработчик Webhook
@csrf_exempt
@require_http_methods(["GET", "POST"])  # Разрешаем GET и POST запросы
def telegram_webhook(request):
    # Если это GET запрос, то Telegram проверяет доступность Webhook
    if request.method == "GET":
        return HttpResponse("Webhook работает!")  # Ответ для GET запроса

    # Если это POST запрос, то Telegram отправляет данные
    elif request.method == "POST":
        print("=== WEBHOOK ПОЛУЧЕН ===")
        print(f"Method: {request.method}")
        print(f"Body: {request.body}")

        try:
            # Преобразуем тело запроса в JSON
            data = json.loads(request.body)
            print(f"JSON: {data}")

            # Проверяем наличие сообщения
            if 'message' in data:
                message = data['message']
                chat_id = message['chat']['id']
                text = message.get('text', '')

                print(f"Получено сообщение: {text} от {chat_id}")

                # Здесь добавляем логику для отправки сообщения через бот
                bot = Bot(token=settings.TELEGRAM_TOKEN)  # Получаем токен из настроек
                bot.send_message(chat_id=chat_id, text="Привет! Я бот.")  # Отправляем ответ

            return HttpResponse("OK")  # Успешный ответ для Telegram

        except Exception as e:
            logger.error(f"Ошибка при обработке запроса: {e}")
            return HttpResponse("Error", status=500)  # В случае ошибки отдаем статус 500
    else:
        return HttpResponse("Invalid method", status=405)  # Ответ на неподдерживаемые методы
