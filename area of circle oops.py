class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius 
my_circle = Circle(5)  
circle_area = my_circle.area()  
print(f"The area of the circle is: {circle_area}")
