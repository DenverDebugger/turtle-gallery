from turtle import *

class MyTurtle(Turtle):

    def square(self, size):
        for _ in range(4):
            self.fd(size)
            self.lt(90)

mainloop()