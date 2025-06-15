class Person:
    def __init__(self, first: str, last:str, age: int, height: float):
        self.first = first
        self.last = last
        self.age = age
        self.height = height
        self.is_happy = True

    def introduce(self) -> None:
        happiness_status = "happy" if self.is_happy else "not feeling happy"
        print(
            f"Hi I'm {self.first}{self.last}."
            f"I'm {self.age} years old, {self.height} tall and {happiness_status}"

        )
