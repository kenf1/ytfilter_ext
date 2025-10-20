from dotenv import load_dotenv
from typing import List, Dict, Any
from models.mongo_model import MongoConnector
from models.response_model import VideoDocument
from datetime import datetime, timedelta, timezone
import logging


class VideoDatabaseManager:
    def __init__(self) -> None:
        load_dotenv()
        self.logger = logging.getLogger(__name__)
        self.mongo = MongoConnector()
        self.logger.debug("MongoConnector instance created")

    def dbquery(self) -> None:
        try:
            self.logger.debug(f"Connected to collection: {self.mongo.collection.name}")

            videos: List[VideoDocument] = [
                VideoDocument.from_dict(doc) for doc in self.mongo.collection.find({})
            ]

            dict_list: List[Dict[str, Any]] = [video.to_dict() for video in videos]

            if dict_list:
                print(dict_list[1])
                self.logger.debug(f"First entry example: {dict_list[0]}")
            else:
                self.logger.warning("No documents found in collection")

        except EnvironmentError as e:
            self.logger.error(f"Environment error while querying DB: {e}")
        except Exception as e:
            self.logger.exception(f"Unexpected error in dbquery: {e}")

    def dbprune(self) -> None:
        cutoff_date: datetime = datetime.now(timezone.utc) - timedelta(days=14)
        cutoff_iso_str: str = cutoff_date.isoformat()

        try:
            self.logger.info(f"Pruning documents older than {cutoff_iso_str}")
            result = self.mongo.collection.delete_many(
                {"updated": {"$lt": cutoff_iso_str}}
            )
            self.logger.info(f"Deleted {result.deleted_count} documents")
        except Exception as e:
            self.logger.exception(f"Error in dbprune: {e}")
