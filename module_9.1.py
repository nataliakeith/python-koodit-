class Car:
    def __init__(self, registration, max_speed, current_speed = 0, travelled_distance = 0):
        self.current_speed = current_speed
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
car = Car('ABC-123', 142)

print(f"The car registration number is {car.registration} and it's maximum speed is {car.max_speed} km/h.")
print(f"The car current speed is {car.current_speed} and it's travelled distance is {car.travelled_distance}")
