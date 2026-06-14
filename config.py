import os


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError(
        "Не задан токен Telegram-бота. Установите переменную окружения TELEGRAM_BOT_TOKEN."
    )
