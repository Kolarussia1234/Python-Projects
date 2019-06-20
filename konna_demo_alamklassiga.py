# Tekitame mitu kilpkonna kasutades klasse Screen ja RawTurtle
# Klass on objektide hulk ja omab mehhanismi
# uute objektide tekitamiseks: def __init__, väljakutse Screen()

from turtle import Screen, RawTurtle
from random import randint, choice


class Frog(RawTurtle):# Frog on RawTurtle alamklass ja võtab üle selle omadused

    def change_color(self):
        self.color(choice(['black','blue','red','yellow','cyan','magenta','darkgreen']))

    def __init__(self, ekraan, x=0, y=0, color='green'): # Kirjutame olemasoleva meetodi üle
        """ Paiguta värviga color konn asukohale x, y """
        # Kutsun väja ülemklassi initsialiseerimismeetodit: super() viitab ülemklassile
        super().__init__(ekraan)
        self.jumpto(x, y)
        self.color(color)
        
                 
    def jump(self, dist): # Lisame uue meetodi
        """ Konn hüppab kauguse dist """
        self.up()
        self.fd(dist)
        self.down()

    def jumpto(self, x, y): # Lisame uue meetodi
        """ Konn hüppab punkti x,y """
        self.up()
        self.goto(x, y)
        self.down()
        self.change_color()

    


def lihtne_demo():
    # Tekitame objekti, mis kuulub klassi Screen
    ekraan = Screen()
    # Tekitame konna objekti, mis kuulub klassi RawTurtle ja on ekraani peal
    konn = RawTurtle(ekraan)
    konn.forward(100)
    # Tekitame teise konna
    kermit = RawTurtle(ekraan)
    kermit.color('green')
    kermit.left(30)
    kermit.forward(50)
    # Liigutame esimest konna
    konn.back(100)

def juhuslikud_konnad(n=100, t=100):
    """
    Tekitab n juhuslikult liikuvat konna
    """
    ekraan = Screen()
    konnad = []
    for i in range(n):
        # Paigutame konna i juhuslikele koordinaatidele
        # Värvime konna juhusliku värviga
        x = randint(-100, 100)
        y = randint(-100, 100)
        varv = choice(['green', 'brown', 'black', 'red', 'blue'])
        konn_i = Frog(ekraan, x, y, varv)
        # Lisame konna i konnade hulka
        konnad.append(konn_i)
        
    # Teeme t juhuslikku liikumist juhusliku konnaga
    for ti in range(t):
        suunamuutus = randint(-60, 60)
        konn = choice(konnad)
        konn.left(suunamuutus)
        konn.fd(10)
        konn.jump(20)
        

        


if __name__ == "__main__":
    juhuslikud_konnad(n=10, t=200)

    
