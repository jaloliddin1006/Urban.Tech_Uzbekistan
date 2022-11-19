from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db
from aiogram.types.web_app_info import WebAppInfo

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Lokatsiyani ulashish", request_location=True),           
            # KeyboardButton(text="Google",web_app=WebAppInfo(url="https://kun.uz/")),           
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Sozlamalar bo'limi"
    
)

location_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍 Lokatsiyani ulashish", request_location=True),           
        ],[
            KeyboardButton(text="🔙 Ortga"),           
            
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Sozlamalar bo'limi"
    
)

def main_btn(user_id, lat, lon):
    main_btn = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f"🥡 Mahsulotlarni ko'rish",web_app=WebAppInfo(url=f"https://erty.uz/{user_id}/{lat}/{lon}")),           
            ],
            [
                KeyboardButton(text="🛡 Shikoyat bildirish"),           
                KeyboardButton(text="🛍 Savatcha")           
            ],
        [
                KeyboardButton(text="📍 Mening joylashuvim"),           
            ],
        [
                KeyboardButton(text="🇺🇿/🇷🇺/🇬🇧 Tilni o'zgartirish")           
            
        ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Asosiy bo'lim"
        
    )
    return main_btn
