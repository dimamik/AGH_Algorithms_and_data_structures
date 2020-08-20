import math
class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return (self.radius * self.radius * math.pi)

Circle = Circle(50)
print(Circle.area())
