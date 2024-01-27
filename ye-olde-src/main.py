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
    car = Robot(left=(8, 7), right=(0, 3))
    sensor_controller = SensorController(
        in_range_cb=print("stopped"),
        out_of_range_cb=car.forward(0.5)
    )

def avoid_collision(speed: float):
    pass

if __name__ == "main":
    main()
