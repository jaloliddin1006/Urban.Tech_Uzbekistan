import asyncio
from utils.db_api.postgresql import Database
# from utils.db_api.postgresql import Database
import requests

# async def test():
#     db = Database()
#     await db.create()
#     # await db.create_table_users()
#     users =await  db.select_all_users()
#     print(users)

# asyncio.run(test())



# response =  requests.get(f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/RUB/18-11-2022")  
# data = response.json()[0]
# print(data['Rate'])




data = {
        "market": {
            "name":"1-dokon",
            "lat":41.12535,
            "lon":56.23595
        },
        "sell_products":{
            "kalbasa":{
                "id":"21331$%$354%$$35",
                "price":13000,
                "amount": 5

            },
            "rolton":{
                "id":"21331$%$354%$$35",
                "price":13000,
                "amount": 5
               
            }                 
        }
    }
pro = data['sell_products']

for i in pro.keys():
    name = pro[i]['price']
    price = pro[i]['price']*pro[i]['amount']*100
    print(price)
    print(i)