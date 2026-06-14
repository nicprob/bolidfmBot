from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


def get_main_menu():
    menu = InlineKeyboardMarkup(row_width=1)
    menu.add(
        InlineKeyboardButton("Слушать эфир", url="https://bolidfm.ru/player"),
        InlineKeyboardButton("Сайт Радио Болид", url="https://bolidfm.ru"),
        InlineKeyboardButton("Реклама на Радио Болид", url="https://advradio.ru"),
        InlineKeyboardButton("Утреннее шоу", url="https://t.me/vpsv88"),
        InlineKeyboardButton("VK", url="https://vk.ru/radiobolid"),
        InlineKeyboardButton(
            "Скачать приложение iPhone",
            url="https://apps.apple.com/ru/app/радио-болид/id1483483936",
        ),
        InlineKeyboardButton(
            "Скачать приложение Android",
            url="https://play.google.com/store/apps/details?id=com.vr.radiobolid",
        ),
    )
    return menu


async def send_main_menu(message: types.Message):
    await message.answer(
        "Привет! Это бот Радио Болид.\nВыберите нужный раздел:",
        reply_markup=get_main_menu(),
    )


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await send_main_menu(message)


@dp.message_handler()
async def menu(message: types.Message):
    text = (message.text or "").lower().strip()
    if text in ("меню", "start", "старт", "начать", "/start", "привет"):
        await send_main_menu(message)
        return

    await message.answer(
        "Я бот Радио Болид. Нажмите кнопку ниже:",
        reply_markup=get_main_menu(),
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
