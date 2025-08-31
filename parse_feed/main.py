import os
from dotenv import load_dotenv
from models.feed import VideoEntries
from data.feed_response import get_xml_wrapper, get_xml_wrapper_debug
from valkey import Valkey
from configs.valkey import create_valkey_client, test_valkey_connection


def main():
    load_dotenv()
    status: str = os.getenv("STATUS", "prod")
    valkey_client: Valkey = create_valkey_client()

    video_entries: VideoEntries = get_xml_wrapper(
        channels_json="./data/channels_example.json",
        filters_json="./data/filters_example.json",
    )

    if status == "debug":
        get_xml_wrapper_debug(video_entries)
        test_valkey_connection()
    else:
        print("Complete")


if __name__ == "__main__":
    main()
