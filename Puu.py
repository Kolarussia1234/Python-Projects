import turtle

def joonista_puu(pikkus,min_pikkus = 1, nurk=90,kahanemine=0.8):
    """
Joonista kaheharulise tavalise puutyve pikkkusega pikkus.
Kui pikkus== min_pikkus, siis rekurrssioon kastetatakse.
Parast puu joonistamist on kilpkonn algpositsioonis
nurk on harude vaheline nurk
kahanemine on reaalarv 0..1 vahel,mis maarab 
    """
    # Joonistan pikkusega tyvi
    turtle.fd(pikkus)
    #Kui pkkus vaiksem voi vordne min_pikkus, siis lopeta too
    if pikkus > min_pikkus:
        #Kui pikkus > kui min_pikkus:
              #Poora kilpokkna poolnurka vasakule.
        turtle.left(nurk/2)
              #Arvuta uus vaiksem pikkus
        uus_pikkus = kahanemine * pikkus
              #Joonista rekurssivselt vasak alampuu
        joonista_puu(uus_pikkus,min_pikkus,nurk,kahanemine)
              #Poora kilpkonna nurga paremale
        turtle.right(nurk)
              #Joonista rekurssivselt parem alampuu
        joonista_puu(uus_pikkus,min_pikkus,nurk,kahanemine)
              #Taasta kilpkonna suun:poolnurka vasakule
        turtle.left(nurk/2)
    #Taasta kilpkonna seisund:pikkus sammu tagasi
    turtle.back(pikkus)
        
turtle.speed(0)
turtle.left(90)
joonista_puu(100,20,30,0.7) 
