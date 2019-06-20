#tEKITAME MITU KILPKONNA KASUTADES KLASSE sCREEN JA rAWtRURTLE
#Klass on objektide hulk ja omab mehhanismi
#UUTE OBJEKTIDE TEKITAMISEKS: DEF__INIT__. VALJAKUTSE sCREEN()

from turtle import Screen,RawTurtle
from random import randint,choice

def lihtne_demo():
    #tekitame objekti, mis kuulub klassi Screen
    ekraan = Screen()
    #tekitame konna objekti, mis kuulub klassi RawTrutle  ja on ekraani peal
    konn= RawTurtle(ekraan)
    konn.forward(100)
    #tekitame teise konna
    kermit = RawTurtle(ekraan)
    kermit.color("green")
    kermit.left(30)
    kermit.forward(50)
    #liigutame esimest konna
    konn.back(100)

def juhuslikud_konnad(n=10, t=10000):
    """
tekitab n juhuslike konne
    """
    ekraan=Screen()
    konnad=[]
    for i in range(n):
        #paigutame konna i juhuslikudele koordinaatidele
        konn_i = RawTurtle(ekraan)
        konn_i.up()
        x = randint(-100,100)
        y = randint(-100,100)
        konn_i.goto(x, y)
        konn_i.down()
        #lisame konna i konnade hulka
        konnad.append(konn_i)
        #varvilised konnad
        varv = choice(['green','brown','black','blue','red','yellow'])
        konn_i.color(varv)
        #lisame varvilisi konne
        konnad.append(konn_i)
       #teeme tee juhuslikku liikumist juhusliku konnaga
    for ti in range(t):
        suunamuutus = randint(-61,61)
        juhuslikk_indeks = randint(0, n-1)
        konn = choice(konnad)
        konn.left(suunamuutus)
        konn.fd(20)



            
if __name__ == "__main__":
    juhuslikud_konnad()

