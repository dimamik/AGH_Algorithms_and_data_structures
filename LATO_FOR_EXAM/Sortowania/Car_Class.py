class Car:
    def __init__(self,max_speed,speed_units):
        self.max_speed =  max_speed
        self.speed_units = speed_units
    def __repr__(self):
        return "Car with the maximum speed of " + str(self.max_speed) +" " +self.speed_units


class Boat:
    def __init__(self,max_speed):
        self.max_speed = max_speed
    def __repr__(self):
        return "Boat with the maximum speed of " +str(self.max_speed) + " knots"

car = Car(50,"km/h")
boat = Boat(40)
print(boat)