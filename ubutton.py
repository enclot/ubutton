from machine import Pin
import time

class Button:

    def __init__(self, gpio, pull):
        self._pin = Pin(gpio, Pin.IN, pull)
        self._changed = False
        self._invert = True if pull==Pin.PULL_UP else False
        self._pressed = False
        self._last_pressed = False
        self._begin_ticks = time.ticks_ms()
        self._last_long_pressed = False
    
    
    def read(self):
        self._last_pressed = self._pressed
        self._pressed = True if self._pin.value()!=self._invert else False
        self._changed = self._last_pressed != self._pressed
        if self._changed:
            self._begin_ticks = time.ticks_ms()
        self._dt_ticks = time.ticks_ms() - self._begin_ticks

    def is_pressed(self):
        return self._pressed
    
    def was_pressed(self):
        return self._pressed and self._changed
    
    def was_released(self):
        return  not self._pressed and self._changed
    
    def was_long_pressed(self, ms):
        is_long_pressed = self._pressed and self._dt_ticks > ms
        changed = self._last_long_pressed != is_long_pressed
        self._last_long_pressed  = is_long_pressed
        return is_long_pressed and changed

    def was_clicked(self):
        return  not self._pressed and self._changed and not self._last_long_pressed


if __name__ == '__main__':

    btn = Button(39, Pin.PULL_UP)
    
    while True:
        btn.read()
        if btn.was_clicked():
            print("clicked")
        elif btn.was_long_pressed(1000):
            print("long press")

            
        time.sleep_ms(10)
        
    