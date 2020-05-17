import requests

class Planet():
    def __init__(self, name, rotation_period, orbital_period, diameter, climate, gravity,
                terrain, surface_water, population, residents, films, created, edited, url):
        self.name = name 
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.diameter = diameter
        self.climate = climate
        self.gravity = gravity
        self.terrain = terrain
        self.surface_water = surface_water
        self.population = population
        self.residents = residents
        self.films = films
        self.created = created
        self.edited = edited
        self.url = url

    @staticmethod
    def get_all():
        planets = []
        url = "https://swapi.dev/api/planets/"   
        r = requests.get(url = url)
        data = r.json()
        count = (data['count']/10)
        for i in range(int(count)):
            url = "https://swapi.dev/api/planets/?page="+str(i+1)   
            r = requests.get(url = url)
            datas = r.json()
            for j in range(len(datas['results'])):
                name = datas['results'][j]['name']
                rotation_period = datas['results'][j]['rotation_period']
                orbital_period = datas['results'][j]['orbital_period']
                diameter = datas['results'][j]['diameter']
                climate = datas['results'][j]['climate']
                gravity = datas['results'][j]['gravity']
                terrain = datas['results'][j]['terrain']
                surface_water = datas['results'][j]['surface_water']
                population = datas['results'][j]['population']
                residents = datas['results'][j]['residents']
                films = datas['results'][j]['films']
                created = datas['results'][j]['created']
                edited = datas['results'][j]['edited']
                url = datas['results'][j]['url']

                planets.append(Planet(name, rotation_period, orbital_period, diameter, climate,
                            gravity, terrain, surface_water, population, residents, films,
                            created, edited, url))
            
        return planets