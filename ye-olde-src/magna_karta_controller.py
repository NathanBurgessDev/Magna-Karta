from gpiozero import Robot
from time import sleep

class MagnaKartaController:
    
    def __init__(self, speed: float) -> None:
        self.front = Robot(left=(17, 27), right=(22, 23))
        self.back = Robot(left=(4, 14), right=(15, 18))
        self.speed = speed

    def forward(self):
        self.back.forward(self.speed)
        self.front.forward(self.speed, curve_right=1)


    def backward(self):
        self.back.backward(self.speed)
        self.front.backward(self.speed)


    def left(self):
        # self.back.left(self.speed)
        # self.front.left(self.speed)
        self.back.forward(self.speed)
        self.front.forward(self.speed, curve_left=1)

    
    def right(self):
        self.back.right(self.speed)
        self.front.right(self.speed)


    def stop(self):
        self.back.stop()
        self.front.stop()


