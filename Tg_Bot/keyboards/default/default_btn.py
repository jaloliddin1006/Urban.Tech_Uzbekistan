from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from loader import db
from aiogram.types.web_app_info import WebAppInfo

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="π Lokatsiyani ulashish", request_location=True),           
            # KeyboardButton(text="Google",web_app=WebAppInfo(url="https://kun.uz/")),           
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder="Sozlamalar bo'limi"
    
)

location_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="π Lokatsiyani ulashish", request_location=True),           
        ],[
            KeyboardButton(text="π Ortga"),           
            
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Sozlamalar bo'limi"
    
)

def main_btn(user_id, lat, lon):
    main_btn = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f"π₯‘ Mahsulotlarni ko'rish",web_app=WebAppInfo(url=f"https://erty.uz/{user_id}/{lat}/{lon}")),           
            ],
            [
                KeyboardButton(text="π‘ Shikoyat bildirish"),           
                KeyboardButton(text="π Savatcha")           
            ],
        [
                KeyboardButton(text="π Mening joylashuvim"),           
            ],
        [
                KeyboardButton(text="πΊπΏ/π·πΊ/π¬π§ Tilni o'zgartirish")           
            
        ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Asosiy bo'lim"
        
    )
    return main_btn
