import pymongo
from decouple import config

client = pymongo.MongoClient(config('DB_MONGO_URL_STRING'))


class PriceTicker:

    def __init__(self):
        self.db_client = client['assetWalletDb']
        self.db_context = self.db_client['prices_ticker']

    def set_price_ticker(self, ticker_code, data, price):
        try:
            db_context = self.db_context
            db_context.update_one({
                "ticker_code": ticker_code,
                "date": data
            }, {"$set": {
                "ticker_code": ticker_code,
                "date": data,
                'price': price
            }}, upsert=True)
        except Exception as e:
            print(e)

    def get_price_ticker(self, ticker_code, data):
        try:
            db_context = self.db_context
            infos = db_context.find({
                "ticker_code": ticker_code,
                "date": str(data)
            })
            res_infos = []
            for info in infos:
                del info['_id']

                dicionario_aux = {**info}

                res_infos.append(dicionario_aux)
            return res_infos
        except Exception as e:
            print(e)
