class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

class GoldenRetriever(Dog):
    def bark (self, sound="Bark"):
        return super().speak(sound)

alpha = GoldenRetriever("pele",69)
pele_voice= alpha.bark("AFRICAN BACK")
print(pele_voice)