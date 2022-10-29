import requests
# https://swapi.dev/api/people
# https://baconipsum.com/api/?type=meat-and-filler

class Stream:

    star_wars_list = []
    pork_list = []

    def __init__(self, star_wars_url:str, pork_url:str) -> None:
        self.store_star_wars(star_wars_url)
        self.store_pork(pork_url)

    def store_star_wars(self, url:str) -> None:
        """
        https://swapi.dev/api/people 

        requires flattening.
        """
        data = requests.get(url)
        data_json = data.json()
        for i in data_json['results']:
            self.star_wars_list.append(i['name'])

    def store_pork(self, url:str)->None:
        data = url
        data_json = data.json()
        for i in data_json:
            self.pork_list.append(url)

    def access(self):
        print(self.star_wars_list)
    
        



    

    

