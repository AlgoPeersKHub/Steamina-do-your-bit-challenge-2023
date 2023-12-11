"""
## Introduction
   Hey User! Meet our Smart Lighting System. It's a cool setup that listens to your voice through the Simply Voice app, made with MIT App Inventor. 
   Want the lights on? Just say it. 
   Time for lights out? Say the word, and it's done. 
   It's not just smart; it's super easy. Welcome to a lighting experience that's as simple as talking! 🌟💬💡


## Parts of the Micro:bit Used
  
   Pins : (Digital Pin Control) Utilizing the pins.digital_write_pin() function to control the state of digital pin P1 (turning it off with 0).

   LEDs: Showing various icons on the micro:bit display using basic.show_icon().

## Programming Concepts
  
   Variable: The creation and initialization of the variable cmd to an empty string ("").

   Function: Defining functions (on_bluetooth_connected(), on_bluetooth_disconnected(), on_uart_data_received()) to encapsulate specific sets of actions.
   
   Global Variable : The use of the global keyword to indicate that the variable cmd is a global variable accessible throughout the program.
 
   Bluetooth Connection Handling: Setting up functions (on_bluetooth_connected(), on_bluetooth_disconnected()) to execute specific actions when Bluetooth is connected or disconnected.

   UART Communication Setup: Initiating the UART service for Bluetooth communication using bluetooth.start_uart_service().

   UART Data Reception and Processing: Reading UART data until a hash delimiter is encountered (bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))) and processing the received command accordingly.

   Conditional Statements: Using if, elif, and else statements to conditionally execute code based on the value of the received command.

   String Comparison: Comparing strings (e.g., cmd.lower() == "on") to determine specific actions based on the received command.

   UART Data Transmission: Sending data back to the connected device using bluetooth.uart_write_string(cmd).


## Programming Language
   Python

## Coding Environment / Text Editor
   Microsoft Makecode (https://makecode.microbit.org/#editor)

## Note: 

"""


# Project Code / Program

# Initialize the command variable
cmd = ""

# Show the ASLEEP icon on the micro:bit display
basic.show_icon(IconNames.ASLEEP)

# Play a giggle sound
soundExpression.giggle.play()

# Turn off the digital pin P1
pins.digital_write_pin(DigitalPin.P1, 0)

# Function to be executed when Bluetooth is connected
def on_bluetooth_connected():
    # Show the HAPPY icon when Bluetooth is connected
    basic.show_icon(IconNames.HAPPY)
    
    # Start the UART service for Bluetooth communication
    bluetooth.start_uart_service()

# Set the function to execute when Bluetooth is connected
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

# Function to be executed when Bluetooth is disconnected
def on_bluetooth_disconnected():
    # Show the SAD icon when Bluetooth is disconnected
    basic.show_icon(IconNames.SAD)

# Set the function to execute when Bluetooth is disconnected
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

# Function to be executed when UART data is received from Bluetooth
def on_uart_data_received():
    global cmd
    
    # Read the received UART data until a hash delimiter is encountered
    cmd = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
    
    # Check the received command and take appropriate actions
    if cmd.lower() == "on":
        pins.digital_write_pin(DigitalPin.P1, 1)
    elif cmd.lower() == "off":
        pins.digital_write_pin(DigitalPin.P1, 0)
    
    # Send the received command back to the connected device
    bluetooth.uart_write_string(cmd)
    
    # Show the HEART icon on the micro:bit display

## This project is part of the simply voice project.
    basic.show_icon(IconNames.HEART)

# Set the function to execute when UART data is received
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)
