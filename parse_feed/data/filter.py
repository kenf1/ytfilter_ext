import json
from typing import List

from models.filter import Filters
from models.feed import VideoEntries


def import_filters_json(filepath: str) -> Filters:
    with open(filepath, "r") as file:
        data = json.load(file)
    return Filters(**data)


def videos_filter_title(
    entries: VideoEntries, keep_filters: List[str], drop_filters: List[str]
) -> VideoEntries:
    keep_filters_lower: List[str] = [f.lower() for f in keep_filters]
    drop_filters_lower: List[str] = [f.lower() for f in drop_filters]

    filtered_entries: VideoEntries = []
    for video in entries:
        title = video.title
        if not title:
            continue
        title_lower = title.lower()

        if keep_filters_lower and not any(f in title_lower for f in keep_filters_lower):
            continue
        if any(f in title_lower for f in drop_filters_lower):
            continue

        filtered_entries.append(video)

    return filtered_entries
