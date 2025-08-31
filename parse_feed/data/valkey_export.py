import json
from dataclasses import asdict
from valkey import Valkey
from typing import List, Dict

from models.feed import VideoEntries
from configs.consts import VIDEO_ENTRY_EXPIRY_TIME


# create valkey entry (key = videoId, value = video entry as json), allow O(1) lookup by videoId
def create_videos_dict(video_entries: VideoEntries) -> Dict[str, str]:
    videos_dict: Dict[str, str] = {}

    for entry in video_entries:
        if entry.videoId is not None:
            videos_dict[entry.videoId] = json.dumps(asdict(entry), indent=2)

    return videos_dict


# create valkey list of all videoId, other functions will handle remove expired
def create_videoid_list(video_entries: VideoEntries) -> List[str]:
    video_ids: List[str] = []

    for v in video_entries:
        video_id: str | None = v.videoId
        if video_id:
            video_ids.append(video_id)

    return video_ids


# wrapper: set videoid list + all videos in VideoEntries
def write_valkeydb(valkey_client: Valkey, video_entries: VideoEntries) -> None:
    videoids_list: List[str] = create_videoid_list(video_entries)
    videos_dict: Dict[str, str] = create_videos_dict(video_entries)

    response = valkey_client.set("videoids", json.dumps(videoids_list))
    if response not in ("OK", True):
        raise RuntimeError(f"Failed to set videoids list: {response}")

    for video_id, video_json in videos_dict.items():
        response = valkey_client.set(video_id, video_json, ex=VIDEO_ENTRY_EXPIRY_TIME)
        if response not in ("OK", True):
            raise RuntimeError(
                f"Failed to set video entry for key {video_id}: {response}"
            )

    print("Complete")


# todo: modify all videoId list when expire
