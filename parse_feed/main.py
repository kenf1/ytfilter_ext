from models.feed import VideoEntries
from data.export import get_xml_wrapper
from models.feed import print_video_entry


def main():
    video_entries: VideoEntries = get_xml_wrapper(
        channels_json="./data/channels_example.json",
        filters_json="./data/filters_example.json",
    )

    if len(video_entries) > 0:
        print_video_entry(video_entries[0])
    else:
        print("Empty list")


if __name__ == "__main__":
    main()
