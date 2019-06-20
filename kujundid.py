import math

# Üks ristkülik

# Muutujad - neid tekib palju, nende sos pole selge
a1 = 2
b1 = 4

# Teine ristkülik
a2 = 9
b2 = 8

# Sõnastik
ristkylik1 = {"a": 2, "b": 4}
ristkylik2 = {"a": 9, "b": 8}

# Muidu hea (üks objekt), aga väärtuse küsimine ja meetodite kirjeldamine/ väljakutse on raske

# print(ristkylik1["a"])  # OO ristkylik1.a oleks lühem kuju

def pindala(rk_sonastik): # Funktsioon/meetod rakendub objektile ja võiks olla objektiga seotud
    return rk_sonastik["a"] * rk_sonastik["b"]

p = pindala(ristkylik1) 


# OO viis: defineerime klassi kuhu need objektid kuuluvad ja mis kirjeldab nende meetodid

class Ristkylik:
    """
    Ristkülikud oma küljepikkuste, pindala ja ümbermõõduga
    """

    def __init__(self, a, b):
        """
        Erimeetod, mis tekitab ja tagastab uue objekti (self).
        Väljakutse on siin definitsioonist erinev: obj = Ristkylik(a, b) 
        """
        self.a = a  # objektile saab lisada atribuute
        self.b = b

    def __repr__(self):
        """
        Stringikirjeldus  objektile. Erimeetod (__ alguses ja lõpus).
        Väljakutse repr(obj), toimub ka print(obj) sees
        """
        return "a: " + str(self.a) + ", b: " + str(self.b)

    def pindala(self):
        """
        Tavaline meetod. Väljakutse kujul obj.pindala()
        Tagastab risküliku pindala.
        """
        return self.a * self.b

    def ymbermoot(self):
        """
        Tavaline meetod. 
        Tagastab risküliku ümbermõõdu.
        """
        return 2 * (self.a + self.b)

    def modifitseeri(self, kordaja):
        """
        Korrutab küljepikkused kordajaga läbi
        Meetod muudab objekti olekut.
        """
        self.a = self.a * kordaja
        self.b = self.b * kordaja


class Ring:

    def __init__(self, r):
        self.r = r

    def pindala(self):
        return math.pi * self.r**2


r1 = Ristkylik(2, 4)
r1.modifitseeri(10)
print(r1)
print("pindala: ", r1.pindala())
print("ümbermõõt: ", r1.ymbermoot())
r2 = Ristkylik(9, 8)
ring_obj = Ring(1)
# Kõikidel kujunditel on meetod pindala(), mis tagastab kujundi pindala.
# Saame krijutada koodi, mis rakendub suvalisele kujundile, kutsub välja
# meetodit pindala(), teadmata, mis klassi see objekt kuulub ja kuidas see
# meetod on realiseeritud. Seda nimetatakse polümorfismiks (paljukujulisus).
# Võimaldab kirjutada koodi, mis rakendub erinevatele klassidele ka klassidele,
# mida koodi kirjutamise ajal olemas polnud.

def summeeri_kujundite_pindala(kujundite_list):
    """
    kujundite_list sisaldab objekte, mis omavad meetodit nimega pindala()
    Tagastame nende kujundite summaarse pindala.
    """ 
    tulem = 0
    for kujund in kujundite_list:
        tulem = tulem + kujund.pindala()
    return tulem
    

kujundid = [r1, r2, ring_obj]
summa = summeeri_kujundite_pindala(kujundid)
print(summa)

print("Ristküliku sisemine sõnastik: ")
for nimi, vaartus in Ristkylik.__dict__.items():
    print(nimi, vaartus)


