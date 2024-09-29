class Car:
    def __init__(self, registration_num, maximum_speed):
        self.registration_num = registration_num
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.distance_travelled = 0

car1 = Car("XYZ-154", 300)
car2 = Car("CBF-984", 250)

print(f"Car with registration number {car1.registration_num}  has {car1.maximum_speed} maximum speed")
print(f"Car with registration number {car2.registration_num}  has {car2.maximum_speed} maximum speed")