

from aiogram import types
from loader import dp, db, bot

import qrcode
import cv2
# 

data = {
        "market": {
            "name":"1-dokon",
            "lat":41.12535,
            "lon":56.23595
        },
        "sell_products":{
            "🥛 Sut":{
                "id":"2133342@54%$$35",
                "price":13000,
                "amount": 5,
                "yaroqlilik":"15-12-2022",
                "darajasi":"yaxshi ✅"

            },
            "🍖 Mol go`shti":{
                "id":"21331$%$354%$$35",
                "price":58000,
                "amount": 1,
                 "yaroqlilik":"18-11-2022",
                "darajasi":"yaroqsiz ❌"
               
            }                 
        }
    }
pro = data['sell_products']


@dp.message_handler(commands=['qr'], commands_prefix='!/', state=None)
async def bot_start(message: types.Message): 
    # print("ok")
    url = message.text[3:]
    
# Generate QR Code
    img=qrcode.make(url)
    img.save(f'photo-{message.from_user.id}.png')
    photo = open(f'photo-{message.from_user.id}.png', 'rb')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)




@dp.message_handler(content_types='photo', state=None)
async def bot_start(message: types.Message): 
    await message.photo[-1].download(f'image-{message.from_user.id}.png')
    img=cv2.imread(f'image-{message.from_user.id}.png')
    det=cv2.QRCodeDetector()
    val, pts, st_code=det.detectAndDecode(img)
    # print(val)
    text = ""
    for i in pro:
        
        if str(val).strip() == pro[i]["id"].strip():
            text = f"Maxsulot nomi: <b>{i}</b>\n"
            text += f"Maxsulot narxi: <b>{pro[i]['price']} so'm</b>\n"
            text += f"Saqlash muddati: <b>{pro[i]['yaroqlilik']} gacha</b>\n"
            text += f"Maxsulot nomi: <b>{pro[i]['darajasi']}</b>\n"
        else:
            pass
            # break
    if text:
        
        await message.reply(text)
    else:
        await message.reply("Bizda bunday mahsulot mavjud emas")
        
    # print(text)
    # print(val)
    # print(f"{pro['🍖 Mol go`shti']['id']}")
