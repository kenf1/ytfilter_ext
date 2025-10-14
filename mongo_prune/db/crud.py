from dotenv import load_dotenv
from typing import List, Dict, Any
from models.mongo_model import MongoConnector
from models.response_model import VideoDocument
from datetime import datetime, timedelta, timezone
import logging

logger = logging.getLogger(__name__)


def get_mongo_connector() -> MongoConnector:
    load_dotenv()  # todo: remove and test
    logger.debug("Creating MongoConnector instance")
    return MongoConnector()


def dbquery(mongo: MongoConnector) -> None:
    try:
        logger.debug(f"Successfully connected to collection: {mongo.collection.name}")

        videos = []
        for doc in mongo.collection.find({}):
            video: VideoDocument = VideoDocument.from_dict(doc)
            videos.append(video)

        dict_list: List[Dict[str, Any]] = [video.to_dict() for video in videos]

        if dict_list:
            print(dict_list[1])
            logger.debug(f"First entry example: {dict_list[0]}")
        else:
            logger.warning("No documents found in collection")
    except EnvironmentError as e:
        logger.error(f"Environment error while querying DB: {e}")
    except Exception as e:
        logger.exception(f"Unexpected error in dbquery: {e}")


def dbprune(mongo: MongoConnector) -> None:
    cutoff_date: datetime = datetime.now(timezone.utc) - timedelta(days=14)
    cutoff_iso_str: str = cutoff_date.isoformat()

    try:
        logger.info(f"Pruning documents older than {cutoff_iso_str}")
        result = mongo.collection.delete_many({"updated": {"$lt": cutoff_iso_str}})
        logger.info(f"Deleted {result.deleted_count} documents")
    except Exception as e:
        logger.exception(f"Error in dbprune: {e}")
