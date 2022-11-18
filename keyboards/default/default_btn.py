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


main_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=f"🥡 Mahsulotlarni ko'rish",web_app=WebAppInfo(url="https://saleh.uz/login/")),           
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


 
dokonlar = ReplyKeyboardMarkup(row_width=2,
                               resize_keyboard=True,
                               input_field_placeholder="Mavjud do'konlar")

for id in markets_name:
    # if curr != id[1]:
    dokonlar.insert(KeyboardButton(text=f"{id}"))
    


            
 
def dokonin(d):
    for i in markets:
    	if i==d:

            dokonlar = ReplyKeyboardMarkup(row_width=2,
                                        resize_keyboard=True,
                                        input_field_placeholder="Tanlangan dokon")

            dokonlar.insert(KeyboardButton(text=f"Mahsulotlar"))
            # for id in markets_name:
            #     # if curr != id[1]:
            #     dokonlar.insert(KeyboardButton(text=f"{id}"))