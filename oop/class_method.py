class Car:
    _total_car = 0

    def __init__(self, brand, year, model, color) -> None:
        self.brand = brand
        self.year = year
        self.model = model
        self.color = color
        Car._total_car += 1

    def total_car_manufacture(cls):
        print(cls._total_car)

    def reset_total_car(cls):
        cls._total_car = 0


car_obj1 = Car("BMW", 2024, "bmw-v9", "Black")
car_obj2 = Car("BMW", 2025, "bmw-v10", "Black")
car_obj3 = Car("BMW", 2026, "bmw-v13", "Black")

car_obj1.total_car_manufacture()
car_obj3.total_car_manufacture()


Car.reset_total_car(car_obj3)
car_obj1.total_car_manufacture()
car_obj3.total_car_manufacture()
