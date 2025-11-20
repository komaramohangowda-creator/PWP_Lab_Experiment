from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
circle = Circle(5)
print(f"Area of the circle: {circle.area():.2f}")
print(f"Perimeter of the circle: {circle.perimeter():.2f}")


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

    def apply_discount(self, discount_percent):
        self.price = self.price * (1 - discount_percent / 100)

# Create book objects
book1 = Book("Python Programming", "Mohan", 1000)
book2 = Book("Signals and Systems", "Gowda", 1200)

print("Book 1 details BEFORE discount:")
book1.display_details()

book1.apply_discount(10)

print("\nBook 1 details AFTER 10% discount:")
book1.display_details()

print("\nBook 2 details:")
book2.display_details()
