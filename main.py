from src.api import search_lyrics
from src.files import save_lrc
from src.matching import pick_best_match
from src.validators import get_valid_input
def main():

    track_name = get_valid_input("Enter track name: ")
    artist_name = get_valid_input("Enter artist name: ")

    results = search_lyrics(track_name, artist_name)
    best = pick_best_match(results, artist_name)

    if best is None:
        print(f"No match found for {artist_name} - {track_name}")
        return

    path = save_lrc(best)
    print(f"Song saved in {path}")


if __name__ == "__main__":
    main()