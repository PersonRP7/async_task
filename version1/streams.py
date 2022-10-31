# https://swapi.dev/api/people
# https://baconipsum.com/api/?type=meat-and-filler
# Stream("https://swapi.dev/api/people", "https://baconipsum.com/api/?type=meat-and-filler")
# from streams import Stream

import requests


class Stream:

    star_wars_list = []
    pork_list = []

    def __init__(self, star_wars_url:str, pork_url:str) -> None:
        self.store_star_wars(star_wars_url)
        self.store_pork(pork_url)

    def remove_whitespace(self, data_list:list)->list:
        """
        Removes all whitespace for any given string in a given list.
        """
        return [item.replace(' ', '') for item in data_list]

    def store_star_wars(self, url:str) -> None:
        """
        https://swapi.dev/api/people 

        requires flattening.
        """
        data = requests.get(url)
        data_json = data.json()
        for i in data_json['results']:
            self.star_wars_list.append(i['name'])
        self.star_wars_list = self.remove_whitespace(self.star_wars_list)


    def store_pork(self, url:str)->None:
        """
        Stores pork in pork_list
        """
        data = requests.get(url)
        data_json = data.json()
        for i in data_json:
            self.pork_list.append(i)
        self.pork_list = self.remove_whitespace(self.pork_list)

    def list_getter(self, list_name) -> list:
        # return self.list_name
        return getattr(self, list_name)



# print(Stream("https://swapi.dev/api/people", "https://baconipsum.com/api/?type=meat-and-filler").pork_list)

# pl2 = [item.replace(' ', '') for item in pl]
# print(pl2)




    

    

