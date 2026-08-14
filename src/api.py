import requests

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

    response = requests.get(url, params=params)
    songs = response.json()

    return songs

