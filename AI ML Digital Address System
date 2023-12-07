"""
## Introduction
   Introducing the AI/ML Digital ID Addresses project—a cutting-edge solution revolutionizing the way we manage and secure building information in our city. 
   Watch the LEDs light up as our AI model identifies and tracks each building in the city.

## Parts of the micro:bit used
   Pins: External LEDs connected

## Programming Concepts
   Variables: The digital_id variable is used to store the digital ID received from serial communication.

   Serial Communication: The code uses serial communication to read the digital ID of the buildings from  AI Glitch Platform(A micro:bit of AI).

   Conditional Statements: The if, elif, and else statements are used to check the value of digital_id and perform different actions based on the conditions.

   Functions: The on_forever function is defined to run continuously, handling the main logic of reading the digital ID and taking actions based on the conditions.

   Control Flow: The basic.pause function is used to introduce delays in the program execution.


## Programming Language
   Python

## Coding environment / Text editor and other platforms
   Microsoft Makecode editor (https://makecode.microbit.org/#editor)
   Teachable machine (https://teachablemachine.withgoogle.com/) A platform for building machine learning model.
   A micro:bit of AI from Glitch (https://ai-training.glitch.me/) A platform that interface the micro:bit and teachable machine.

## Feel free to comment or contribute
"""

## Project code or program

# Initialize digital_id variable
digital_id = ""

# Set up serial communication
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE9600)

# Show a heart icon on the micro:bit
basic.show_icon(IconNames.HEART)
basic.clear_screen()

# Define the main function
def on_forever():
    global digital_id
    
    # Read the digital ID from the serial communication
    digital_id = serial.read_string()
    
    # Check the digital ID and perform actions accordingly
    if digital_id == "Digital ID for building 1":
        basic.show_icon(IconNames.HAPPY)
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(5000)
    elif digital_id == "Digital ID for building 2":
        basic.show_icon(IconNames.FABULOUS)
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.pause(5000)
        # Continue with the elif if you have more buildings to assign IDs to?
    else:
        basic.show_icon(IconNames.NO)
        
# Run the main function continuously
basic.forever(on_forever)
