from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db

from aiogram.types.web_app_info import WebAppInfo


select_lang = InlineKeyboardMarkup(
	inline_keyboard=[
	[
	
		InlineKeyboardButton(text="O'zbek ๐บ๐ฟ ",callback_data="uzbek"),
		InlineKeyboardButton(text="ะ ัััะบะธะน ๐ท๐บ ", callback_data="russian"),
		InlineKeyboardButton(text="English ๐บ๐ธ ", callback_data="english"),
	],
])
