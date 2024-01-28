from gpiozero import Robot

class MagnaKartaController:
    
    def __init__(self, speed: float) -> None:
        self.front = Robot(left=(17, 27), right=(22, 23))
        self.back = Robot(left=(4, 14), right=(15, 18))
        self.speed = speed

    def forward(self):
        self.back.forward(self.speed)
        self.front.forward(self.speed)
        self.back.stop()
        self.front.stop()

    def backward(self):
        self.back.backward(self.speed)
        self.front.backward(self.speed)
        self.back.stop()
        self.front.stop()

    def left(self):
        self.back.left(self.speed)
        self.front.left(self.speed)
        self.back.stop()
        self.front.stop()
    
    def right(self):
        self.back.right(self.speed)
        self.front.right(self.speed)
        self.back.stop()
        self.front.stop()


