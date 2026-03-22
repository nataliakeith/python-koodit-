import random

class Car:
    def __init__(self, registration, max_speed, current_speed=0, travelled_distance=0):
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance
        self.registration = registration
        self.max_speed = max_speed

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
    def race_finished(self):
            for car in self.cars:
                if car.travelled_distance >= self.distance:
                    return True
            return False
    def print_status(self):
        print("Registration" "|" "Max speed" "|" "Current speed" "|" "Distance")
        for car in self.cars:
            print(car.registration, "|", car.max_speed, "|", car.current_speed, "|", car.travelled_distance)
cars = []
for i in range(1, 11):
    registration = f"ABC-{i}"
    max_speed = random.randint(100, 200)
    car = Car(registration, max_speed)
    cars.append(car)
race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while True:
    race.hour_passes()
    hours += 1
    if hours % 10 == 0:
        print(f"Status after {hours} hours: ")
        race.print_status()
    if race.race_finished():
        break
print(f"Final status after {hours} hours: ")
race.print_status()

