import requests


class Starship():
    def __init__(self, name, model, manufacturer, cost_in_credits, length, 
                max_atmosphering_speed, crew, passengers, cargo_capacity, 
                consumables, hyperdrive_rating, mglt, starship_class, pilots,
                films, created, edited, score, url):
        self.name = name
        self.model = model 
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed
        self.crew = crew
        self.passengers = passengers
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.hyperdrive_rating = hyperdrive_rating
        self.mglt = mglt 
        self.starship_class = starship_class
        self.pilots = pilots
        self.films = films
        self.created = created
        self.edited = edited
        self.url = url
        self.score = score

    @staticmethod
    def get_all():
        startships = []
        url = "https://swapi.dev/api/starships/"   
        r = requests.get(url = url)
        data = r.json()
        if type(data['count']/10) is float:
            count = int((data['count']/10) + 1)
        elif type(data['count']/10) is int:
            count = (data['count']/10)

        for i in range(count):
            url = "https://swapi.dev/api/starships/?page="+str(i+1)   
            r = requests.get(url = url)
            datas = r.json()
            for j in range(len(datas['results'])):
                name = datas['results'][j]['name']
                model = datas['results'][j]['model'] 
                manufacturer = datas['results'][j]['manufacturer'] 
                cost_in_credits = datas['results'][j]['cost_in_credits'] 
                length = datas['results'][j]['length']
                max_atmosphering_speed = datas['results'][j]['max_atmosphering_speed']
                crew = datas['results'][j]['crew']
                passengers = datas['results'][j]['passengers'] 
                cargo_capacity = datas['results'][j]['cargo_capacity']
                consumables = datas['results'][j]['consumables']
                hyperdrive_rating = datas['results'][j]['hyperdrive_rating']
                mglt = datas['results'][j]['MGLT']
                starship_class = datas['results'][j]['starship_class']
                pilots = datas['results'][j]['pilots']
                films = datas['results'][j]['films']
                created = datas['results'][j]['created']
                edited = datas['results'][j]['edited']
                url = datas['results'][j]['url']
                if hyperdrive_rating != 'unknown' and cost_in_credits != 'unknown':
                    score = str(float(float(hyperdrive_rating)/int(cost_in_credits)))
                else:
                    score = '0.00'

                startships.append(Starship(name, model, manufacturer, cost_in_credits, 
                    length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables,
                    hyperdrive_rating, mglt, starship_class, pilots, films, created, edited, score, url,))
            
        return startships