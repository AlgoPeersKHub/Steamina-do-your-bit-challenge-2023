"""
## Introduction
   
Meet the Smart Security System – your cool and clever security upgrade! Using an ultrasonic sensor, micro:bit magic, and flashy LEDs, it automatically turns on lights when someone's around. Simple, snazzy, and super smart, it's not just a security system; it's your personal watchdog. 
Step into the future of security with a system that's easy, fun, and always on guard.


## Parts of the Micro:bit Used & Other materials

   Ultraspnic sensor : Utilizing an ultrasonic sensor (sonar.ping()) to measure distance.
   
   Digital Pin Control: Manipulating digital pins (pins.digital_write_pin()) to control external devices or indicators based on the condition specified in the code.

   External LEDs: 

## Programming Concepts
  
   Variable Initialization: The creation and initialization of a variable (distance) to store and manage data during the program's execution.
   
   Displaying Output: The use of a function (basic.show_icon()) to visually represent information on an output device, in this case, the micro:bit's LED display.

   Function Definition: The definition of a function (on_forever()) that encapsulates a set of instructions to be executed. This function runs continuously in a perpetual loop.
 
   Global Variables: The declaration of a global variable (distance) that can be accessed and modified from any part of the code.

   Conditional Statements: The use of conditional statements (if, else) to make decisions based on the measured distance. If the distance is less than 100 centimeters, it takes one set of actions; otherwise, it takes another set of actions.

   Forever Loop: The concept of a perpetual loop (basic.forever()) that ensures the continuous execution of the defined function (on_forever()), allowing the program to run indefinitely.


## Programming Language
   Python

## Coding environment / Text editor
   Mirosoft Makecode (https://makecode.microbit.org/#editor)

## Feel free to comment or contribute

"""

## Project Code / Program

# Initialize the distance variable
distance = 0

# Display the YES icon on the micro:bit
basic.show_icon(IconNames.YES)

# Define the main function that runs forever
def on_forever():
    global distance
    
    # Measure the distance using the ultrasonic sensor
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P2, PingUnit.CENTIMETERS)
    
    # Check if the distance is less than 100 centimeters
    if distance < 100:
        # Display the CONFUSED icon if the distance is less than 100 centimeters
        basic.show_icon(IconNames.CONFUSED)
        
        # Turn on the digital pin P1
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        # Turn off the digital pin P1 if the distance is greater than or equal to 100 centimeters
        pins.digital_write_pin(DigitalPin.P1, 0)

# Run the on_forever function continuously
basic.forever(on_forever)

