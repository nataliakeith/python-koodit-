import random

class Car:

    def __init__(self, registration, max_speed, current_speed = 0, travelled_distance = 0):
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
        self.travelled_distance +=  self.current_speed * hours

cars = []
for i in range(1, 11):
    registration = f"ABC-{i}"
    max_speed = random.randint(100, 200)

    car = Car(registration, max_speed)
    cars.append(car)

while True:
    finished_race = False
    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            finished_race = True
    if finished_race:
        break
print("Registration" "|" "Max speed" "|" "Current speed" "|" "Distance")
for car in cars:
    print(car.registration, "|", car.max_speed, "|", car.current_speed, "|", car.travelled_distance)
