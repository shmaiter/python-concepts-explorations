class Dog:
    # class attributes
    species = "Canis familiaris"

    def __init__(self, name, age):
        # instance attributes
        self.name = name
        self.age = age

    # Instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        classname = type(self).__name__
        return f"{classname}(name={self.name!r}, age={self.age!r})"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GolderRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


miles = JackRussellTerrier("Miles", 4)
print(miles.speak("Grrr"))

jim = Bulldog("Jim", 5)
print(jim.speak("Woof"))

goshly = GolderRetriever("Goshly",5)
print(goshly.speak())











