from gpiozero import Robot
from sensor import SensorController
from gpiozero import DistanceSensor

from signal import pause

# class MotorController:

#     def __init__(self) -> None:
#         self.motor = Motor(forward=2, backward=12)

#     def forward(self, speed: int) -> None:
#         self.motor.forward(speed)

#     def backward(self, speed: int) -> None:
#         self.motor.backward(speed)

def main():
    sensor = DistanceSensor(echo=18, trigger=4, threshold_distance=0.2 )
    
    
    #sensor_controller = SensorController(
      #  in_range_cb=printstop,
     #   out_of_range_cb=movecar
    #)
    sensor.when_in_range = printstop
    sensor.when_out_of_range= movecar
    pause()
def avoid_collision(speed: float):
    pass

def printstop():
    print("stopped")

def movecar():
    global car
    print("car")
    

if __name__ == "__main__":
    main()

while True:
    try:
        continue
    except KeyboardInterrupt:
        print("Ending program")
