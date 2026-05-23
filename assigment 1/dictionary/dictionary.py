import json
import os

FILE_NAME = "dictionary.json"

DEFAULT_DICTIONARY = {
    "hello": "hei",
    "cat": "kissa",
    "dog": "koira",
}

def load_dictionary():
    """
    Load dictionary from JSON file.
    If loading fails, use the default dictionary.
    """
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                dictionary = json.load(file)

            print("Dictionary loaded successfully.")
            return dictionary

        except json.JSONDecodeError:
            print("Error: JSON file is corrupted.")

        except OSError as error:
            print(f"Error loading dictionary: {error}")

    print("Using default dictionary.")
    return DEFAULT_DICTIONARY.copy()

def save_dictionary(dictionary):
    """
    Save dictionary to JSON file.
    """
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(
                dictionary,
                file,
                indent=4,
                ensure_ascii=False,
            )

        print("Dictionary saved successfully.")

    except OSError as error:
        print(f"Error saving dictionary: {error}")

def main():
    """
    Main program loop.
    """
    dictionary = load_dictionary()

    print("\nDictionary Application")
    print("Press Enter without typing a word to exit.\n")

    while True:
        word = input("Enter a word: ").strip().lower()

        if word == "":
            break

        if word in dictionary:
            print(f"Translation: {dictionary[word]}")

        else:
            print("Word not found.")
            print("Please input a definition.")

            definition = input("Definition: ").strip()

            if definition != "":
                dictionary[word] = definition
                print("Word added to dictionary.")

            else:
                print("No definition entered.")

        print()

    save_dictionary(dictionary)
    print("Goodbye!")

if __name__ == "__main__":

    main()