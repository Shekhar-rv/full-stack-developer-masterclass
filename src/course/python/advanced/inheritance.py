class Person():

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def hello(self) -> None:
        print("Hello")
    
    def report(self) -> None:
        print(f"My name is {self.first_name} {self.last_name}")


class Agent(Person):

    def __init__(self, first_name: str, last_name: str, passcode: int) -> None:
        Person.__init__(self, first_name, last_name)
        self.passcode = passcode

    def report(self) -> None:
        print("I'm here")

    def reveal(self):
        if self.passcode == 123:
            print("I'm a secret agent")
        else:
            self.report()

# x = Person("John", "Doe")
# x.report()
y = Agent(first_name="James", last_name="Bond", passcode=123)
y.hello()
y.reveal()

class Animal():

    def __init__(self, name: str, species: str) -> None:
        self.name = name
        self.species = species

    def greet(self) -> None:
        print(f"Hi! My name is {self.name} and I am a {self.species}")

class Dog(Animal):

    def __init__(self, name: str) -> None:
        Animal.__init__(self, name, "Dog") # type: ignore

    def sound(self) -> None:
        print("Woof!")

class Cat(Animal):
    
    def __init__(self, name: str) -> None:
        Animal.__init__(self, name, "Cat")

    def sound(self) -> None:
        print("Meow!")

a = Animal("Rex", "Dog")
a.greet()
d = Dog("Rex")
d.greet()
d.sound()
print(d.species)
c = Cat("Whiskers")
c.greet()
c.sound()
print(c.species)