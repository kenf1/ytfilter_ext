from models.channel import Channels
from models.feed import VideoEntries
from data.channels import import_channels_json, channel_rss_url
from data.feed import get_xml, parse_xml


def get_xml_wrapper(channels_json: str) -> VideoEntries:
    channels: Channels = import_channels_json(channels_json)

    # todo: accept + parse all channels from json
    if channels[0].channel_id:
        url: str = channel_rss_url(channels[0].channel_id)
        raw_xml: str = get_xml(url)

        return parse_xml(raw_xml)
    else:
        raise ValueError("Missing required channel_id from channels json")
