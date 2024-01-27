from gpiozero import Robot

class MagnaKartaController:
    
    def __init__(self, speed: float) -> None:
        self.back = Robot(left=(22, 23), right=(9, 25))
        self.front = Robot(left=(26, 13), right=(20, 21))
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

