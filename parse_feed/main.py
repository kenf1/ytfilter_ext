from models.channel import Channels
from data.channels import import_channels_json, channel_rss_url
from data.feed import get_xml


def main():
    channels: Channels = import_channels_json("./data/channels_example.json")
    # print(channels[0].channel_name, channels[0].channel_id)

    if channels[0].channel_id:
        url: str = channel_rss_url(channels[0].channel_id)
        raw_xml: str = get_xml(url)
        print(raw_xml)


if __name__ == "__main__":
    main()
