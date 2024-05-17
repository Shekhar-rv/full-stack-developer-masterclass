class Circle():
    """A class to represent a circle."""
    pi = 3.14

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle"""
        return self.pi * self.radius * self.radius

    def perimeter(self) -> float:
        """Calculate the perimeter of the circle"""
        return round(2 * self.pi * self.radius, 2)
    

c = Circle(radius=5)
print(c.area())  # 78.5
print(c.perimeter())  # 31.4

class Dog():
    """A class to represent a dog."""
    def __init__(self, name: str, breed: str, age: int) -> None:
        self.name = name
        self.breed = breed
        self.age = age

    def calculate_human_age(self) -> int:
        """Calculate the age of the dog in human years"""
        return self.age * 7
    
dog1 = Dog(name="Hans", breed="German Shepherd", age=7)
print(dog1.calculate_human_age())  # 49