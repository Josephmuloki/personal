class Camera:
    def take_photo(self):
        print ("Taking a photo...")

class Phone:
    def make_call(self):
        print (f"Making a call...")

class Smartphone(Camera, Phone):  
    pass

phone = Smartphone()
phone.take_photo()
phone.make_call()

