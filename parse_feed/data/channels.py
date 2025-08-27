import json
from typing import Any

from models.channel import Channel, Channels


def load_channels_json(filepath: str) -> Any:
    with open(filepath, "r") as file:
        data: Any = json.load(file)
    return data


def convert_to_struct(data: Any) -> Channels:
    transformed: Channels = []

    for item in data:
        channel_name: str = item.get("channel_name")
        channel_id: str = item.get("channel_id")
        transformed.append(Channel(channel_name, channel_id))

    return transformed


# wrapper function
def import_channels_json(filepath: str) -> Channels:
    json_data: Any = load_channels_json(filepath)
    return convert_to_struct(json_data)


def channel_rss_url(channel_id: str) -> str:
    return f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
