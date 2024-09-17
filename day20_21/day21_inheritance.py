class Animal:
    def __init__(self) -> None:
        self.num_of_eyes = 2

    def breath(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
        self.num_of_fins = 4

    def breath(self):
        super().breath()
        print("while under water")

    def swim(self):
        print("swimming underwater")


fish = Fish()

print(fish.num_of_eyes)
print(fish.num_of_fins)
fish.breath()
fish.swim()
