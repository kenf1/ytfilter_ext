from typing import List
from dataclasses import dataclass


@dataclass
class Channel:
    channel_name: str
    channel_id: str

    def __post_init__(self):
        if self.channel_name is None:
            raise ValueError("channel_name must be provided")
        if self.channel_id is None:
            raise ValueError("channel_id must be provided")


Channels = List[Channel]
