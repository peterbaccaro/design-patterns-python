class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        self.builder.set_seats(4)
        self.builder.set_engine("Gasoline")
        self.builder.set_wheels(4)

    def construct_truck(self):
        self.builder.set_seats(2)
        self.builder.set_engine("Diesel")
        self.builder.set_wheels(6)


class Builder:
    def __init__(self):
        self.product = Product()

    def set_seats(self, seats):
        self.product.seats = seats

    def set_engine(self, engine):
        self.product.engine = engine

    def set_wheels(self, wheels):
        self.product.wheels = wheels

    def get_product(self):
        return self.product


class Product:
    def __init__(self):
        self.seats = None
        self.engine = None
        self.wheels = None

    def __str__(self):
        return f"Seats: {self.seats}, Engine: {self.engine}, Wheels: {self.wheels}"


class CarBuilder(Builder):
    def __init__(self):
        super().__init__()

    def set_engine(self, engine):
        if engine != "Gasoline":
            raise ValueError("Car engine must be gasoline")
        self.product.engine = engine


class TruckBuilder(Builder):
    def __init__(self):
        super().__init__()

    def set_engine(self, engine):
        if engine != "Diesel":
            raise ValueError("Truck engine must be diesel")
        self.product.engine = engine


def client(director):
    car_builder = CarBuilder()
    director.builder = car_builder
    director.construct_car()
    car_product = car_builder.get_product()
    print("Car:", car_product)

    truck_builder = TruckBuilder()
    director.builder = truck_builder
    director.construct_truck()
    truck_product = truck_builder.get_product()
    print("Truck:", truck_product)


if __name__ == '__main__':
    director = Director(None)
    client(director)
