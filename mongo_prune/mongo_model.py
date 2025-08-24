import os
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


class MongoConnector:
    mongo_uri: str
    mongo_db: str
    mongo_coll: str
    client: MongoClient
    db: Database
    collection: Collection

    def __init__(self):
        self.mongo_uri: str = os.getenv("MONGO_URI")
        self.mongo_db: str = os.getenv("MONGO_DB")
        self.mongo_coll: str = os.getenv("MONGO_COLL")

        missing = [
            var
            for var, value in [
                ("MONGO_URI", self.mongo_uri),
                ("MONGO_DB", self.mongo_db),
                ("MONGO_COLL", self.mongo_coll),
            ]
            if not value
        ]
        if missing:
            raise EnvironmentError(
                f"Missing environment variables: {', '.join(missing)}"
            )

        self.client: MongoClient = MongoClient(self.mongo_uri)
        self.db: Database = self.client[self.mongo_db]
        self.collection: Collection = self.db[self.mongo_coll]
