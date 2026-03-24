class Car:
    def __init__(self, registration, max_speed, current_speed=0, travelled_distance=0):
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
        self.registration = registration
        self.max_speed = max_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

class ElectricCar(Car):
    def __init__(self, registration, max_speed, battery):
        super().__init__(registration, max_speed)
        self.battery = battery

class GasolineCar(Car):
    def __init__(self, registration, max_speed, tank):
        super().__init__(registration, max_speed)
        self.tank = tank


electric_car = ElectricCar("ABC-15", 180, 52.2)
electric_car.accelerate(60)
electric_car.drive(3)
print(f"Electric car distance: {electric_car.travelled_distance} km")

gas_car = GasolineCar("ACD-123", 165, 32.3)
gas_car.accelerate(50)
gas_car.drive(3)
print(f"Gasoline car distance: {gas_car.travelled_distance} km")

