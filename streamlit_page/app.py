import os
from dotenv import load_dotenv
from dataclasses import asdict
import streamlit as sl

from parse_feed.data.feed_response import get_xml_wrapper
from parse_feed.models.feed import VideoEntries

load_dotenv()
status: str = os.getenv("STATUS", "prod")

video_entries: VideoEntries = get_xml_wrapper(
    channels_json="./data/channels_example.json",
    filters_json="./data/filters_example.json",
)

sl.title("Video Entries Dashboard")
sl.write(f"Environment status: {status}")

dict_entries = [asdict(entry) for entry in video_entries]

sl.subheader("Raw Video Entries (JSON)")
sl.json(dict_entries, expanded=False)  # Collapsed view

sl.subheader("Tabular View")
sl.dataframe(dict_entries)

sl.subheader("Detail for Each Entry")
for i, entry in enumerate(video_entries):
    with sl.expander(f"Video #{i + 1}: {entry.title or '(untitled)'}"):
        sl.write(entry)
