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

markets = {
    "1-dokon":(41.312812, 69.524208), 
    "2-dokon":(41.312932, 69.528208), 
    "3-dokon":(41.312952, 69.528202),
    "4-dokon":(41.312952, 69.528202),
    "5-dokon":(41.312952, 69.528202),
    "6-dokon":(41.312952, 69.528202),
    "7-dokon":(41.312952, 69.528202)
}
markets_name = []
for i in markets:
	markets_name.append(i)
 
def dokonin(d):
    for i in markets:
    	if i==d:
            dokon = InlineKeyboardMarkup(
            inline_keyboard=[
            [
            
                InlineKeyboardButton(text="Maxsulotlarni ko'rish", callback_data=f"{d}:max"),

            ],
            [
            
                InlineKeyboardButton(text="Savat", callback_data=f"{d}:max"),
                InlineKeyboardButton(text="Maxsulotlarni ko'rish", callback_data=f"{d}:max"),

            ],
        ])
