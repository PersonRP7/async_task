import requests
import operator
from collections import Counter

def sw_data(url) -> None:
    sw_list = []
    data = requests.get(url)
    data_json = data.json()
    for i in data_json['results']:
        sw_list.append(i['name'])
    return sw_list

def pork_data(url):
    data = requests.get(url)
    data_json = data.json()
    return data_json

# print(pork_data("https://baconipsum.com/api/?type=meat-and-filler"))

star_wars = sw_data("https://swapi.dev/api/people")
pork = pork_data("https://baconipsum.com/api/?type=meat-and-filler")

# def mt_counter(ls, letter):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     count = 0
#     for item in ls:
#         for letter in item:
#             if letter in vowels:
#                 count += 1
#     return count

# def mt_counter(ls, letter):
#     [i for i,j in Counter(ls).items() if j>1]

def count(word, repeating_letter, n_of_repeats):
    counter = 0
    if word.count(repeating_letter) >= n_of_repeats:
        return True
    return False

# print(count("wwoorrdd", "r", 2))


def counter_mt(repeating_letter, n_of_repeats, **kwargs):
    repeated_letter_words = {}
    for key, value in kwargs.items():
        for item in value:
            if count(item, repeating_letter, n_of_repeats):
                repeated_letter_words[key] = item 
    return repeated_letter_words

print(counter_mt("a", 2, sw = star_wars, p = pork))

# def counter_mt(repeating_letter, n_of_repeats, **kwargs):
#     repeated_letter_words = {}
#     for key, value in kwargs.items():
#         for item in value:
#             if any(repeating_letter in s for s in value):
#                 repeated_letter_words[key] = [item]
#     return repeated_letter_words

# print(counter_mt("a", 2, sw = star_wars, p = pork))