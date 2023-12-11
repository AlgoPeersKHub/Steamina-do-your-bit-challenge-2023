"""
## Introduction.
   Presenting the Smart Bulb powered by micro:bit technology! 
   This innovative project ensures seamless and effortless lighting adjustments based on ambient light conditions. 
   No more fumbling for switches; let the micro:bit light sensor and external LEDs intelligently illuminate your space.


##Parts of the Micro:bit Used
 
  Speaker: Generating sounds or expressions through the device's speaker.

  Pins: Managing the state of LEDs, such as turning them on or off.


## Programming Concepts
   
   Functions: Creating reusable blocks of code with a specific name and functionality.
  
   Conditional Statement : Allows the execution of specific code based on whether a given condition is true or false.
   
   Loops: A structure that repeats a specific block of code indefinitely.
   
   Variable: Allocating memory and assigning an initial value to a variable.
   
   Global variable: A variable that can be accessed and modified from any part of the code.
   
   String comparison: Evaluating whether two strings are equal or not.


## Programing Language
   Python


## Coding environment or Text editor
   Microsoft Makecode (https://makecode.microbit.org/#editor)

""'

## Project Code or Program

# Define the main function that runs forever
def on_forever():
    # Check if the light level is less than 10
    if input.light_level() < 10:
        # Display an LED pattern on the micro:bit
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        
        # Turn on digital pins P0 and P1
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        # If light level is 10 or more, clear the micro:bit display
        basic.clear_screen()
        
        # Turn off digital pins P0 and P1
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)

# Run the on_forever function continuously
basic.forever(on_forever)
