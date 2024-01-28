from gpiozero import DistanceSensor
from magna_karta_controller import MagnaKartaController
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from sshkeyboard import listen_keyboard
from time import sleep

magna_karta = MagnaKartaController(speed=1)
sensor = DistanceSensor(echo=10, trigger=25, threshold_distance=0.2)

def main():

    listen_keyboard(
        on_press=on_press,
        on_release=on_release
    )

    PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
    PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
    # Create PCF8574 GPIO adapter.
    try:
        mcp = PCF8574_GPIO(PCF8574_address)
    except:
        try:
            mcp = PCF8574_GPIO(PCF8574A_address)
        except:
            print ('I2C Address Error !')
            exit(1)
    
    lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

    with open("../assets/magna-carta.txt", "r") as f:
        text = f.read()
        for i in range(0, len(text), 16):
            line = text[i:i+16]
            lcd.clear()
            lcd.setCursor(0,0)
            lcd.message(line)
            sleep(1)

def on_press(key):
    if key == 'w':
        print(sensor.distance * 100)
        if sensor.distance * 100 > 40:
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
