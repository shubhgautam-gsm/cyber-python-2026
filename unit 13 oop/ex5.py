from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod #fixed (FARAJIYAT )
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


    def area2(self):
        return   10* self.radius * self.radius
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Usage of Abstraction
rectangle = Rectangle(5, 4)
print("Area of Rectangle:", rectangle.area())  # Output: Area of Rectangle: 20

circle = Circle(3)
print("Area of Circle:", circle.area2())  # Output: Area of Circle: 28.26

triangle = Triangle(4, 3)
print("Area of Triangle:", triangle.area())  # Output: Area of Triangle: 6.0
MOTO_triangle = Triangle(444, 3555)
print("Area of Triangle:", MOTO_triangle.area())  # Output: Area of Triangle: 6.0





# area=lxb #rectangle
# area=lxl #square
# area=radius*2


election_india='voting machine'
election_america='online'


