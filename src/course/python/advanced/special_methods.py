from typing import List

class Book():
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

    def __len__(self) -> int:
        return self.pages

    def __del__(self) -> None:
        print("A book object has been deleted")

mybook = Book("Python Rocks!", "Shekhar Ramesh", 159)
print(mybook)
print(len(mybook))


class Student():
    def __init__(self, names: List[str]) -> None:
        self.names = names

    def __str__(self) -> str:
        return f"Students: {', '.join(self.names)}"
    
    def __len__(self) -> int:
        return len(self.names)