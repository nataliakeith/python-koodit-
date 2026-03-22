class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
        print(f"Floor: {self.current_floor}")
    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
        print(f"Floor: {self.current_floor}")
    def go_to_floor(self, selected_floor):
        while self.current_floor < selected_floor:
            self.floor_up()
        while self.current_floor > selected_floor:
            self.floor_down()

class Building:
    def __init__(self, bottom, top,  n_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []
        for i in range(n_elevators):
            elevator = Elevator(bottom, top)
            self.elevators.append(elevator)

    def run_elevator(self, number, destination_floor):
        elevator = self.elevators[number]
        elevator.go_to_floor(destination_floor)
    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)

b = Building(1, 5, 3)
b.run_elevator(2,4)
b.fire_alarm()