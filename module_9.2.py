class Car:
    def __init__(self, registration, max_speed, current_speed = 0, travelled_distance = 0):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0
        return


car = Car('ABC-123', 142)

print(f"The car registration number is {car.registration} and it's maximum speed is {car.max_speed} km/h.")
print(f"The car current speed is {car.current_speed} km/h and it's travelled distance is {car.travelled_distance} km.")

car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
print(f"Car current speed is {car.current_speed} km/h.")
car.accelerate(-200)
print(f"The final speed of the car is {car.current_speed} km/h.")