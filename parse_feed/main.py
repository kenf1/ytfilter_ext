from typing import Any

from data.channels import import_channels_json


def main():
    channels: Any = import_channels_json("./data/channels_example.json")
    print(channels[0]["channel_name"], channels[0]["channel_id"])


if __name__ == "__main__":
    main()
