import requests


def get_xml(url: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(
            f"Failed to retrieve RSS feed. Status code: {response.status_code}"
        )
