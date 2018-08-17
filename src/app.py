import datetime

import pymongo

from src.common.database import Database
from src.models.main import Main
from src.models.new_account import New_account

Database.initialize()

main = Main()
main.start_service()


