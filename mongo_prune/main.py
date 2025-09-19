from db.crud import get_mongo_connector, dbquery, dbprune
from models.mongo_model import MongoConnector
from configs.otel_setup import setup_otel_logging
import logging
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    setup_otel_logging()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    mongo_conn: MongoConnector = get_mongo_connector()

    try:
        logger.info("Starting database query")
        dbquery(mongo_conn)
        logger.info("Database query completed")

        logger.info("Starting database prune")
        dbprune(mongo_conn)
        logger.info("Database prune completed")
    finally:
        logger.info("Closing MongoDB connection")
        mongo_conn.client.close()
        logger.info("MongoDB connection closed")

    logger.info("Main complete")
