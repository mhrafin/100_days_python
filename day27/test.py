def add(*arg):
    sum = 0
    for n in arg:
        sum += n
    return sum


# These are arguments
print(add(1, 2, 3, 45, 6, 7, 8, 9, 18))


def calculate(n, **kwargs):
    print(kwargs)
    # {'add': 3, 'multiply': 5}

    n += kwargs["add"]
    print(n)  # 6
    n *= kwargs["multiply"]
    print(n)  # 30


calculate(2, add=4, multiply=5)


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")


car_1 = Car(make="Nissan", model="123")
print(f"{car_1.make = }")  # car_1.make = 'Nissan'
print(f"{car_1.model = }")  # car_1.model = '123'

car_2 = Car(make="Toyota")
print(f"{car_2.make = }")  # car_1.make = 'Toyota'
print(f"{car_2.model = }")  # car_1.model = None
