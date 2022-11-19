from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from datetime import datetime
# import asyncpg
from data.config import ADMINS
from loader import dp, db, bot
# import sqlite3
from keyboards.default.default_btn import location, main_btn, location_2
from aiogram.dispatcher import FSMContext
# from aiogram.types import Bot
import requests       

import requests
from datetime import *
import asyncio
import pytz
from loader import scheduler
from keyboards.inline.inline_btn import select_lang

tz = pytz.timezone('Asia/Tashkent')

td = datetime.now().date()

################################## Web site ni API dan doimiy ma'lumot olish va jo'natish ########################################################
async def djangoconnect(user_id=None, lat=None, lon=None):
    if lat and lon:

        response =  requests.get(f"https://erty.uz/{user_id}/{lat}/{lon}")  
        data = response.json()[0]
    elif user_id and not (lat and lon):
        response =  requests.get(f"https://erty.uz/{user_id}/json/sells_product/")   
        data = response.json()[0]
        await bot.send_message(973108256, data['Rate'])
    else:
        pass
        
    # print("-----------------------------------------------------------------")
            
    
    
def schedule_jobs():
    scheduler.add_job(djangoconnect, "interval", seconds=16)
##################################  ########################################################





##################################  Start buyrug'ini uslash ##########################################

@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message, state:FSMContext): 
    try:
        user = db.add_user(id=message.from_user.id,
                                 name=message.from_user.full_name
                                 )
    except :
        user =  db.select_user(id=message.from_user.id)

    await message.answer("Xush kelibsiz!", reply_markup=location)



@dp.message_handler( IsPrivate(), state=None,text="📍 Mening joylashuvim")
async def bot_start(message: types.Message, state:FSMContext):
    user = db.select_user(id=message.from_user.id)[3].split(",")
    await bot.send_location(chat_id=message.from_user.id, latitude=user[0], longitude=user[1])
    await message.answer("yangi joylashuv manzilini tashlang", reply_markup=location_2)


@dp.message_handler( IsPrivate(), content_types=['location'])
async def bot_start(message: types.Message, state:FSMContext):
    lat = message.location.latitude
    lon = message.location.longitude
    # print(lat, lon)
    reply = f"latitude:  {lat}\nlongitude: {lon}"
    db.update_user_location(f"{lat},{lon}", message.from_user.id)
    await message.answer(reply, reply_markup=main_btn( message.from_user.id, lat, lon))
    await state.finish()

@dp.message_handler( IsPrivate(), text="🔙 Ortga")
async def bot_start(message: types.Message, state:FSMContext):
    user = db.select_user(id= message.from_user.id)[3].split(",")
    lat = user[0]
    lon = user[1]
    await message.answer("Bosh mennu", reply_markup=main_btn( message.from_user.id, lat, lon))
    await state.finish()
    
##################################  ########################################################




##############  shikoyat ########

@dp.message_handler( IsPrivate(), state=None,text="🛡 Shikoyat bildirish")
async def bot_start(message: types.Message, state:FSMContext):
    await message.answer("Marxamat bizga/maxsulotlarimizga qanday shikoyat va arizalaringiz bor. Yozishingiz mumkin", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state("shikoyat")
    # print()


@dp.message_handler( IsPrivate(), state="shikoyat")
async def bot_start(message: types.Message, state:FSMContext):
    await message.answer("✅ Qabul qilindi")
    user = db.select_user(id= message.from_user.id)[3].split(",")
    lat = user[0]
    lon = user[1]
    await message.answer("Bosh mennu", reply_markup=main_btn( message.from_user.id, lat, lon))
    await state.finish()
    
    
    
    
##############  tilni o'zgartirish  ########

@dp.message_handler( IsPrivate(), state=None,text="🇺🇿/🇷🇺/🇬🇧 Tilni o'zgartirish")
async def bot_start(message: types.Message, state:FSMContext):

    await message.answer("O'zingizga Kerakli tilni tanlang. ", reply_markup=select_lang)


@dp.callback_query_handler()
async def book_invoice(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("✅ Til sozlandi")
    user = db.select_user(id= call.from_user.id)[3].split(",")
    lat = user[0]
    lon = user[1]
    await call.message.answer("Bosh mennu", reply_markup=main_btn( call.from_user.id, lat, lon))
    # await state.finish()
    



#############################  PAYMENT #############################3

#### Web backend tayyor bo'lishga ulgurmay qolganligi sababli  qo'lda boshlang'ich qiymatlar kiritildi #### 
data = {
        "market": {
            "name":"1-dokon",
            "lat":41.12535,
            "lon":56.23595
        },
        "sell_products":{
            "🥛 Sut":{
                "id":"21331$%$3%$$35",
                "price":13000,
                "amount": 5

            },
            "🍖 Mol go'shti":{
                "id":"21331$%$354%$5",
                "price":58000,
                "amount": 1
               
            }                 
        }
    }

from data.products import products_,  FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING,  prices

@dp.message_handler( IsPrivate(), text="🛍 Savatcha")
async def bot_start(message: types.Message, state:FSMContext):
    pro = data['sell_products']
    txt=""
    for i in pro:
        txt+=i+"\n"
    
    # await call.message.answer("holaa madrid")

    await bot.send_invoice(chat_id=message.from_user.id,
                        **products_.generate_invoice(),
                        payload="txt",
                        )
    # Currency_total_amount_invalid
    
    
@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Chet elga yetkazib bera olmaymiz")
    elif query.shipping_address.city.lower() == "tashkent":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING],
                                        ok=True)



@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):

    
    user_id = pre_checkout_query.from_user.id
    
    # db.delete_sells_all_product(user_id, user_id)
    
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="To'lovingiz qabul qilindi.  \n  Xaridingiz uchun rahmat! \n ")
        
    adress_data = pre_checkout_query.order_info.shipping_address
    client_adress = f"""
        State: {adress_data['state']},
        City: {adress_data['city']},
        Address 1: {adress_data['street_line1']},
        Address 2: {adress_data['street_line2']},
        Post code: {adress_data['post_code']}
    """
    # db.update_user_check_no(pre_checkout_query.id, user_id)
    
    check_sell1 =  f"#CHECK: {pre_checkout_query.id}\n\n"
    check_sell = f"Jami xarajat: {pre_checkout_query.invoice_payload}\n"
    check_sell += f"Telegram user: <a href='tg://user?id={pre_checkout_query.from_user.id}'> {pre_checkout_query.from_user.full_name}</a>\n"
    check_sell +=  f"Xaridor: {pre_checkout_query.order_info.name}\n"
    check_sell +=  f"Manzil: {client_adress}\n"
    check_sell +=  f"Tel: {pre_checkout_query.order_info.phone_number}"
    
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text=check_sell1+check_sell,                                                              
                            )
    user = db.select_user(id= user_id)[3].split(",")
    lat = user[0]
    lon = user[1]
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Tez orada siz bilan bog'lanamiz. \nQandaydir muammo yuzaga kelsa biz bilan bog'laning:\nTelegram: @Jaloliddin_Mamatmusayev \nTelefon: +998932977419", reply_markup=main_btn())
    pro = data['market']
    name = pro['name']
    lat = pro['lat']
    lon = pro['lon']
    await bot.send_location(chat_id=pre_checkout_query.from_user.id, latitude=lat, longitude=lon)
    date = datetime.now( )
    
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text=f"{name} manzili.")
    # db.add_sells_products(user_id, check_sell, check_sell1, date)
    
    await bot.send_message(chat_id=973108256,
                           text=check_sell1+check_sell,
                           
                                                                                           
                            )
    
