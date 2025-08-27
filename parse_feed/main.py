from models.feed import VideoEntries
from data.export import get_xml_wrapper
from models.feed import print_video_entry


def main():
    video_entries: VideoEntries = get_xml_wrapper("./data/channels_example.json")
    print_video_entry(video_entries[0])


if __name__ == "__main__":
    main()
