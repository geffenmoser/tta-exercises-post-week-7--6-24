import random

word_list_url = "https://norvig.com/ngrams/sowpods.txt"
word_list_path = r"C:\Users\geffg\OneDrive\devIns 2024\tta exercises post week 7, 6-24 created repository\tta-exercises-post-week-7--6-24\Week4\Day4\ExercisesXP\pythonProject2\sowpods.txt"

import requests

response = requests.get(word_list_url)
with open(word_list_path, 'w') as file:
    file.write(response.text)

def get_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words


def get_random_sentence(length, words):
    random_words = random.sample(words, length)
    sentence = ' '.join(random_words).lower()
    return sentence


def main():
    print(
        "This program generates a random sentence of a specified length from a list of words.")

    try:
        length = int(input(
            "How long do you want the sentence to be? (Enter an integer between 2 and 20): "))
        if length < 2 or length > 20:
            raise ValueError("Invalid length")
    except ValueError as e:
        print(f"Error: {e}. Please enter an integer between 2 and 20.")
        return

    words = get_words_from_file(word_list_path)
    random_sentence = get_random_sentence(length, words)
    print(f"Your random sentence is: {random_sentence}")

main()

#exercise 2

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)

salary = data['company']['employee']['payable']['salary']
print(f"Salary: {salary}")

data['company']['employee']['birth_date'] = '1990-01-01'

with open('updated_data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Updated JSON data saved to 'updated_data.json'")