from src.api import search_lyrics
from src.files import save_lrc
from src.matching import pick_best_match
def main():

    track_name = input("Enter track name: ")
    artist_name = input("Enter artist name: ")

    results = search_lyrics(track_name, artist_name)
    best = pick_best_match(results, artist_name)

    if best is None:
        print(f"No match found for {artist_name} - {track_name}")
        return

    path = save_lrc(best)
    print(f"Song Save in tests/")


if __name__ == "__main__":
    main()