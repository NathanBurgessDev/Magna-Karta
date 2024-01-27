from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep



def loop():
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns

    with open("../assets/magna-carta.txt", "r") as f:
        for line in f:
            words = line.split(" ")
            for word in words:     
                lcd.clear()
                lcd.cursor(0,0)
                lcd.message(word)
                sleep(1)

    # while(True):         
    #     # lcd.clear()
    #     lcd.setCursor(0,0)  # set cursor position
    #     lcd.message(text) # display Magna Carta
    #     sleep(10)

def destroy():
    lcd.clear()
    
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

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()