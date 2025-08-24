import os
from typing import Optional
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


class MongoConnector:
    mongo_uri: Optional[str]
    mongo_db: Optional[str]
    mongo_coll: Optional[str]
    client: MongoClient
    db: Database
    collection: Collection

    def __init__(self):
        self.mongo_uri = os.getenv("MONGO_URI")
        self.mongo_db = os.getenv("MONGO_DB")
        self.mongo_coll = os.getenv("MONGO_COLL")

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

        self.client = MongoClient(self.mongo_uri)  # type: ignore
        self.db = self.client[self.mongo_db]  # type: ignore
        self.collection = self.db[self.mongo_coll]  # type: ignore
