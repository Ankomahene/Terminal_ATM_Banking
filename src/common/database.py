import datetime

import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DB=None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DB = client['atmdb']

    @staticmethod
    def insert(data):
        Database.DB["account"].insert(data)

    @staticmethod
    def find_one(query):
        return Database.DB["account"].find_one(query)

    @staticmethod
    def find(query):
        return Database.DB["account"].find(query)


    @staticmethod
    def update_balance(card_number, pin, amount):
        return Database.DB["account"].update_one({'card_number': card_number, 'pin': pin}, {'$inc': {'balance': amount}, '$set': {'last_transaction_date': datetime.datetime.utcnow()} })

    @staticmethod
    def update_pin( card_number, new_pin):
        return Database.DB["account"].update_one({'card_number': card_number}, {'$set': {'pin': new_pin} })