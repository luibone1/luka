class Car:

    wheels = 4


    def __init__(self, brand, color, year):

        self.brand = brand

        self.color = color

        self.year = year


# :( yuy-ს გამოყენება მინდა

car1 = Car("BMW", "Black", 2022)
car2 = Car("Toyota", "White", 2021)


print(f"{car1.brand} {car1.wheels}")
print(f"{car2.brand} {car2.wheels}")


car2.wheels = 3


print(car1.wheels)
print(car2.wheels)
print(Car.wheels)

