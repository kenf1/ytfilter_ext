from dotenv import load_dotenv
from typing import List, Dict, Any
from mongo_model import MongoConnector
from response_model import VideoDocument


def main():
    load_dotenv()

    try:
        mongo: MongoConnector = MongoConnector()
        print("Successfully connected to:", mongo.collection)

        videos = []
        for doc in mongo.collection.find({}):
            video = VideoDocument.from_dict(doc)
            videos.append(video)

        dict_list: List[Dict[str, Any]] = [video.to_dict() for video in videos]
        print(dict_list[1])
    except EnvironmentError as e:
        print(f"Environment error: {e}")


if __name__ == "__main__":
    main()
