import re
from collections import Counter


class Text:
    def __init__(self, text):
        self.text = text
        self.words = self._get_words()

    def _get_words(self):
        # Using regex to handle punctuation and split by whitespace
        return re.findall(r'\b\w+\b', self.text.lower())

    def word_frequency(self, word):
        word = word.lower()
        frequency = self.words.count(word)
        if frequency == 0:
            return f"The word '{word}' is not present in the text."
        return frequency

    def most_common_word(self):
        if not self.words:
            return "The text is empty."
        word_counts = Counter(self.words)
        most_common = word_counts.most_common(1)[0]
        return most_common[0]

    def unique_words(self):
        return list(set(self.words))

    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename, 'r') as file:
                text = file.read()
            return cls(text)
        except FileNotFoundError:
            return "The file was not found."

text_instance = Text(
    "This is a sample text. This text is for testing purposes.")

print(f"Frequency of 'text': {text_instance.word_frequency('text')}")
print(f"Most common word: {text_instance.most_common_word()}")
print(f"Unique words: {text_instance.unique_words()}")

file_path = (r"C:\Users\geffg\OneDrive\devIns 2024\tta exercises post week 7, 6-24 created repository\tta-exercises-post-week-7--6-24\Week4\Day4\DailyChallenge\THE STRANGER.txt")
file_text_instance = Text.from_file(file_path)
if isinstance(file_text_instance, Text):
    print(f"Frequency of 'the': {file_text_instance.word_frequency('the')}")
    print(f"Most common word: {file_text_instance.most_common_word()}")
    print(f"Unique words: {file_text_instance.unique_words()}")
else:
    print(file_text_instance)
