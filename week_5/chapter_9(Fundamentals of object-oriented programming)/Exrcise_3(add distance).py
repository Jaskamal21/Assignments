class Car:
    def __init__(self, registration_num, maximum_speed):
        self.registration_num = registration_num
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.distance_travelled = 0

    def add_speed(self, increase):
        new_speed = self.current_speed + increase

        if new_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def get_distance(self, hours):
        new_distance = self.current_speed * hours
        self.distance_travelled += new_distance

car1 = Car("XYZ-154", 300)
car2 = Car("CBF-984", 250)

car1.add_speed(20)
car1.get_distance(5)
print(f"Total distance travelled : {car1.distance_travelled}")

car1.add_speed(30)
car1.get_distance(3)
print(f"Total distance travelled : {car1.distance_travelled}")