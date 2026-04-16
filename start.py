from turtle import *

class MyTurtle(Turtle):

    def square(self, size):
        for _ in range(4):
            self.fd(size)
            self.lt(90)

    def triangle(self, size):
        for _ in range(3):
            self.fd(size)
            self.lt(120)
    
    # TODO: Hexagon
    # TODO: Octagon
    # TODO: Circle
    # TODO: Spiral
    # TODO: Star
    # TODO: Mosaic
    # TODO: Fractals
    # TODO: Regular Polyhedra

t = MyTurtle()
t.square(100)
t.triangle(50)
mainloop()