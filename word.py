import requests
import operator

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

def counter(ls):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for item in ls:
        for letter in item:
            if letter in vowels:
                count += 1
    return count


def many_counter(**kwargs):
    vowel_data = {}
    for key, value in kwargs.items():
        vowel_data[key] = counter(value)
        # print(f"{key} : {counter(value)}")
    print(vowel_data)
    print(f"{max(vowel_data.items(), key=operator.itemgetter(1))[0]} has the most vowels.")


many_counter(sw = star_wars, p = pork)

