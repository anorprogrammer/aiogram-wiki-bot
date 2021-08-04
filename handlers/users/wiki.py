from aiogram import types

from loader import dp

from wikilib import wiki_result

# Wiki bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    try:
        mgs = wiki_result(message.text)
        await message.answer(mgs)
    except:
        await message.answer("Xabar noto'g'ri kiritildi yoki ma'lumot topilmadi")