

from aiogram import types
from loader import dp, db, bot

import qrcode
import cv2
# 

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
    await message.reply(val)
