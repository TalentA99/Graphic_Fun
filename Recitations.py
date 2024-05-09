#Author: Talent
from face import Face
from random import uniform
class Crowd:

    def __init__(self, size):
        self.size = size
        self.list = []


        for i in range(size):
            x = uniform(0, 400)
            y = uniform(0, 400)
            f = Face(x,y,30)
            self.list.append(f)


    def lookat(self, x, y):
        for face in self.list:
            face.lookat(x,y)


    def draw(self):
        for face in self.list:
            face.draw()
