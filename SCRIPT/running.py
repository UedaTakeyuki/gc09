# coding:utf-8
# Copy Right Atelier Ueda🐸 © 2016 -
#
# return:  ["/dev/video0", "/dev/video1", ...]

import time
import led

class LED:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def __str__(self):
        pass

    # Start to use LED.
    def use(self, number): #number: LED number 0 or 1
        # release trigger for get control.
        command_str = 'sudo sh -c "echo none > /sys/class/leds/led' + str(number) +'/trigger"'
        p = subprocess.check_call(command_str, shell=True)

    # End to use LED.
    def release(self, number): #number: LED number 0 or 1
        # back to default.
        if number == 0: 
            trigger_str = "mmc0"
        elif number == 1:
            trigger_str = "input"
        command_str = 'sudo sh -c "echo ' + trigger_str + ' > /sys/class/leds/led' + str(number) +'/trigger"'
        p = subprocess.check_call(command_str, shell=True)

    # Turn LED on.
    def on(self, number): #number: LED number 0 or 1
        command_str = 'sudo sh -c "echo 1 > /sys/class/leds/led' + str(number) +'/brightness"'
        p = subprocess.check_call(command_str, shell=True)

    # Turn LED on.
    def off(self, number): #number: LED number 0 or 1
        command_str = 'sudo sh -c "echo 0 > /sys/class/leds/led' + str(number) +'/brightness"'
        p = subprocess.check_call(command_str, shell=True)

    def short(self, number): #number: LED number 0 or 1
        self.on(number)
        time.sleep(0.1)
        self.off(number)
        time.sleep(0.1)

    def long(self, number): #number: LED number 0 or 1
        self.on(number)
        time.sleep(0.3)
        self.off(number)
        time.sleep(0.1)

    def inter_char(self, number): #number: LED number 0 or 1
        self.off(number)
        time.sleep(0.2)

    def inter_word(self, number): #number: LED number 0 or 1
        self.off(number)
        time.sleep(0.6)

if __name__ == '__main__':
    led = LED()
    print "green on."
    led.use(0)
    led.on(0)
    print "red on."
    led.use(1)
    led.on(1)
    print "green off."
    led.off(0)
    led.release(0)
    print "red off."
    led.off(1)
    led.release(1)

    time.sleep(1)

    led.use(0)
    led.on(0)

    led.short(0)
    led.short(0)
    led.short(0)
    led.inter_char(0)
    led.long(0)
    led.long(0)
    led.long(0)
    led.inter_char(0)
    led.short(0)
    led.short(0)
    led.short(0)
    led.inter_word(0)
