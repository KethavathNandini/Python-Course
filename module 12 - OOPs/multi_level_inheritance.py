class Vehicle:
    company = "~Infinity Motors"

    def __init__(self, n_wheels, n_seats, mileage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return (f"This vehicle is from {Vehicle.company} and has {self.n_wheels} wheels, {self.n_seats} seats and"
                f" {self.mileage} mileage")


# v1 = Vehicle(4 , 8 , 40)
# print(v1.get_details())

class Car(Vehicle):
    def __init__(self, car_type, drive_type, wheels, seats, mileage):
        self.car_type = car_type
        self_drive_type = drive_type
        # Vehicle.__init__(self, 4, 6, 28)
        super().__init__(wheels,seats,mileage)


class ElectricCar(Car):

    def __init__(self,car_type, drive_type, wheels, seats, mileage,battery_capacity, distance_range):
        print("intializing of ElectricCar")
        self.battery_capacity = battery_capacity
        self.distance_range = distance_range
        super().__init__(car_type,drive_type,wheels, seats, mileage)

    def charge(self):
        print(f"Charing the to {self.battery_capacity}")



ec1 = ElectricCar("Sedan" , "Manual" , 4,5,35,100,50)

print(ec1)
print(ec1.get_details())