import operator
import random
from streams import Stream

class StreamOperators:

    vowels = [
        "a", "e", "i", "o", "u",
        "A", "E", "I", "O", "U"
    ]
   
    @staticmethod
    def length_comparison(lorem:str, pirate:str)->dict:
        length_data = {
            "lorem": len(lorem),
            "pirate": len(pirate)
        }
        print(f"{max(length_data.items(), key=operator.itemgetter(1))[0]} has the most items.")
        return length_data

 
    @staticmethod
    def skewer(lorem:str, pirate:str)->None:
        lorem_skewer = ""
        pirate_skewer = ""
        for i in range(1):
            lorem_skewer += '-'.join(random.sample(lorem, random.randint(1,len(lorem))))
            pirate_skewer += '-'.join(random.sample(pirate, random.randint(1,len(pirate))))
        print("\n")
        print("Lorem skewer: \n")
        print(lorem_skewer)
        print("\n")
        print("Pirate skewer: \n")
        print(pirate_skewer)
        print("\n")
        length_data = {"lorem":len(lorem_skewer), "pirate":len(pirate_skewer)}
        print(length_data)



StreamOperators.skewer(
    Stream.stream_to_list(Stream.lorem),
    Stream.stream_to_list(Stream.pirate)
)

# print(
#     StreamOperators.length_comparison(
#     Stream.stream_to_list(Stream.lorem),
#     Stream.stream_to_list(Stream.pirate)
#     )
#     )