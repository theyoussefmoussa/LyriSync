import os
from pathlib import Path
from dotenv import load_dotenv
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError

from src.validators import get_tag

def save_lrc(song: dict) -> str:
    """
    Save a song's synced lyrics to a .lrc file.
    Returns the path of the saved file.
    """
    load_dotenv()
    output_dir = os.getenv("OUTPUT_DIR")

    filename = f"{song['artistName']} - {song['trackName']}.lrc"
    filename = filename.replace("/", "-")  # avoid path separator in filenames

    full_path = os.path.join(output_dir, filename)
    os.makedirs(output_dir, exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as file:
        file.write(song["syncedLyrics"])

    return full_path

def scan_folder(folder_path):
    """
    Scan a folder for .mp3 files and extract their metadata.
    """
    folder_path = Path(folder_path)
    songs = []

    for file in folder_path.iterdir():
        if file.is_file() and file.suffix.lower() == ".mp3":

            # Skip files with no ID3 tag at all instead of crashing the whole scan
            try:
                tags = EasyID3(file)
            except ID3NoHeaderError:
                print(f"Skipping {file.name}: no ID3 tag found.")
                continue

            audio = MP3(file)

            song = {
                "filename": file.name,
                "title": get_tag(tags, "title"),
                "artist": get_tag(tags, "artist"),
                "album": get_tag(tags, "album"),
                "genre": get_tag(tags, "genre"),
                "year": get_tag(tags, "date"),
                "track": get_tag(tags, "tracknumber"),
                "duration": audio.info.length,
                "bitrate": audio.info.bitrate,
            }
            songs.append(song)

    return songs


def save_scanned_files(songs, output_file):
    """
    Save scanned song info to a text file.
    Handles both song dicts (from scan_folder) and plain filename strings (not-found list).
    """
    with open(output_file, "w", encoding="utf-8") as f:
        for song in songs:
            if isinstance(song, dict):
                line = f"{song['artist']} - {song['title']} ({song['album']}, {song['year']})"
            else:
                line = song
            f.write(line + "\n")