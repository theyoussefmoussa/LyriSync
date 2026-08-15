import requests
from src.constants import TIMEOUT
url = "https://lrclib.net/api/search"


def search_lyrics(track_name, artist_name, album_name=None):
    """
    Search lrclib for candidate matches. Returns raw list of results (dicts).
    """

    params = {
        "track_name": track_name,
        "artist_name": artist_name,
    }
    if album_name:
        params['album_name'] = album_name

    try: 
        response = requests.get(
            url, 
            params=params,
            timeout=TIMEOUT
        )
        response.raise_for_status()  # Raise an exception for HTTP errors   
        songs = response.json()
        return songs


    # Errors Types 
    except requests.exceptions.Timeout:
        print("Request timed out.")
        return []

    except requests.exceptions.ConnectionError:
        print("Could not connect to LRCLIB.")
        return []

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
        return []

    except ValueError:
        print("LRCLIB returned invalid JSON.")
        return []

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []
        


