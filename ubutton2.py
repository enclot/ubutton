from machine import Pin, Timer
import time

class Button:

    def __init__(self, gpio, pull):
        self._pin = Pin(gpio, Pin.IN, pull)
        self._pin.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=lambda t:self._button_handler())

        self._invert = True if pull==Pin.PULL_UP else False
        self._pressed = False
        self._timer = Timer(0)
        self._counter = 0
        self._last_pressed = False
        self._last_long_pressed = False
    
    def _button_handler(self):
        self._pressed = True if self._pin.value()!=self._invert else False
        if self._pressed:
            self._timer.init(period=100, mode=Timer.PERIODIC, callback=lambda t:self._timer_handler())
        else:
            self._timer.deinit()
            self._counter = 0
            
    def _timer_handler(self):
        self._counter += 100

    def is_pressed(self):
        return self._pressed

    
    
    def was_long_pressed(self, ms):
        is_long_pressed = self._pressed and self._pressed and self._counter > ms
        changed = self._last_long_pressed != is_long_pressed
        self._last_long_pressed  = is_long_pressed
        return is_long_pressed and changed
        
    def was_clicked(self):
        changed = self._last_pressed != self._pressed
        self._last_pressed = self._pressed
        return  not self._pressed and changed and not self._last_long_pressed


if __name__ == '__main__':

    btn = Button(39, Pin.PULL_UP)
    
    while True:

        if btn.was_clicked():
            print("clicked")
        elif btn.was_long_pressed(1000):
            print("long press")
            
        time.sleep_ms(10)
        
    
