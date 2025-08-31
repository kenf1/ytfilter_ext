import json
from typing import Any, List, Optional
import re

from models.channel import Channels
from models.feed import VideoEntries, print_video_entry
from data.channels import import_channels_json, channel_rss_url
from data.feed_request import get_xml, parse_xml
from models.filter import Filters


def get_xml_wrapper(channels_json: str, filters_json: str) -> VideoEntries:
    channels: Channels = import_channels_json(channels_json)
    filters: Filters = import_filters_json(filters_json)

    # todo: accept + parse all channels from json
    if channels[0].channel_id:
        url: str = channel_rss_url(channels[0].channel_id)
        raw_xml: str = get_xml(url)

        all_video_entries: VideoEntries = parse_xml(raw_xml)

        # filter: include regex
        return videos_filter_title(all_video_entries, filters.keep, filters.drop)
    else:
        raise ValueError("Missing required channel_id from channels json")


# default index 0
def get_xml_wrapper_debug(video_entries: VideoEntries) -> None:
    if len(video_entries) > 0:
        print_video_entry(video_entries[0])
    else:
        print("Empty list")


def import_filters_json(filepath: str) -> Filters:
    with open(filepath, "r") as file:
        data: Any = json.load(file)
    return Filters(**data)


def videos_filter_title(
    entries: VideoEntries,
    keep_filters: Optional[List[str]] = None,
    drop_filters: Optional[List[str]] = None,
) -> VideoEntries:
    drop_filters_lower: List[str] = (
        [f.lower() for f in drop_filters] if drop_filters else []
    )
    filtered_entries: VideoEntries = []

    for video in entries:
        title: str | None = video.title
        if not title:
            continue
        title_lower: str = title.lower()

        if keep_filters:
            if not any(re.search(pattern, title) for pattern in keep_filters):
                continue

        if any(f in title_lower for f in drop_filters_lower):
            continue

        filtered_entries.append(video)

    return filtered_entries
