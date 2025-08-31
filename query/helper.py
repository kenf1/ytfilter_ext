import os
import valkey
from valkey import Valkey
import json
import collections.abc
from typing import Optional, Any


def create_valkey_client() -> valkey.Valkey:
    valkey_uri: Optional[str] = os.getenv("VALKEY_URI")

    if valkey_uri:
        return valkey.from_url(valkey_uri)
    else:
        raise ValueError("Missing VALKEY_URI")


async def get_decode_json(valkey_client: Valkey, key) -> Optional[Any]:
    result = valkey_client.get(key)

    if isinstance(result, collections.abc.Awaitable):
        result = await result

    if result is None:
        return None

    if isinstance(result, bytes):
        result = result.decode("utf-8")

    return json.loads(result)
