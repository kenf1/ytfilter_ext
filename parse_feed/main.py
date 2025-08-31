import os
from dotenv import load_dotenv
from valkey import Valkey

from models.feed import VideoEntries
from data.feed_response import get_xml_wrapper, get_xml_wrapper_debug
from configs.valkey import create_valkey_client, test_valkey_connection
from data.valkey_export import write_valkeydb


def main():
    load_dotenv()
    status: str = os.getenv("STATUS", "prod")
    valkey_client: Valkey = create_valkey_client()

    video_entries: VideoEntries = get_xml_wrapper(
        channels_json="./data/channels_example.json",
        filters_json="./data/filters_example.json",
    )

    # fixed branches: prod (write to db), debug (print output + connection status), everything else
    if status == "debug":
        get_xml_wrapper_debug(video_entries)
        test_valkey_connection()
    elif len(video_entries) > 0:
        write_valkeydb(valkey_client, video_entries)
    else:
        print("Empty list: no new entries")


if __name__ == "__main__":
    main()
