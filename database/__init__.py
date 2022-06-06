import sys
import pymongo
import logging

USER_NAME = "user0"
USER_PASSWORD = ""

db = None

LOG_FORMAT = "[%(levelname)s] %(asctime)s - %(message)s"
logging.basicConfig(stream = sys.stdout, 
                    filemode = "w",
                    format = LOG_FORMAT,
                    level=logging.NOTSET)

# connect to database (mongoDB)
try:
    logging.info("connecting to mongodb atlas...")
    client = pymongo.MongoClient("mongodb+srv://{}:{}@cluster0.ybzp5.mongodb.net/?retryWrites=true&w=majority".format(USER_NAME, USER_PASSWORD))
    # the name of this database is "codech"
    db = client.codech
    logging.info("connected successfully!")
except Exception as e:
    logging.fatal(e)
    sys.exit(0)

from database.message import *
from database.user import *

user_add("nickeeeeee")
message_insert("phJYHj", "hel23233loooo")

for i in message_get_all():
    print(i)