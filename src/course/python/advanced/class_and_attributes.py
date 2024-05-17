class Student():

    planet = 'Earth' # class object attribute

    def __init__(self, name: str, gpa: float):
        self.name = name
        self.gpa = gpa

    def say_hello(self):
        return f'Hello, {self.name} from planet {self.planet}, your GPA is {self.gpa}'
    

student1 = Student(name='John', gpa=3.5)
print(type(student1.name))  # John
print(student1.say_hello())  # Hello, John
student2 = Student(name='Jane', gpa=3.8)
print(student2.say_hello())  # Hello, Jane
print(student2)


class Agent():

    origin = "USA"

    def __init__(self, name: str, height: float, weight: float) -> None:
        self.name = name
        self.height = height
        self.weight = weight


x = Agent(name='James Bond', height=6.0, weight=200)
print(x.name)  # James Bond
print(x.origin)  # USA
print(x.weight)  # 6.0
x.weight = 190
print(x.weight)  # 190