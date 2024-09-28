class Car:
    def __init__(self, brand, year, model, color) -> None:
        self.brand = brand
        self.year = year
        self.model = model
        self.color = color

    def car_info(self):
        return self.brand, self.year, self.model, self.color

    @staticmethod
    def car_price(brand, year, model, color):
        """
        fetch the car price from the api call or database.
        Car price is not related with any car instance or object.
        """
        print("staticmethod ->", brand, year, model, color)
        return 50000


car_obj = Car("BMW", 2024, "bmw-v9", "Black")

print("Car Info:", car_obj.car_info())
print(
    Car.car_price(
        car_obj.brand,
        car_obj.year,
        car_obj.model,
        car_obj.color,
    )
)
print(
    car_obj.car_price(
        car_obj.brand,
        car_obj.year,
        car_obj.model,
        car_obj.color,
    )
)
