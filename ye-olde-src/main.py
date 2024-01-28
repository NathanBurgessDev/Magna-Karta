from sensor import SensorController
from magna_karta_controller import MagnaKartaController
from signal import pause

magna_karta = MagnaKartaController(speed=0.5)

def main():
    # sensor_controller = SensorController(
    #    in_range_cb=avoid_collision,
    #    out_of_range_cb=forward
    # )
    # pause()
    magna_karta.forward()

def avoid_collision():
    global magna_karta
    magna_karta.left()

def forward():
    global magna_karta
    magna_karta.forward()

if __name__ == "__main__":
    main()
    
while True:
    try:
        continue
    except KeyboardInterrupt:
        print("Ending program")
