from sensor import SensorController
from magna_karta_controller import MagnaKartaController
from signal import pause
import keyboard

magna_karta = MagnaKartaController(speed=1)

def main():
    # sensor_controller = SensorController(
    #    in_range_cb=avoid_collision,
    #    out_of_range_cb=forward
    # )
    # pause()
    while True:
        try:
            if keyboard.is_pressed('w'):
                print("forward")
                magna_karta.forward()
            elif keyboard.is_pressed('s'):
                magna_karta.backward()
            elif keyboard.is_pressed('a'):
                magna_karta.left()
            elif keyboard.is_pressed('d'):
                magna_karta.right()
            elif keyboard.is_pressed('q'):
                magna_karta.front.close()
                magna_karta.back.close()
                quit()
        except:
            continue

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
