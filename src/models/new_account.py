import datetime

from src.common.database import Database


class New_account(object):
    def __init__(self, card_number, pin, name, acc_number, balance, date=datetime.datetime.utcnow()):
        self.card_number = card_number
        self.pin = pin
        self.name = name
        self.acc_number = acc_number
        self.balance = balance
        self.date = date

    def add_account_to_db(self):
        Database.insert(data=self.json())


    def json(self):
        return {
            "card_number": self.card_number,
            "pin": self.pin,
            "name": self.name,
            "acc_number": self.acc_number,
            "balance": self.balance,
            "last_transaction_date": self.date
        }