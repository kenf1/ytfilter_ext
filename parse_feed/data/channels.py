import json
from typing import Any


def import_channels_json(filepath: str) -> Any:
    with open(filepath, "r") as file:
        data: Any = json.load(file)
    return data
