from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import db

from aiogram.types.web_app_info import WebAppInfo


select_lang = InlineKeyboardMarkup(
	inline_keyboard=[
	[
	
		InlineKeyboardButton(text="O'zbek 🇺🇿 ",callback_data="uzbek"),
		InlineKeyboardButton(text="Русский 🇷🇺 ", callback_data="russian"),
		InlineKeyboardButton(text="English 🇺🇸 ", callback_data="english"),
	],
])
