from gpiozero import DistanceSensor
from magna_karta_controller import MagnaKartaController
from sshkeyboard import listen_keyboard
from time import sleep

magna_karta = MagnaKartaController(speed=1)
sensor = DistanceSensor(echo=10, trigger=25, threshold_distance=0.2)

def main():

    listen_keyboard(
        on_press=on_press,
        on_release=on_release
    )

def on_press(key):
    if key == 'w':
        print(sensor.distance * 100)
        if sensor.distance * 100 > 20:
            magna_karta.forward()
        else:
            magna_karta.stop()
    elif key == 's':
        magna_karta.backward()
    elif key == 'a':
        magna_karta.left()
    elif key == 'd':
        magna_karta.right()
    elif key == 'q':
        magna_karta.front.close()
        magna_karta.back.close()
        quit()

def on_release(key):
    magna_karta.stop()
    pass

def avoid_collision():
    global magna_karta
    magna_karta.left()

def forward():
    global magna_karta
    magna_karta.forward()

if __name__ == "__main__":
    main()
    
# while True:
#     try:
#         continue
#     except KeyboardInterrupt:
#         print("Ending program")
