import requests
import xml.etree.ElementTree as ET
from typing import Optional

from models.feed import VideoEntry, VideoEntries


def get_xml(url: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(
            f"Failed to retrieve RSS feed. Status code: {response.status_code}"
        )


def get_text(elem: Optional[ET.Element]) -> Optional[str]:
    return elem.text if elem is not None else None


def get_attr(elem: Optional[ET.Element], attr: str) -> Optional[str]:
    return elem.attrib.get(attr) if elem is not None else None


def parse_xml(xml_str: str) -> VideoEntries:
    # xml feed header, under xmlns
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "yt": "http://www.youtube.com/xml/schemas/2015",
        "media": "http://search.yahoo.com/mrss/",
    }

    root = ET.fromstring(xml_str)
    entries: VideoEntries = []

    for entry in root.findall("atom:entry", ns):
        video = VideoEntry(
            videoId=get_text(entry.find("yt:videoId", ns)),
            title=get_text(entry.find("atom:title", ns)),
            link=get_attr(entry.find("atom:link[@rel='alternate']", ns), "href"),
            description=get_text(entry.find("media:group/media:description", ns)),
            published=get_text(entry.find("atom:published", ns)),
            updated=get_text(entry.find("atom:updated", ns)),
        )
        entries.append(video)

    return entries
