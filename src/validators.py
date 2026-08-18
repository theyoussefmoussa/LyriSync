from src.constants import SONG_LENGTH
def get_valid_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
        # Check for exit command
        if user_input.lower() == "exit":
            print("Exiting the program.")
            exit(0)

        # Validate input length
        if len(user_input) > SONG_LENGTH:
            print(f"Input is too long. Please enter a shorter value (max {SONG_LENGTH} characters).")
            continue
         # Check for help command
        if user_input.lower() == "help":
             print("Please enter the requested information. Type 'exit' to quit.")
             print("Ensure your input is concise and relevant.")
             continue

        # return the valid input
        return user_input


def print_separator(char="-", length=30):
    """
    Print a horizontal separator line for readability in terminal output.
    """
    print(char * length)



def get_tag(tags, key):
    """
    Helper function to safely get a tag value from EasyID3 tags.
    Returns the first value if it exists, otherwise returns None.
    """
    value = tags.get(key)
    return value[0] if value else None
