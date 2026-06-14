import inspect
import socket

import aiohttp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN


def create_ipv4_bot(token):
    bot_params = inspect.signature(Bot).parameters
    connector = aiohttp.TCPConnector(family=socket.AF_INET)

    if "connector" in bot_params:
        return Bot(token=token, connector=connector)

    if "session" in bot_params:
        session = aiohttp.ClientSession(connector=connector)
        return Bot(token=token, session=session)

    connector.close()
    bot = Bot(token=token)
    bot._connector_init["family"] = socket.AF_INET
    return bot


bot = create_ipv4_bot(TOKEN)
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
    print("MENU HANDLER:", message.text, message.from_user.id)
    await message.answer(
        "Привет! Это бот Радио Болид.\nВыберите нужный раздел:",
        reply_markup=get_main_menu(),
    )


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    print("START HANDLER:", message.text, message.from_user.id)
    await send_main_menu(message)


@dp.message_handler()
async def menu(message: types.Message):
    print("FALLBACK HANDLER:", message.text, message.from_user.id)
    text = (message.text or "").lower().strip()
    if text in ("меню", "start", "старт", "начать", "/start", "привет"):
        await send_main_menu(message)
        return

    await message.answer(
        "Я бот Радио Болид. Нажмите кнопку ниже:",
        reply_markup=get_main_menu(),
    )


if __name__ == "__main__":
    print("BOT STARTING")
    executor.start_polling(dp, skip_updates=False)
    print("BOT STOPPED")
