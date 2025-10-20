import os
from dotenv import load_dotenv
from dataclasses import asdict
import streamlit as st

from parse_feed.data.feed_response import get_xml_wrapper
from parse_feed.models.feed import VideoEntries


def main() -> None:
    load_dotenv()
    environment = os.getenv("STATUS", "prod")

    st.title("🎬 Video Entries Dashboard")
    st.caption(f"Environment: **{environment}**")

    video_entries: VideoEntries = get_xml_wrapper(
        channels_json="./data/channels_example.json",
        filters_json="./data/filters_example.json",
    )

    entry_dicts = [asdict(entry) for entry in video_entries]

    st.subheader("Raw Video Entries (JSON)")
    st.json(entry_dicts, expanded=False)

    st.subheader("Tabular View")
    st.dataframe(entry_dicts)

    st.subheader("Detailed Entries")
    for i, entry in enumerate(video_entries, start=1):
        with st.expander(f"Video {i}: {entry.title or '(Untitled)'}"):
            st.write(entry)


if __name__ == "__main__":
    main()
