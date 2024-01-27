from gpiozero import Robot

class MagnaKartaController:
    
    def __init__(self, speed: float) -> None:
        self.back = Robot(left=(9, 25), right=(22, 23))
        self.front = Robot(left=(20, 21), right=(26, 13))
        self.speed = speed

    def forward(self):
        self.back.forward(self.speed)
        self.front.forward(self.speed)

    def backward(self):
        self.back.backward(self.speed)
        self.front.backward(self.speed)

    def left(self):
        self.back.left(self.speed)
        self.front.left(self.speed)
    
    def right(self):
        self.back.right(self.speed)
        self.front.right(self.speed)
