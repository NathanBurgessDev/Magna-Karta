from gpiozero import Robot
from sensor import SensorController

# class MotorController:

#     def __init__(self) -> None:
#         self.motor = Motor(forward=2, backward=12)

#     def forward(self, speed: int) -> None:
#         self.motor.forward(speed)

#     def backward(self, speed: int) -> None:
#         self.motor.backward(speed)

def main():
    car = Robot(left=(22, 23), right=(9, 25))
    sensor_controller = SensorController(
        in_range_cb=printstop,
        out_of_range_cb=movecar
    )
    
def avoid_collision(speed: float):
    pass

def printstop():
    print("stopped")

def movecar():
    car.forward(0.5)

if __name__ == "__main__":
    main()

while True:
    try:
        continue
    except KeyboardInterrupt:
        print("Ending program")
