class Pet:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

chickenBombone = Pet("Chicken", 2, 1)
print(chickenBombone.__dict__)