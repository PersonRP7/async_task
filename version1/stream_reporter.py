from streams import Stream
from stream_operators import StreamOperators

base_stream = Stream("https://swapi.dev/api/people", 
"https://baconipsum.com/api/?type=meat-and-filler",
 "https://pokeapi.co/api/v2/pokemon"
)
star_wars = base_stream.list_getter("star_wars_list")
pork = base_stream.list_getter("pork_list")
pokemon = base_stream.list_getter("pokemon_list")

def reporter()->None:
    print("")

