"""
Data: 16.07.2021
Author: Shahobiddin Anorboyev

"""

import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN
from wikilib import wiki_result

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    /start buyrug'iga javob beuvchi funksiya
    """
    await message.reply("Assalomu alaykum Wikipedia botga hush kelibsiz !!!"+"\n\n"+
                        "Wikipedia botdan foydalanish uchun xabar yuboring")

@dp.message_handler()
async def send_wiki(message: types.Message):
    """
    Xabarga Wikipediadan ma'lumot topib beruvchi funksiya
    """
    try:
        mgs = wiki_result(message.text)
        await message.answer(mgs)
    except:
        await message.answer("Xabar noto'g'ri kiritildi yoki ma'lumot topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)