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

    def hexagon(self, size):
        for _ in range(6):
            self.fd(size)
            self.lt(60)
    
    def circle(self, size):
        super().circle(size)

        
    def octagon(self, size):
        pass

    def spiral(self, size):
        pass

    def star(self, size):
        pass

    # TODO: Hexagon
    # TODO: Octagon
    # TODO: Circle
    # TODO: Spiral
    # TODO: Star
    # TODO: Mosaic
    # TODO: Fractals
    # TODO: Regular Polyhedra

t = MyTurtle()
t.circle(100)
#t.hexagon(100)
#t.square(100)
#t.triangle(50)
mainloop()