from src.api import search_lyrics
from src.matching import pick_best_match
from src.files import save_lrc, scan_folder, save_scanned_files
import os

def process_folder(folder_path):
    """
    Scan a folder, find best lyric matches, and save results.
    """
    scanned_files = scan_folder(folder_path)

    for song in scanned_files:
        print(f"Scanned File: {song['filename']}")

        candidates = search_lyrics(song["title"], song["artist"], song["album"])
        best_match = pick_best_match(candidates, song["artist"])

        if best_match:
            print(f"Best Match: {best_match['trackName']} by {best_match['artistName']} from album {best_match.get('albumName', 'Unknown')}")
            save_lrc(best_match)
        else:
            print(f"No match found for: {song['filename']}")

    save_scanned_files(scanned_files, os.path.join(folder_path, "scanned_files.txt"))
