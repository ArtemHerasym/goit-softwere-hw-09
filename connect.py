from mongoengine import connect
from mongoengine.connection import get_connection
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
mongo_db = os.getenv("MONGO_DB")

connect(
    db=mongo_db,
    host=mongo_uri
)
get_connection().admin.command("ping")
print("Connected successfully")