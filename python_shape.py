class Shape():
    def __init__(self, color=""):
        self.color = color
    
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

    def __str__(self):
        return self.color

class Rectangle(Shape):
    def __init__(self, color="", width=0.0, height=0.0):
        super().__init__(color)
        self.width = float(width)
        self.height = float(height)
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height) * 2
    
    def __str__(self):
        return self.color + " " + str(self.width) + " " + str(self.height)
    
test_rectangle = Rectangle('red', 5, 7)
test_rectangle2 = Rectangle('green', 6.6, 7.7)

print("Rectangle area: " + str(test_rectangle.area()))
print("Rectangle str: " + str(test_rectangle.__str__()))
print("Rectangle perimeter: " + str(test_rectangle.perimeter()))

print("Rectangle area: " + str(test_rectangle2.area()))
print("Rectangle str: " + str(test_rectangle2.__str__()))
print("Rectangle perimeter: " + str(test_rectangle2.perimeter()))

