from dotenv import load_dotenv
from valkey import Valkey
import asyncio
import logging

from helper import create_valkey_client, get_decode_json
from configs import setup_otel_logging


# todo: add struct
async def main():
    load_dotenv()

    setup_otel_logging()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    valkey_client: Valkey = create_valkey_client()

    videoids_res = await get_decode_json(valkey_client, "videoids")
    print(videoids_res)

    if videoids_res:
        single_video = await get_decode_json(valkey_client, videoids_res[0])
        print(single_video)

    logger.info("Query main complete")


if __name__ == "__main__":
    asyncio.run(main())
