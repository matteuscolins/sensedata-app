import requests


class Film():
    def __init__(self, title, episode_id, opening_crawl, director, producer, release_date, 
                    characters, planets, starships, vehicles, species, created, edited, url):
        self.title = title
        self.episode_id = episode_id
        self.opening_crawl = opening_crawl
        self.director = director
        self.producer = producer
        self.release_date = release_date
        self.characters = characters
        self.planets = planets
        self.starships = starships
        self.vehicles = vehicles
        self.species = species
        self.created = created
        self.edited = edited
        self.url = url

    @staticmethod
    def get_all():
        films = []
        url = "https://swapi.dev/api/films/"   
        r = requests.get(url = url)
        data = r.json()
        if type(data['count']/10) is float:
            count = int((data['count']/10) + 1)
        elif type(data['count']/10) is int:
            count = (data['count']/10)

        for i in range(count):
            url = "https://swapi.dev/api/films/?page="+str(i+1)   
            r = requests.get(url = url)
            datas = r.json()
            for j in range(len(datas['results'])):
                title = datas['results'][j]['title']
                episode_id = datas['results'][j]['episode_id'] 
                opening_crawl = datas['results'][j]['opening_crawl'] 
                director = datas['results'][j]['director'] 
                producer = datas['results'][j]['producer']
                release_date = datas['results'][j]['release_date']
                characters = datas['results'][j]['characters']
                planets = datas['results'][j]['planets'] 
                starships = datas['results'][j]['starships']
                vehicles = datas['results'][j]['vehicles']
                species = datas['results'][j]['species']
                created = datas['results'][j]['created']
                edited = datas['results'][j]['edited']
                url = datas['results'][j]['url']

                films.append(Film(title, episode_id, opening_crawl, director, producer,
                            release_date, characters, planets, starships, vehicles, species,
                            created, edited, url))
            
        return films
