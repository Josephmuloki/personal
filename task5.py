class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Power: {self.power}")

#app = Appliance("LG" , "100kw") 
#app.show_details()
class WashingMachine(Appliance):
    def __init__(self, brand, power, drum_size):
        super().__init__(brand, power)
        self.drum_size = drum_size

    def show_details(self):
        super().show_details()
        print(f"Drum size: {self.drum_size}") 

app = WashingMachine ("LG" , "100kw", "50cm") 
app.show_details()
    