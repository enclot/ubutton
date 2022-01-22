# ubutton
This is button module for MicroPython.

You can get the status of button click and long press (hold).

I tested it using Atom Lite and MicroPython v1.18 on 2022-01-17; ESP32 module with ESP32.



## ubutton.py

We need to call read() in the main loop.

~~~
btn = Button(39, Pin.PULL_UP)

while True:
    btn.read()
    if btn.was_clicked():
    	print("clicked")
    elif btn.was_long_pressed(1000):
    	print("long press")
    
    time.sleep_ms(10)
~~~



## ubutton2.py

only ESP32

There is no need to call read().But It use Timer(0).

~~~
btn = Button(39, Pin.PULL_UP)

while True:
    if btn.was_clicked():
    	print("clicked")
    elif btn.was_long_pressed(1000):
    	print("long press")
    
    time.sleep_ms(10)
~~~





## Reference

Arduino Button Library   https://github.com/JChristensen/JC_Button

