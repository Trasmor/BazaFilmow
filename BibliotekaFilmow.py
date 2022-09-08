from datetime import date
import random

class Movies:
    def __init__(self, title, release, genre, views):
        self.title = title
        self.release =  release
        self.genre = genre
        self.views = views
        
    def play(self):
        self.views += 1

    def __str__(self):
        return f"'{self.title}' ({self.release}) {self.views}"

    def __eq__(self, other):
        return self.title == other.title

class Series(Movies):
    def __init__(self, title, release, genre, views, episode, season):
        super().__init__(title, release, genre, views)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"'{self.title}':S{self.season:02d}E{self.episode:02d} {self.views}"

Film_1 = Movies(title="Incepcja", release=2010, genre="Sci-Fi, Psychologiczne", views=1)
Film_2 = Movies(title="Shrek", release=2001, genre="Animacja, Komedia", views=1)
Film_3 = Movies(title="Fight Club", release=2000, genre="Thriller, Psychologiczny", views=1)
Film_4 = Movies(title="Wyspa Tajemnic", release=2010, genre="Dramat, Thriller", views=1)
Film_5 = Movies(title="Gran Torino", release=2009, genre="Dramat", views=1)

Serial_1 = Series(title="Dr House", release=2004, genre="Dramat, Komedia", views=1, season=4, episode=12)
Serial_2 = Series(title="Breaking Bad", release=2008, genre="Dramat, Kryminał", views=1, season=2, episode=3)
Serial_3 = Series(title="The Waking Dead", release=2010, genre="Dramat, Horror", views=1, season=7, episode=14)
Serial_4 = Series(title="Peaky Blinders", release=2014, genre="Kryminał, Dramat historyczny", views=1, season=6, episode=9)
Serial_5 = Series(title="Czarnobyl", release=2019, genre="Dramat", views=1, season=4, episode=6)

database = [Film_1, Film_2, Film_3, Film_4, Film_5, Serial_1, Serial_2, Serial_3, Serial_4, Serial_5]

def get_movies():
    movies = []
    for obj in database:
        if obj.season > 0:
            movies.append(obj)
    return movies

def get_series():
    series = []
    for obj in database:
        if obj.season >= 1:
            series.append(obj)
    return series

def search(title):
    for i in database:
        if i.title == title:
            return i

def generate_views():
    x = random.choice(database)
    x.views = random.randint(1, 100)
    return x.views

def generate_views_loop():
    for i in range(10):
        generate_views()

def top_titles(obj, content_type='all'):
    if content_type == 'Movies':
        movies = []
        for obj in database:
            if isinstance(obj, Series):
                continue
            movies.append(obj)
        top_titles = sorted(movies, key=lambda movie: movie.views, reverse=True)
        return top_titles[:obj]
    elif content_type == 'Series':
        series = []
        for obj in database:
            if isinstance(obj, Series):
                continue
            series.append(obj)
        top_titles = sorted(series, key=lambda series: series.views, reverse=True)
        return top_titles[:obj]
    else:
        top_titles = sorted(database, key=lambda x: x.views, reverse=True)
        return top_titles[:obj]


if __name__ == '__main__':
    print("Biblioteka filmów")
    print(f"Najpopularniejsze filmy i seriale dnia {date.today():%d.%m.%Y}")
    generate_views_loop()
    for i in top_titles(3):
        print(i)
#Dla mentora
#Random zawsze zwraca conajmniej 2 jedynki w views, nie mam już siły z tym walczyć dlatego wysyłam zadanko niby działające, ale nie na 100% 
print("------------")
print(Serial_1)
print(Serial_2)
print(Serial_3)
print(Serial_4)
print(Serial_5)
print(Film_1)
print(Film_2)
print(Film_3)
print(Film_4)
print(Film_5)