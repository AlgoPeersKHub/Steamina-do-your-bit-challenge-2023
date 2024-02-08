"""
## Introduction
   
   Explore our Accessible Traffic Light project, where safety knows no bounds! 
   This  traffic light is a unique solution for pedestrians, including those with visual impairments and children. 
   With added sound signals for the visually impaired and a friendly stick figure display for kids, crossing roads just got safer and more enjoyable for everyone.


## Parts of the Micro:bit Used
    
    Pins (Digital Pins Control): Turning things on or off (like lights or devices) using the micro:bit's digital pins.

    LEDs: Showing patterns or images on the micro:bit's LED screen.


## Programming Concepts
  
    Looping (for loop): Repeating a set of actions a certain number of times.

    Function: A block of code that performs a specific task or set of tasks.

    Conditional Statements (if statements): Making decisions in code based on certain conditions. If a condition is true, do one thing; if false, do another.

     Event Handling: Managing actions that occur continuously or repeatedly in the program.


## Programming Language
   Python

## Coding Environment / Text Editor
   Microsoft Makecode (https://makecode.microbit.org/#editor)

## Feel free to comment or contribute
"""

## Project Code / Program

def on_forever():
    # Turn on DigitalPin.P0
    pins.digital_write_pin(DigitalPin.P0, 1)
    
    # Play a sound effect four times in the background
    for index in range(4):
        music.play(music.builtin_playable_sound_effect(soundExpression.hello),
                   music.PlaybackMode.IN_BACKGROUND)
    
    # Show a pattern on the LED matrix
    basic.show_leds("""
        . . # . .
        # # # # #
        . . # . .
        . # # # .
        # . # . #
    """)
    
    # Pause for 5 seconds (5000 milliseconds)
    basic.pause(5000)
    basic.pause(5000)
    basic.pause(5000)
    basic.pause(5000)
    basic.pause(5000)
    basic.pause(5000)
    
    # Clear the LED matrix
    basic.clear_screen()
    
    # Turn off DigitalPin.P0 and turn on DigitalPin.P1
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    
    # Pause for 5 seconds
    basic.pause(5000)
    basic.pause(5000)
    
    # Turn off DigitalPin.P1 and turn on DigitalPin.P2
    pins.digital_write_pin(DigitalPin.P1, 0)
    pins.digital_write_pin(DigitalPin.P2, 1)
    
    # Pause for 5 seconds
    basic.pause(5000)
    basic.pause(5000)
    
    # Turn off DigitalPin.P2
    pins.digital_write_pin(DigitalPin.P2, 0)

# Run the function forever
basic.forever(on_forever)
