import os
import valkey
from valkey import Valkey


def create_valkey_client() -> valkey.Valkey:
    valkey_uri: str | None = os.getenv("VALKEY_URI")

    if valkey_uri:
        return valkey.from_url(valkey_uri)
    else:
        raise ValueError("Missing VALKEY_URI")


def test_valkey_connection() -> None:
    try:
        # todo: create client outside function
        client: Valkey = create_valkey_client()

        if client.ping():
            print("Connected to Valkey")
        else:
            print("Failed to receive ping response from Valkey")
    except Exception as e:
        print("Error connecting to Valkey:", e)
