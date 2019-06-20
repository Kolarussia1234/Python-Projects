# Tekitame mitu kilpkonna kasutades klasse Screen ja RawTurtle
# Klass on objektide hulk ja omab mehhanismi
# uute objektide tekitamiseks: def __init__, väljakutse Screen()

from turtle import Screen, RawTurtle
from random import randint, choice

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
        konn_i = RawTurtle(ekraan)
        konn_i.up()
        x = randint(-100, 100)
        y = randint(-100, 100)
        konn_i.goto(x, y)
        konn_i.down()
        # Värvime konna juhusliku värviga
        varv = choice(['green', 'brown', 'black', 'red', 'blue'])
        konn_i.color(varv)
        # Lisame konna i konnade hulka
        konnad.append(konn_i)
        
    # Teeme t juhuslikku liikumist juhusliku konnaga
    for ti in range(t):
        suunamuutus = randint(-60, 60)
        konn = choice(konnad)
        konn.left(suunamuutus)
        konn.fd(20)
        

        


if __name__ == "__main__":
    juhuslikud_konnad(n=10, t=200)

    
