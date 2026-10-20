import gpiozero as gz
import time
import signal

def basic_on_off():
    print("Basic On / Off")
    green_led = gz.DigitalOutputDevice(18)
    green_led.on()
    time.sleep(3)
    green_led.off()

def fancy_leds():
    print("Fancy LEDs")
    red_led = gz.LED(14)
    green_led = gz.LED(18)
    yellow_led = gz.LED(15)

    #yellow_led.blink(on_time=2, off_time=1, n=3, background=False)
    red_led.blink(on_time=0.3, off_time=0.1)
    time.sleep(0.1)
    yellow_led.blink(on_time=0.3, off_time=0.1)
    time.sleep(0.1)
    green_led.blink(on_time=0.3, off_time=0.1)
    signal.pause()

def led_board():
        #DONE: figure out how to use an LEDBoard for pins 14,15,18
    print("LED Board")
        # contruct it
    ledBoard = gz.LEDBoard(14,15,18)
        # make a loop runs 5 times
    for i in range(1,5):
        # turn on all leds
        ledBoard.on()
        # wait 1 sec
        time.sleep(1)
        # turn off all leds
        ledBoard.off()
        # wait 1 sec
        time.sleep(1)
        # turn on red and green
        ledBoard.value = (1,0,1)
        # wait 1 sec
        time.sleep(1)
        # (extra) turn on only yellow at 0.5 brightness
        ledBoard.value = (0,0.5,0)
        # wait 1 sec
        time.sleep(1)

    

def main():
    print("Leds")
    #basic_on_off()
    #fancy_leds()
    led_board()

main()