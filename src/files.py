import os
from dotenv import load_dotenv


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