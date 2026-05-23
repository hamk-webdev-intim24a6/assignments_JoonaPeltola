import urllib.request
import urllib.error
import re
from html.parser import HTMLParser

DANGEROUS_WORDS = [
    "bomb",
    "kill",
    "murder",
    "terror",
    "terrorist",
    "terrorists",
    "terrorism"
]

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []

    def handle_data(self, data):
        self.text_parts.append(data)

    def get_text(self):
        return " ".join(self.text_parts)

def count_dangerous_words(text):
    count = 0

    for word in DANGEROUS_WORDS:
        pattern = r"\b" + re.escape(word) + r"\b"
        matches = re.findall(
            pattern,
            text,
            flags=re.IGNORECASE
        )
        count += len(matches)

    return count

def main():
    url = input("Give me a valid URL to download?")

    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        response = urllib.request.urlopen(request)

        content = response.read()

    except urllib.error.URLError as e:
        print(f"Error opening url: {url}")
        print(e)
        return

    except ValueError as e:
        print(f"Error opening url: {url}")
        print(e)
        return

    content_type = response.headers.get_content_type()

    if content_type == "text/html":

        try:
            decoded_content = content.decode("utf-8")
            parser = TextExtractor()
            parser.feed(decoded_content)
            visible_text = parser.get_text()
            count = count_dangerous_words(visible_text)
            print(f"Number of dangerous words: {count}")

        except UnicodeDecodeError:
            print("Doesn't appear to be an HTML file with utf-8 encoding.")

    else:
        print("Doesn't appear to be an HTML file with utf-8 encoding.")
    path = input("Give me a valid path to save the contents?")

    try:
        with open(path, "wb") as file:
            file.write(content)

        print(f"Saving succeeded to: {path}")

    except Exception:
        print("Saving failed.")

if __name__ == "__main__":
    main()