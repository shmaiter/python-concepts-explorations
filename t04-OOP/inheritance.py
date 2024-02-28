class Parent:
    hair_color = "brown"
    speaks = ["English"]

class Child(Parent):
    hair_color = "purple"

    def __init__(self):
        super().__init__()
        self.speaks.append("German")

miles = Child()
print(miles.hair_color)