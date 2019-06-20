# -*- coding: utf-8 -*-

class Graaf:

    def __init__(self, maatriks):
        self.maatriks = maatriks
    
    def on_seos(self, i, j):
        return bool(self.maatriks[i][j])


    def kaal(self, i, j):
        if self.maatriks[i][j] != 0:
            return self.maatriks[i][j]
        else:
            return None

    def astak(self, tipp):
        """
        Tagastab tipu astaku:
        sealt väjuvate seoste arvu
        """
        return sum(self.maatriks[tipp])

    def tippude_arv(self):
        return len(self.maatriks)

    def teepikkus(self, marsruut):
        """
        Tagastab tippude loendi 'marsruut' teepikkuse.
        Kui marsruut pole korrektne, siis None.
        """
        if len(marsruut) < 2:
            return 0
        tulem = 0
        for alg in range(len(marsruut)-1):
            lopp = alg + 1
            k = self.kaal(marsruut[alg], marsruut[lopp])
            print(alg, lopp, marsruut[alg], marsruut[lopp], k)
            if k == None:
                return None
            else:
                tulem = tulem + k
        return tulem


    def seotud_tipud(self, tipp):
        """
        Tagastab tipuga seotud tippude loendi
        """
        tulem = []
        tippude_arv = len(self.maatriks)
        for i in range(tippude_arv):
            if self.on_seos(tipp, i):
                tulem.append(i)
        return tulem
            
            
    def tee(self, alg, lopp, senine_tee=[]):
        """
        Tagastab mingi suvalise tee tipust alg tippu lopp
        """
        seotud = self.seotud_tipud(alg)
        uus_tee = senine_tee + [alg]
        if lopp in seotud:
            return uus_tee + [lopp]
        else:
            tee_jargmisest = None
            for jargmine in seotud:
                if not jargmine in senine_tee:
                    tee_jargmisest = self.tee(jargmine, lopp, uus_tee)
                    if tee_jargmisest != None:
                        return tee_jargmisest
                
                
        
    def uuenda_kaugused(self, valitu, kylastatud, kaugused):
        """
        Uuenda sõnastikku kaugused nende teedega, mis lisavad valitud tipuni
        viivale teele ühe kaare(seose) külastamata tipuni, juhul kui leitud
        tee on lühem.
        """
        valitu_kaugus, valitu_tee = kaugused[valitu]
        for tipp in self.seotud_tipud(valitu):
            if not tipp in kylastatud:
                kaugus_labi_valitu = valitu_kaugus + self.kaal(valitu, tipp)
                senine_kaugus, senine_tee = kaugused.get(tipp, (10**100, []))
                if kaugus_labi_valitu < senine_kaugus:
                    kaugused[tipp] = (kaugus_labi_valitu, valitu_tee + [tipp])


    def lyhima_teega_tipp(self, kylastatud, kaugused):
        """
        Lühima teega külastamata tipp sõnastikust kaugused
        None, kui ei ole külastamata tippu, milleni viib tee
        """
        senine_lyhim = 10**100 # Lõpmatus
        tulem = None
        for tipp in kaugused:
            if not tipp in kylastatud:
                teepikkus, tee = kaugused[tipp]
                if teepikkus < senine_lyhim:
                    senine_lyhim = teepikkus
                    tulem = tipp
        return tulem

        
    def lyhim_tee(self, alg):
        """
        Dijkstra algoritm
        Tagastab sõnastiku, mis sisaldab lühimaid teid graafi algtipust
        kõikidesse teistesse tippudesse, kuhu algtipust saab jõuda.
        Sõnastiku formaat: {tipu_indeks: (kaugus, [tee]),...}
        """
        kaugused = {alg: (0, [alg])} # Tulem
        kylastatud = []
        valitu = alg
        # Kuni on veel teid, mis viivad külastamata tippudesse
        while valitu != None:
            self.uuenda_kaugused(valitu, kylastatud, kaugused)
            kylastatud.append(valitu)
            valitu = self.lyhima_teega_tipp(kylastatud, kaugused)
        return kaugused

    def __repr__(self):
        """
        Objekti esitus stringina
        """
        return "\n".join([str(x) for x in self.maatriks])


def graaf_failist(fn):
    """
    Loeb failist nimega fn graafi seosemaatriksi.
    Seosemaatriksi read peavad olema failis eraldatud reavahetustega.
    Elemendid peavad olema eraldatud komadega.
    """
    f = open(fn)
    tulem = []
    for failirida in f.readlines():
        tulemirida = []
        for seoseStr in failirida.split(","):
            tulemirida.append(int(seoseStr))
        tulem.append(tulemirida)
    return Graaf(tulem)

def suurim_astak(fn):
    """
    Tagastab suurima astakuga tipu indeksi graafile, 
    mille seosemaatriks on kirjeldatud failis nimega fn.
    """
    graaf = graaf_failist(fn)
    seni_suurim_astak = -1
    for tipu_indeks in range(tippude_arv(graaf)):
        if astak(graaf, tipu_indeks) > seni_suurim_astak:
            seni_suurim_astak = astak(graaf, tipu_indeks)
            tulem = tipu_indeks
    return tulem
        



    
    
if __name__ == "__main__":
    # Positiivne täisarv näitab seose olemasolu ja kaalu
    
    suhete_graaf = [[0, 10, 20, 0],
                   [10, 0, 2, 0],
                   [20, 2, 0, 0],
                   [0, 0, 0, 0]]
    linnade_graaf = [[0, 200, 0, 200, 270],
                     [200, 0, 100, 0, 0],
                     [0, 100, 0, 0, 250],
                     [200, 0, 0, 0 ,0],
                     [270, 0, 250, 0, 0]]

    #print(tee(linnade_graaf, 3, 2))
    g = Graaf(suhete_graaf)
    print(g.lyhim_tee(1))
    print(g.seotud_tipud(1))
    linnaindeksid = {"Tallinn": 0,
                  "Kohtla-Jarve": 1,
                  "Narva": 2,
                  "Parnu": 3,
                  "Tartu": 4}

    def on_tee(linn1, linn2):
        return on_seos(linnade_graaf, linnaindeksid[linn1], linnaindeksid[linn2])

    #print(on_tee("Tallinn", "Kohtla-Jarve"))
    #print(suurim_astak("linnadegraaf.txt"))
    graaf2 = graaf_failist("linnadegraaf.txt")
    print(graaf2)
