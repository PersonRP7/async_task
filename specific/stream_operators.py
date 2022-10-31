import operator
from streams import Stream

class StreamOperators:

   
    @staticmethod
    def length_comparison(lorem:str, pirate:str)->dict:
        length_data = {
            "lorem": len(lorem),
            "pirate": len(pirate)
        }
        print(f"{max(length_data.items(), key=operator.itemgetter(1))[0]} has the most items.")
        return length_data

# print(
#     StreamOperators.length_comparison(
#     Stream.stream_to_list(Stream.lorem),
#     Stream.stream_to_list(Stream.pirate)
#     )
#     )