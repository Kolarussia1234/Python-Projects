import turtle

def joonista_koch(pikkus,min_pikkus=1):
    


    if pikkus >= min_pikkus:
        turtle.speed(0)


        joonista_koch(pikkus/3,min_pikkus)
        
        turtle.left(60)

        joonista_koch(pikkus/3,min_pikkus)

        turtle.right(120)

        joonista_koch(pikkus/3,min_pikkus)

        turtle.left(60)
        
        joonista_koch(pikkus/3,min_pikkus)

    else:
         turtle.fd(pikkus)

        
        

        

        

    
joonista_koch(600,5)#seda void muidugi muuta :)
        
