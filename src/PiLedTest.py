import RPi.GPIO as GPIO
import socket
from time import sleep
from hal import hal_led as led
from hal import hal_input_switch as switch

GPIO.setmode(GPIO.BCM)


def init():
    led.init()


def set_led_on():
    led.set_output(0, 1)


def set_led_off():
    led.set_output(0, 0)


def blink_led(frequency):
    init()
    try:
        while True:
            ret = switch.read_slide_switch()
            if ret == 1:  # Switch is to the right
                set_led_off()
                sleep(0.5)
            else:  # Switch is to the left
                set_led_on()
                sleep(0.5 / frequency)
    except KeyboardInterrupt:
        set_led_off()


if __name__ == "__main__":
    frequency = 5  # Set the desired initial frequency (e.g., 5Hz)

    try:
        while True:
            ret = switch.read_slide_switch()
            if ret == 1:  # Switch is to the right
                blink_led(10)
                sleep(5)  # Keep LED at 10Hz for 5 seconds
                set_led_off()
            else:  # Switch is to the left
                blink_led(frequency)
    except KeyboardInterrupt:
        set_led_off()

