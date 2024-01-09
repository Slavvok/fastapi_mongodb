import os

import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

CONNECTION_STRING = os.getenv("MONGO_CONNECTION_STRING")
DATABASE = os.getenv("MONGO_DATABASE")

client: motor.motor_asyncio.AsyncIOMotorClient = motor.motor_asyncio.AsyncIOMotorClient(CONNECTION_STRING)
db = client.get_database(DATABASE)
