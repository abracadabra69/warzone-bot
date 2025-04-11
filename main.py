import os
import requests
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
API_URL = f"https://api.telegram.org/bot{TOKEN}"

# Устанавливаем Webhook
@app.on_event("startup")
async def set_webhook():
    url = f"{API_URL}/setWebhook"
    response = requests.post(url, data={"url": WEBHOOK_URL})
    print("Webhook set:", response.json())

# Обработка входящих сообщений
@app.post("/")
async def receive_update(request: Request):
    data = await request.json()
    
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "Привет! Я бот по Warzone метам.")
        elif text == "/meta":
            send_message(chat_id, get_fake_meta())
        else:
            send_message(chat_id, "Я тебя не понял, дружище.")

    return JSONResponse(content={"ok": True})

# Функция отправки сообщений
def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

# Пока фейк-мета, позже подключим парсер
def get_fake_meta():
    return get_meta_loadouts()