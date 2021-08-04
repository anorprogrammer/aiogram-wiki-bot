from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\n"
                        "Wikipedia botga hush kelibsiz !!!"+"\n\n"+
                        "Wikipedia botdan foydalanish uchun xabar yuboring"
    )
