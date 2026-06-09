import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is required")

STREAM_URL = "https://icecast-bulteam.cdnvideo.ru/bolid128"
AD_URL = "https://advradio.ru"
TG_SHOW_URL = "https://t.me/vpsv88"
VK_SHOW_URL = "https://vk.ru/vpsv88"
SITE_URL = "https://bolidfm.ru"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("🎧 Слушать эфир"))
main_menu.row(KeyboardButton("🌞 Утреннее шоу"), KeyboardButton("📻 Программы"))
main_menu.row(KeyboardButton("🎁 Розыгрыши"), KeyboardButton("💰 Реклама"))
main_menu.add(KeyboardButton("📍 Контакты"))

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("🚗💨 Радио Болид\n\nВыбирай раздел:", reply_markup=main_menu)

@dp.message_handler(lambda m: m.text == "🎧 Слушать эфир")
async def listen(message: types.Message):
    await message.answer(f"🎧 Слушать эфир:\n{STREAM_URL}")

@dp.message_handler(lambda m: m.text == "🌞 Утреннее шоу")
async def morning_show(message: types.Message):
    await message.answer(
        "🌞 Утреннее шоу «В постели с врагами»\n\n"
        "Максим Чапаев и Николай Иванович будят город.\n\n"
        f"📱 Telegram: {TG_SHOW_URL}\n"
        f"📢 VK: {VK_SHOW_URL}"
    )

@dp.message_handler(lambda m: m.text == "📻 Программы")
async def programs(message: types.Message):
    await message.answer(
        "📻 Программы Радио Болид:\n\n"
        "🌞 Утреннее шоу\n"
        "🎵 Music Bolid FM\n"
        "🌙 Night Music BolidFM\n"
        "🔥 Grand Hit BolidFM"
    )

@dp.message_handler(lambda m: m.text == "🎁 Розыгрыши")
async def gifts(message: types.Message):
    await message.answer("🎁 Розыгрыши скоро появятся.")

@dp.message_handler(lambda m: m.text == "💰 Реклама")
async def ads(message: types.Message):
    await message.answer(f"💰 Реклама на радио:\n{AD_URL}")

@dp.message_handler(lambda m: m.text == "📍 Контакты")
async def contacts(message: types.Message):
    await message.answer(
        f"📍 Радио Болид\n\n"
        f"🌐 Сайт: {SITE_URL}\n"
        "☎ Телефон: +7 (342) 233-41-49\n"
        "✉ Email: office@bolidfm.ru"
    )

@dp.message_handler()
async def fallback(message: types.Message):
    await message.answer("Я понимаю только кнопки меню.", reply_markup=main_menu)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)