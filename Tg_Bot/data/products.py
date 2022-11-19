from aiogram import types
from aiogram.types import LabeledPrice
from utils.misc.product import Product
from loader import dp, bot, db
import sqlite3

narx=0
prices = []

data = {
        "market": {
            "name":"1-dokon",
            "lat":41.12535,
            "lon":56.23595
        },
        "sell_products":{
            "🥛 Sut":{
                "id":"21331$%$354%$$35",
                "price":13000,
                "amount": 5

            },
            "🍖 Mol go'shti":{
                "id":"21331$%$354%$$35",
                "price":58000,
                "amount": 1
               
            }                 
        }
    }
pro = data['sell_products']
desc = 0
for i in pro:
    name = str(i+'  x '+str(pro[i]['amount']))
    price =  pro[i]['price']*pro[i]['amount']*100
    desc += 1
    prices.append(LabeledPrice(label=name, amount=price))
# prices.append(LabeledPrice(label="pepsi", amount=2000000))

products_ = Product(
    title="Mahsulotlar uchun masofaviy to'lov",
    description=f"Siz tanlagan mahsulotlaringiz turi: \n{desc} xil.  \n\n💵 Mahsulotlarni xarid qilish uchun quidagi tugmani bosing va onlayn to'lovni amalga oshiring.",
    currency="UZS",
    
    prices=prices,

    start_parameter="create_invoice_book_",
    photo_url='https://image.similarpng.com/very-thumbnail/2020/12/Online-payment-concept-Illustration-on-transparent-background-PNG.png',
    photo_width=1080,
    photo_height=1180,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)



REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (3 kun). Maxsus quti bilan",
    prices=[
        LabeledPrice(
            'Maxsus quti', 599900),
        LabeledPrice(
            '3 ish kunida yetkazish', 899900),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 1299900),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(
    id='pickup',
    title="Do'kondan olib ketish",
    prices=[
        LabeledPrice("Yetkazib berish", 0)
    ])

