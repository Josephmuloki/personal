class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
    
    def start(self):
        print(f"Start the {self.vehicle_type}")
    
#van = Vehicle("van")
#van.start()

class Car(Vehicle):
    def __init__(self, vehicle_type, number_of_doors):
        super().__init__(vehicle_type)
        self.number_of_doors = number_of_doors

    def close(self):
        super().start()
        print(f"after closing all the {self.number_of_doors} doors")

#van = Car("van", 4)
#van.close()

class ElectricCar(Car):
    def __init__(self, vehicle_type, number_of_doors, battery_capacity):
        super().__init__(vehicle_type, number_of_doors)
        self.battery_capacity =battery_capacity

    def capacity(self):
        super().close()
        print(f"So that a {self.battery_capacity} battery capacity can be achieved.")

van = ElectricCar("van", 4, "100kw")
van.capacity()           
        