from dotenv import load_dotenv
from typing import List, Dict, Any
from models.mongo_model import MongoConnector
from models.response_model import VideoDocument
from datetime import datetime, timedelta, timezone


def get_mongo_connector() -> MongoConnector:
    load_dotenv()
    return MongoConnector()


def dbquery(mongo: MongoConnector) -> None:
    try:
        print("Successfully connected to:", mongo.collection)

        videos = []
        for doc in mongo.collection.find({}):
            video: VideoDocument = VideoDocument.from_dict(doc)
            videos.append(video)

        dict_list: List[Dict[str, Any]] = [video.to_dict() for video in videos]

        # show 1st entry
        print(dict_list[1])
    except EnvironmentError as e:
        print(f"Environment error: {e}")


def dbprune(mongo: MongoConnector) -> None:
    cutoff_date: datetime = datetime.now(timezone.utc) - timedelta(days=14)
    cutoff_iso_str: str = cutoff_date.isoformat()

    result = mongo.collection.delete_many({"updated": {"$lt": cutoff_iso_str}})

    print(f"Deleted {result.deleted_count} documents")
