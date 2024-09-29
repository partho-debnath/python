class Car:
    _total_car = 0

    def __init__(self, brand, year, model, color) -> None:
        print("__init__")
        self.brand = brand
        self.year = year
        self.model = model
        self.color = color
        self.price = None
        Car._total_car += 1

    def total_car_manufacture(cls):
        print(cls._total_car)

    @classmethod
    def reset_total_car(cls):
        cls._total_car = 0

    @classmethod
    def create_car_with_price(cls, brand, year, model, price, color):
        print("Create car with price.")
        a = cls(brand, year, model, color)
        a.price = price
        return a


car_obj1 = Car("BMW", 2024, "bmw-v9", "Black")
car_obj2 = Car("BMW", 2025, "bmw-v10", "Black")
car_obj3 = Car("BMW", 2026, "bmw-v13", "Black")


print("Brand:", car_obj1.brand)
print("Price:", car_obj1.price)

car_obj1.total_car_manufacture()
car_obj3.total_car_manufacture()


# Car.reset_total_car()
car_obj2.reset_total_car()

car_obj1.total_car_manufacture()
car_obj2.total_car_manufacture()
car_obj3.total_car_manufacture()


car_obj4 = Car.create_car_with_price(
    "New",
    2030,
    "new-n1",
    1200,
    "Blue",
)

car_obj4.total_car_manufacture()
print("Price:", car_obj4.price)
print("Brand:", car_obj4.brand)
