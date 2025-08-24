from db.crud import get_mongo_connector, dbquery, dbprune
from models.mongo_model import MongoConnector

if __name__ == "__main__":
    mongo_conn: MongoConnector = get_mongo_connector()
    dbquery(mongo_conn)
    dbprune(mongo_conn)
