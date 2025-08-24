from dotenv import load_dotenv
from mongo_model import MongoConnector


def main():
    load_dotenv()

    try:
        mongo: MongoConnector = MongoConnector()
        print("Successfully connected to:", mongo.collection)
    except EnvironmentError as e:
        print(f"Environment error: {e}")


if __name__ == "__main__":
    main()
