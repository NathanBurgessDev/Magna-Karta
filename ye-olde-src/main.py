from sensor import SensorController
from magna_karta_controller import MagnaKartaController
from signal import pause
from pynput.keyboard import Listener
from time import sleep

magna_karta = MagnaKartaController(speed=1)

def main():
    # sensor_controller = SensorController(
    #    in_range_cb=avoid_collision,
    #    out_of_range_cb=forward
    # )
    # pause()

    with Listener(on_press, on_release) as listener:
        listener.join()

    # while True:
        # try:

        # except:
        #     continue

def on_press(key):
    if key.char == 'w':
        sleep(0.1)
        magna_karta.forward()
    elif key.char == 's':
        sleep(0.1)
        magna_karta.backward()
    elif key.char == 'a':
        sleep(0.1)
        magna_karta.left()
    elif key.char == 'd':
        sleep(0.1)
        magna_karta.right()
    elif key.char == 'q':
        sleep(0.1)
        magna_karta.front.close()
        magna_karta.back.close()
        quit()

def on_release(key):
    # magna_karta.stop()
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
