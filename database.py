from dotenv import load_dotenv
import pymongo
import os

import pymongo.collection
import pymongo.database
import pymongo.typings
from pymongo import MongoClient

# load mongo info
load_dotenv()
URL = os.getenv("MONGO_URL")
PROT = os.getenv("PORT")
HOSTNAME = os.getenv("HOSTNAME")
PASSWORD = os.getenv("PASSWORD")


class MongoDB:
    def __init__(self, db_name:str) -> None:
        
        self.url = URL
        self.port = PROT
        self.hostname = HOSTNAME
        self.password = PASSWORD
        self.full_url = f"mongodb://{self.hostname}:{self.password}@{self.url}:{self.port}"

        self.db_name = db_name
        self.client = None
        self.db = None
    
    def __enter__(self):
        self.client : MongoClient = MongoClient(self.full_url)
        self.db = self.client[self.db_name]
        return self.db
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            self.client.close()