import requests


class Specie():
    def __init__(self, name, classification, designation, average_height, skin_colors, hair_colors,
                eye_colors, average_lifespan, homeworld, language, people, films, created, edited, 
                url):
        self.name = name
        self.classification = classification
        self.designation = designation
        self.average_height = average_height
        self.skin_colors = skin_colors
        self.hair_colors = hair_colors
        self.eye_colors = eye_colors
        self.average_lifespan = average_lifespan
        self.homeworld = homeworld
        self.language = language
        self.people = people
        self.films = films
        self.created = created
        self.edited = edited
        self.url = url

    @staticmethod
    def get_all():
        species = []
        url = "https://swapi.dev/api/species/"   
        r = requests.get(url = url)
        data = r.json()
        if type(data['count']/10) is float:
            count = int((data['count']/10) + 1)
        elif type(data['count']/10) is int:
            count = (data['count']/10)

        for i in range(count):
            url = "https://swapi.dev/api/species/?page="+str(i+1)   
            r = requests.get(url = url)
            datas = r.json()
            for j in range(len(datas['results'])):
                name = datas['results'][j]['name']
                classification = datas['results'][j]['classification'] 
                designation = datas['results'][j]['designation'] 
                average_height = datas['results'][j]['average_height'] 
                skin_colors = datas['results'][j]['skin_colors']
                hair_colors = datas['results'][j]['hair_colors']
                eye_colors = datas['results'][j]['eye_colors']
                average_lifespan = datas['results'][j]['average_lifespan'] 
                homeworld = datas['results'][j]['homeworld']
                language = datas['results'][j]['language']
                people = datas['results'][j]['people']
                films = datas['results'][j]['films']
                created = datas['results'][j]['created']
                edited = datas['results'][j]['edited']
                url = datas['results'][j]['url']

                species.append(Specie(name, classification, designation, average_height, skin_colors,
                            hair_colors, eye_colors, average_lifespan, homeworld, language, people,
                            films, created, edited, url))
            
        return species