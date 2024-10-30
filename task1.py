class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        return f"This device is of {self.brand} brand and of model {self.model}."

#dev = Device( "Apple", "Iphone 16 Pro max")
#print(dev.show_info())  
class Smart_phone(Device):
    def __init__(self, brand, model, storage_capacity):
        super().__init__(brand, model)
        self.storage_capacity = storage_capacity

    def show_info(self):
        print (super().show_info (), f"Its storage capacity is {self.storage_capacity}")
    
phone = Smart_phone("Apple", "Iphone 16 Pro max", "556GB")
phone.show_info()