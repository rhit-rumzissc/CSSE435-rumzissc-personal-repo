import gpiozero as gz
import time
import signal

def playback_pattern(red_led, yellow_led, green_led, pattern):
    print("Playback")
    # playback pattern
    for x in pattern:
        if x == 'r':
            red_led.on()
            time.sleep(0.5)
            red_led.off()
            time.sleep(0.1)
        elif x == 'y':
            yellow_led.on()
            time.sleep(0.5)
            yellow_led.off()
            time.sleep(0.1)
        elif x == 'g':
            green_led.on()
            time.sleep(0.5)
            green_led.off()
            time.sleep(0.1)
    # clear pattern
    pattern.clear()

def append_to_pattern(led, pattern, color):
    print("Appending")
    led.on()
    time.sleep(0.5)
    led.off()
    pattern.append(color)
    print(pattern)

def button_events():
    print ("Button Events")
    pattern = []

    clear_button = gz.Button(25)
    red_button = gz.Button(22)
    yellow_button = gz.Button(23)
    green_button = gz.Button(24)

    red_led = gz.LED(14)
    green_led = gz.LED(18)
    yellow_led = gz.LED(15)

    clear_button.when_pressed = lambda: playback_pattern(red_led, yellow_led, green_led, pattern)
    red_button.when_pressed = lambda: append_to_pattern(red_led, pattern, color = 'r')
    yellow_button.when_pressed = lambda: append_to_pattern(yellow_led, pattern, color = 'y')
    green_button.when_pressed = lambda: append_to_pattern(green_led, pattern, color = 'g')
    
    signal.pause()


def main():
    print("Sequence Repeater")
    button_events()



main()