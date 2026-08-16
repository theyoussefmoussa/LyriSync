from dotenv import load_dotenv
import os
load_dotenv()
from src.api import search_lyrics
from src.files import save_lrc
from src.matching import pick_best_match
from src.validators import get_valid_input
from src.pipeline import process_folder
from src.cli import process_song

def main():
    print("Welcome to the Lyric Sync Tool!")
    print("Type 'exit' to exit the program")

    while True:
        print('-' * 50)
        user_choice = input("Enter '1' for a specific song or '2' for a folder scan: ").strip()

        if user_choice.lower() == 'exit':
            print("Exiting the program.")
            break

        if user_choice == '1':
            process_song()

        elif user_choice == '2':
            inner_choice = get_valid_input("Do you want to scan the default testing folder or specify a folder? (default/specific): ").strip()
            if inner_choice.lower() == 'default':
                folder_path = os.getenv("TESTING_PATH")
                process_folder(folder_path)

            elif inner_choice.lower() == 'specific':
                folder_path = get_valid_input("Enter the folder path: ")
                process_folder(folder_path)

        else:
            print("Invalid choice. Please enter '1' or '2'.")
            continue


if __name__ == "__main__":
    main()