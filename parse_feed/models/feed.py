from dataclasses import dataclass
from typing import Optional, List


@dataclass
class VideoEntry:
    videoId: Optional[str]
    title: Optional[str]
    link: Optional[str]
    description: Optional[str]
    published: Optional[str]
    updated: Optional[str]


VideoEntries = List[VideoEntry]


# formatted print
def print_video_entry(video: VideoEntry) -> None:
    print(
        f"VideoEntry:\n"
        f"  videoId:     {video.videoId}\n"
        f"  title:       {video.title}\n"
        f"  link:        {video.link}\n"
        f"  description: {video.description}\n"
        f"  published:   {video.published}\n"
        f"  updated:     {video.updated}"
    )
