class MathOperations:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

    def add(self, *args):
        return sum(args)


# Creating an object and using the overloaded 'add' method
math_obj = MathOperations()

# The latest 'add' method with variable-length arguments will be used
print(math_obj.add(1, 2))  # Output: 3
print(math_obj.add(1, 2, 3))  # Output: 6
print(math_obj.add(1, 2, 3, 4))  # Output: 10
print(math_obj.add(1, 2, 3, 4, 5))  # Output: 15


class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


rec = Shape(3, 5)
cir = Circle(7)
print(rec.area())
print(cir.area())