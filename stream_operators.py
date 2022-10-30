# max(d.items(), key=operator.itemgetter(1))[0]

import operator

#
from streams import Stream
base_stream = Stream("https://swapi.dev/api/people", "https://baconipsum.com/api/?type=meat-and-filler")
star_wars = base_stream.list_getter("star_wars_list")
pork = base_stream.list_getter("pork_list")
#

class StreamOperators:


    @staticmethod
    def length_comparison(**kwargs):
        length_data = {}
        for key, value in kwargs.items():
            length_data[key] = len(value)
            print(f"{key} : {len(value)}")
        print(f"{max(length_data.items(), key=operator.itemgetter(1))[0]} has more items.")
            

StreamOperators.length_comparison(sw = star_wars, p = pork)