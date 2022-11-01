from streams import Stream
from stream_operators import StreamOperators


base_stream = Stream("https://swapi.dev/api/people", 
"https://baconipsum.com/api/?type=meat-and-filler",
 "https://pokeapi.co/api/v2/pokemon"
)
star_wars = base_stream.list_getter("star_wars_list")
pork = base_stream.list_getter("pork_list")
pokemon = base_stream.list_getter("pokemon_list")


def send_error_email(error_traceback)->str:
    # return f"Sending error email with {error_traceback}"
    print(f"Sending error email with {error_traceback}")


def try_except_decorator(reporting_function):
    """
    Catches any kind of Exception.
    """
    try:
        return reporting_function()
    except Exception as e:
        return send_error_email(e)


def reporter()->None:
    print("LENGTH COMPARISON:")
    print("\n")
    print(StreamOperators.length_comparison(sw = star_wars, p = pork, po = pokemon))
    print("\n")
    print("VOWEL COMPARISON:")
    print(StreamOperators.vowel_comparison(sw = star_wars, p = pork, po = pokemon))
    print("\n")
    print("REPEATING R's COMPARISON:")
    print(StreamOperators.counter_more_than("r", 2, sw = star_wars, p = pork, po = pokemon))
    print("\n")
    print("LONGEST SKEWER:")
    print(StreamOperators.skewer(sw = star_wars, p = pork, po = pokemon))

if __name__ == "__main__":
    try_except_decorator(reporter)




