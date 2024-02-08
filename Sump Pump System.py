"""## Introduction
   
   Do you want to know how to prevet flooding in buildings? 
   This project, featuring the micro:bit, water pumps, and sensors, is a high-tech solution designed to prevent flooding in waterlogged areas. 
   Stay dry and secure with our innovative approach to flood control.

## Parts of the Micro:bit Used
   
   Pins: Analog Input (pins.analog_read_pin): Reading analog values from a specified pin (P0) to measure the water level.

   Pins: Digital Output (pins.digital_write_pin): Controlling a digital output pin (P1) to turn it on or off based on the water level condition

   LED  Display (basic.show_icon and basic.show_number): Displaying icons and numeric values on the micro:bit's LED matrix to provide visual feedback.


## Programming Concepts
   
   Variable (water_level): Declaring and using a variable to store and track the water level.

   Function (on_forever): Defining a function that contains the main logic of the program. The function runs continuously in a loop.

   Global Keyword (global water_level): Using the global keyword to declare a global variable within the function, allowing it to be accessed and modified outside the function.

   Conditional Statements (if and else): Checking the water level and executing different code blocks based on whether the water level is above or below a certain threshold.

   Data Logging (datalogger): Including a timestamp in the data log, logging the water level data, and creating a continuous record of the water level over time.
   
   Looping (basic.forever): Running a section of code continuously in an infinite loop, ensuring the program continues to monitor.


## Programming Language
   Python

## Coding environment or Text
   Microsoft Makecode (https://makecode.microbit.org/#editor)

## Feel free to comment or contribute
"""


## Project Code / Program

# Initialize the variable to store the water level
water_level = 0

# This loop runs continuously
def on_forever():
    global water_level
    
    # Include a timestamp in the data log with a format based on minutes
    datalogger.include_timestamp(FlashLogTimeStampFormat.MINUTES)
    
    # Read the analog value from pin P0, representing the water level
    water_level = pins.analog_read_pin(AnalogPin.P0)
    
    # Check if the water level is above or equal to 70
    if water_level >= 70: # Adjust the water level according to the size of your basin.
        # If the water level is high, turn on a digital output on pin P1
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        # If the water level is below 70, display a checkmark icon and turn off the digital output on pin P1
        basic.show_icon(IconNames.YES)
        pins.digital_write_pin(DigitalPin.P1, 0)
    
    # Log the water level data with the timestamp
    datalogger.log(datalogger.create_cv("water level ", water_level))
    
    # Display the current water level on the LED matrix
    basic.show_number(water_level)

# Run the loop forever
basic.forever(on_forever)
