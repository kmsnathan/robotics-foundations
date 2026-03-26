import random
"""
class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
miles = Dog("Miles",4)
print(miles)

class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
        
    def __str__(self):
        return f"The {self.color} car has {self.mileage:,} miles"

red = Car("red", 3000000)
blue = Car("blue", 2000000000)

print(blue)
print(red)
"""
class Robot:
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
        
    def move(self):
        print(f"{self.name} moving at {self.speed} m/s")
    
    def __repr__(self):
        return f"Robot({self.name!r}, {self.speed})"
        
spot = Robot('Spot',1.5)
#spot.move()

class Sensor:
    def __init__(self,sensor_type):
        self.sensor_type = sensor_type
        
    def read(self):
        if random.random() < 0.4:
            raise ValueError("Sensor returned invalid data")
        return round(random.uniform(0.5, 5.0),2)
    
    def __repr__(self):
        return(f"Sensor({self.sensor_type!r})")  
#my_sensor = Sensor("Lidar")
#print(my_sensor.read())
#print(spot)

class MobileRobot(Robot):
    def __init__(self,name,speed,battery):
        super().__init__(name, speed)
        self.battery = battery
        
    def move(self):
        super.move()
        print(f"Battery: {self.battery}%")
        
square = [x **2 for x in range(10)]
reading = [x*0.1 for x in range(20) if x %2 == 0]

sensor = Sensor("lidar_front")
for i in range(10):
    try:
        reading = sensor.read()
        print(f"Reading: {i+1}: {reading} m") 
    except ValueError as e:
        print(f"[WARNING] Sensor '{sensor.sensor_type}' failed: {e}")
    #finally:
    #    print("Sensor read attempt finished.")