import turtle
from random import randint, choice

class Frog(turtle.RawTurtle):
    
    def __init__(self, screen, x, y):
        super().__init__(screen)
        self.up()
        self.goto(x, y)
        self.down()
        self.color('green')
    
    def jump(self, dist):
        self.up()
        self.fd(dist)
        self.down()

class MagicFrog(Frog):

    def change_color(self):
        self.color(choice(['black','blue','red','yellow','cyan','magenta','darkgreen']))
        
    def jump(self,dist):
        self.up()
        self.fd(dist)
        self.down()
        self.change_color()
        
    
if __name__ == "__main__":        
    s = turtle.Screen()
    konnad = [Frog(s, 10, 30), MagicFrog(s, 40, 80), MagicFrog(s, 70, 130)]
    for konn in konnad:
        for i in range(9): 
            konn.fd(10)
            konn.jump(10)


    turtle.done()
