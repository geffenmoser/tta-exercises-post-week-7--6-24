import re
from anagram_checker import AnagramChecker

word_list_url = "https://norvig.com/ngrams/sowpods.txt"
word_list_path = r"C:\Users\geffg\OneDrive\devIns 2024\tta exercises post week 7, 6-24 created repository\tta-exercises-post-week-7--6-24\Week4\Day4\ExercisesXP\pythonProject2\sowpods.txt"

def main():
    anagram_checker = AnagramChecker(word_list_path)

    while True:
        print("Menu:")
        print("1. Input a word")
        print("2. Exit")
        choice = input("Choose an option: ")

        if choice == '2':
            break
        elif choice == '1':
            user_input = input("Enter a word: ").strip()
            if not is_valid_input(user_input):
                print("Invalid input. Please enter a single word containing only alphabetic characters.")
                continue

            if anagram_checker.is_valid_word(user_input):
                anagrams = anagram_checker.get_anagrams(user_input)
                print(f'YOUR WORD: "{user_input.upper()}"')
                print("This is a valid English word.")
                print(f"Anagrams for your word: {', '.join(anagrams)}")
            else:
                print(f'YOUR WORD: "{user_input.upper()}"')
                print("This is not a valid English word.")
        else:
            print("Invalid choice. Please choose 1 or 2.")

def is_valid_input(word):
    return bool(re.match("^[a-zA-Z]+$", word)) and len(word.split()) == 1

if __name__ == "__main__":
    main()
