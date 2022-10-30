# max(d.items(), key=operator.itemgetter(1))[0]

# from async_task.word import pork_data
import operator
from collections import defaultdict

#
from streams import Stream
base_stream = Stream("https://swapi.dev/api/people", "https://baconipsum.com/api/?type=meat-and-filler")
star_wars = base_stream.list_getter("star_wars_list")
pork = base_stream.list_getter("pork_list")
#

class StreamOperators:

    # vowels = ["a", "e", "i", "o", "u"]
    vowels = [
        "a", "e", "i", "o", "u",
        "A", "E", "I", "O", "U"
    ]

    @staticmethod
    def counter_general(ls:list) ->int:
        """
        Not to be used by itself. Used by vowel_comparison
        as a filter function.
        """
        count = 0
        for item in ls:
            for letter in item:
                if letter in StreamOperators.vowels:
                    count += 1
        return count

    @staticmethod
    def vowel_comparison(**kwargs) ->None:
        """
        Relies on counter_general for looping
        """
        vowel_data = {}
        for key, value in kwargs.items():
            vowel_data[key] = StreamOperators.counter_general(value)
        print(vowel_data)
        print(f"{max(vowel_data.items(), key=operator.itemgetter(1))[0]} has the most vowels.")


    #Indentation on 22?
    @staticmethod
    def length_comparison(**kwargs)->None:
        """
        Example: StreamOperators.length_comparison(sw = star_wars, p = pork)
        Where sw and p are Stream class attributes in the form a flat list.
        """
        length_data = {}
        for key, value in kwargs.items():
            length_data[key] = len(value)
            print(f"{key} : {len(value)}")
        # print(f"{max(length_data.items(), key=operator.itemgetter(1))[0]} has more items.")
        print(f"{max(length_data.items(), key=operator.itemgetter(1))[0]} has the most items.")
            

    @staticmethod
    def count_repeat(word:str, repeating_letter:str, n_of_repeats:int)->bool:
        """
        Not to be used by itself. Used by the counter_more_than
        as a filter function.
        """
        counter = 0
        if word.count(repeating_letter) >= n_of_repeats:
            return True
        return False

    @staticmethod
    def counter_more_than(repeating_letter, n_of_repeats, **kwargs):
        repeated_letter_words = defaultdict(list)
        for key, value in kwargs.items():
            for item in value:
                if StreamOperators.count_repeat(item, repeating_letter, n_of_repeats):
                    repeated_letter_words[key].append(item)
        return repeated_letter_words

# StreamOperators.length_comparison(sw = star_wars, p = pork)
# StreamOperators.vowel_comparison(sw = star_wars, p = pork)
print(StreamOperators.counter_more_than("a", 2, sw = star_wars, p = pork))