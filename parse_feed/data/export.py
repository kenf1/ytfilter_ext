from models.channel import Channels
from models.feed import VideoEntries
from data.channels import import_channels_json, channel_rss_url
from data.feed import get_xml, parse_xml
from data.filter import import_filters_json, videos_filter_title
from models.filter import Filters


def get_xml_wrapper(channels_json: str, filters_json: str) -> VideoEntries:
    channels: Channels = import_channels_json(channels_json)
    filters: Filters = import_filters_json(filters_json)

    # todo: accept + parse all channels from json
    if channels[0].channel_id:
        url: str = channel_rss_url(channels[0].channel_id)
        raw_xml: str = get_xml(url)

        all_video_entries: VideoEntries = parse_xml(raw_xml)

        # filter: keep + drop
        return videos_filter_title(all_video_entries, filters.keep, filters.drop)
    else:
        raise ValueError("Missing required channel_id from channels json")
