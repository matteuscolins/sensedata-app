
import requests
from operator import is_not
from functools import partial

class People():
    def __init__(self, name, height, mass, hair_color, skin_color, 
                eye_color, birth_year, gender, homeworld, films,
                species, vehicles, starships, created, edited, url):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld
        self.films = films
        self.species = species
        self.vehicles = vehicles
        self.starships = starships
        self.created = created
        self.edited = edited
        self.url = url

    @staticmethod
    def get_all():
        peoples = []
        url = "https://swapi.dev/api/people/"   
        r = requests.get(url = url)
        data = r.json()
        if type(data['count']/10) is float:
            count = int((data['count']/10) + 1)
        elif type(data['count']/10) is int:
            count = (data['count']/10)

        for i in range(count):
            url = "https://swapi.dev/api/people/?page="+str(i+1)   
            r = requests.get(url = url)
            datas = r.json()
            for j in range(len(datas['results'])):
                name = datas['results'][j]['name']
                height = datas['results'][j]['height'] 
                mass = datas['results'][j]['mass'] 
                hair_color = datas['results'][j]['hair_color'] 
                skin_color = datas['results'][j]['skin_color']
                eye_color = datas['results'][j]['eye_color']
                birth_year = datas['results'][j]['birth_year']
                gender = datas['results'][j]['gender'] 
                homeworld = datas['results'][j]['homeworld']
                films = datas['results'][j]['films']
                species = datas['results'][j]['species']
                vehicles = datas['results'][j]['vehicles']
                starships = datas['results'][j]['starships']
                created = datas['results'][j]['created']
                edited = datas['results'][j]['edited']
                url = datas['results'][j]['url']

                peoples.append(People(name, height, mass, hair_color, skin_color, 
                    eye_color, birth_year, gender, homeworld, films,
                    species, vehicles, starships, created, edited, url))
            
        return peoples

