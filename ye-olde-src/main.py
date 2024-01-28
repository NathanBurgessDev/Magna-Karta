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
    while True:
        key = input()
        match key:
            case 'w':
                magna_karta.forward()
            case 's':
                magna_karta.backward()
            case 'a':
                magna_karta.left()
            case 'd':
                magna_karta.right()
            case 'q':
                magna_karta.front.close()
                magna_karta.back.close()
                quit()

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
