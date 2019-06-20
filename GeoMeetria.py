# Moodul geomeetriliste kujunditega


"""
class Ruut: # Klassi nimi
    
    #Ruudud oma pindala ja ymbermooduga
    

    #Klassi plokkis on klassi meetodid kujul def meetod(self,.....)

    def __init__(self, kylg): # initsialiseerimis meetod, valjakutse on Ruut(kylg)
        self.kylg = kylg # Tekkitame ja vaartustame atribuudi kylg



    def pindala(self):
        #tagastab ruudu pindala
        return self.kylg**2



    def ymbermoot(self):
         #tagastab ruudu ymermoodu
        return 4 * self.kylg


if __name__ == "__main__":
    r1 = Ruut(2)
    print("Pindala:",r1.pindala(),"Ymbermoot:",r1.ymbermoot())
    """


class Ring:
        def __init__(self,raadius):
            self.raadius = raadius



        def pindala(self):
            return self.raadius**2 * 3.14



        def ymbermoot(self):
            return 2 * 3.14 * self.raadius


if __name__ == "__main__"  :
    r1=Ring(10)
    print("Pindala:", r1.pindala(), "Ymbermoot:",r1.ymbermoot())
        
        
