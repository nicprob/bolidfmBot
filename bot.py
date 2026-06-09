import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup

from config import TOKEN, STREAM_URL, AD_URL, TG_SHOW_URL, VK_SHOW_URL, SITE_URL

bot = Bot(token=TOKEN)
dp = Dispatcher()

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎧 Слушать эфир")],
        [KeyboardButton(text="🌞 Утреннее шоу"), KeyboardButton(text="📻 Программы")],
        [KeyboardButton(text="🎁 Розыгрыши"), KeyboardButton(text="💰 Реклама")],
        [KeyboardButton(text="📍 Контакты")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🚗💨 Радио Болид\n\n"
        "Выбирай раздел:",
        reply_markup=main_menu
    )

@dp.message(F.text == "🎧 Слушать эфир")
async def listen(message: Message):
    await message.answer_audio(
        audio=STREAM_URL,
        title="Радио Болид",
        performer="Bolid FM"
    )

@dp.message(F.text == "🌞 Утреннее шоу")
async def morning_show(message: Message):
    await message.answer(
        "🌞 Утреннее шоу «В постели с врагами»\n\n"
        "Максим Чапаев и Николай Иванович будят город, "
        "проверяют реальность на прочность и делают утро менее бесполезным.\n\n"
        f"📱 Telegram: {TG_SHOW_URL}\n"
        f"📢 VK: {VK_SHOW_URL}"
    )

@dp.message(F.text == "📻 Программы")
async def programs(message: Message):
    await message.answer(
        "📻 Программы Радио Болид:\n\n"
        "🌞 Утреннее шоу\n"
        "Главное утреннее шоу Радио Болид. Новости, юмор, розыгрыши, рубрики и бодрое безумие.\n\n"
        "🎵 Music Bolid FM\n"
        "Музыкальный поток Радио Болид: хиты, драйв и настроение.\n\n"
        "🌙 Night Music BolidFM\n"
        "Ночная музыка для тех, кто не спит, работает или просто подозрительно бодр.\n\n"
        "🔥 Grand Hit BolidFM\n"
        "Большие хиты, знакомые треки и музыка, которую хочется слушать громче."
    )

@dp.message(F.text == "🎁 Розыгрыши")
async def gifts(message: Message):
    await message.answer(
        "🎁 Розыгрыши Радио Болид\n\n"
        "Здесь будут конкурсы, подарки и всякие приятные штуки.\n"
        "Пока раздел готовится. Да, даже ботам иногда нужно собраться с мыслями."
    )

@dp.message(F.text == "💰 Реклама")
async def ads(message: Message):
    await message.answer(
        "💰 Реклама на радио\n\n"
        "Хотите рекламу на Радио Болид?\n"
        f"Переходите на сайт: {AD_URL}"
    )

@dp.message(F.text == "📍 Контакты")
async def contacts(message: Message):
    await message.answer(
        "📍 Радио Болид\n\n"
        f"🌐 Сайт: {SITE_URL}\n"
        "☎ Телефон: +7 (342) 233-41-49\n"
        "✉ Email: office@bolidfm.ru"
    )

@dp.message()
async def fallback(message: Message):
    await message.answer(
        "Я пока понимаю только кнопки меню. "
        "Печатать можно, конечно, но бот не обязан изображать телепата.",
        reply_markup=main_menu
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())