from db.crud import VideoDatabaseManager
from configs.otel_setup import setup_otel_logging
import logging
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()

    setup_otel_logging()
    logger = logging.getLogger()
    manager = VideoDatabaseManager()

    try:
        logger.info("Starting database query")
        manager.dbquery()
        logger.info("Database query completed")

        logger.info("Starting database prune")
        manager.dbprune()
        logger.info("Database prune completed")
    finally:
        logger.info("Closing MongoDB connection")
        manager.mongo.client.close()
        logger.info("MongoDB connection closed")

    logger.info("Main complete")
