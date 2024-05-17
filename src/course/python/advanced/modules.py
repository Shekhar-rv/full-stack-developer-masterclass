def useful_func():
    print("This is a useful function")


class UsefulClass():
    def __init__(self, message: str):
        self.message = message

    def report(self):
        print(f"Message: {self.message}")