from math import sqrt, atan2

# Geomeetriline punkt tasandil klassina

class Punkt:

    def __init__(self, x, y):
        """
        Tekitame punkti koordinaatidel x, y
        """
        # Väärtustame meie objekti (self) atribuudid x ja y
        self.x = x
        self.y = y

    def nihuta(self, dx, dy):
        """
        Nihutab punkti dx ja dy võrra
        """
        self.x = self.x + dx
        self.y = self.y + dy

    def kaugus(self, punkt2):
        """
        Tagastab meie punkti ja punkt2-e vahelise kauguse
        """
        x_kaugus = abs(self.x - punkt2.x)
        y_kaugus = abs(self.y - punkt2.y)
        return sqrt(x_kaugus**2 + y_kaugus**2)
        

class PolaarPunkt(Punkt):
    """
    PolaarPunkt on Punkti alamklass, Punkt on PolaarPunkti ülemklass.
    Alamklass võtab ülemklassi omadused (meetodid) automaatselt üle, aga
    võib defineerida ka oma meetodeid ja olemasolevaid vajadusel ümber defineerida.
    PolaarPunkt lisab kaks meetodit: polaarkaugus() ja polaarnurk()
    """

    def polaarkaugus(self):
        #return sqrt(self.x**2 + self.y**2)
        return self.kaugus(Punkt(0, 0))

    def polaarnurk(self):
        return atan2(self.y, self.x)
    

    

    

if __name__ == "__main__":
    p1 = PolaarPunkt(10, 5) # See kutsub välja meetodit __init__()
    print(p1.x, p1.y)
    p1.nihuta(-10, -20)
    #Punkt.nihuta(p1, -10, -20)
    print(p1.x, p1.y)
    print(p1.kaugus(Punkt(0, 0)))
    p2 = Punkt(100, 200)
    print(p2.kaugus(p1), p1.kaugus(p2))
    print("Punkti p1 polaarnurk radiaanides", p1.polaarnurk())
    
    
