from aiogram import types

from loader import dp
from keyboards.default.default_btn import main_btn

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer("Menu", reply_markup=main_btn)

