from src.api import search_lyrics
from src.matching import pick_best_match
from src.files import save_lrc, scan_folder, save_scanned_files
import os
from src.validators import print_separator
def process_folder(folder_path):
    """
    Scan a folder, find best lyric matches, and save results.
    """
    scanned_files = scan_folder(folder_path)
    BASE_PATH = os.getenv('BASE_PATH')
    songs_found_count = 0
    songs_not_found_count = 0
    not_found_songs_list = []
    for song in scanned_files:
        print(f"Scanned File: {song['filename']}")

        candidates = search_lyrics(song["title"], song["artist"], song["album"])
        best_match = pick_best_match(candidates, song["artist"])

        if best_match:
            print(f"Best Match: {best_match['trackName']} by {best_match['artistName']} from album {best_match.get('albumName', 'Unknown')}")
            print_separator()
            save_lrc(best_match)
            songs_found_count += 1
        else:
            print(f"No match found for: {song['filename']}")
            print_separator()
            songs_not_found_count += 1
            not_found_songs_list.append(song['filename']) 

    # Save Songs File Names in Txt Files
    save_scanned_files(not_found_songs_list, os.path.join(BASE_PATH, "not_found_songs.txt"))
    save_scanned_files(scanned_files, os.path.join(BASE_PATH, "found_songs.txt"))
    print(f"Found Songs: {songs_found_count} | Not Found Songs: {songs_not_found_count}")