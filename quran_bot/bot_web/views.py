from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Update
from .bot import bot, dispatcher
import json

@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        json_str = request.body.decode('utf-8')
        update_json = json.loads(json_str)
        update = Update.de_json(update_json, bot)
        dispatcher.process_update(update)
        return JsonResponse({"ok": True})
    return JsonResponse({"ok": False})
from django.shortcuts import render

# Create your views here.
