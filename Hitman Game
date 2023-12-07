"""
## Introduction
   🎯Hey there. are you up for a challenge?
    Dive into the Hitman Challenge! Aim, hit the spot, and score points. Stay sharp, and have a blast! 🚀 
    You've got the game code for your micro:bit below—let the fun begin!

## Parts of the micro:bit used
   
   Accelerometer Sensor: Detects the shake gesture through the on_gesture_shake function.

   LEDs (Light Emitting Diodes): Displays various LED patterns in response to the shake gesture through the basic.show_leds function.


## Programming Concepts

Variable: The code uses the variable hits to keep track of the number of hits (shakes).

Function: The on_gesture_shake function is defined to handle the shake gesture. It increments the hits variable, displays the current hit count, and triggers additional actions when the hit count reaches 10.

Global Variable: The global keyword is used to indicate that the variable hits is a global variable, meaning it can be accessed and modified both inside and outside the function.

Conditional Statements: The code includes a conditional statement (if hits == 10) to check if the hit count has reached 10. If true, it plays a sound, displays LED patterns, shows a message, and logs the hit count.

Loops: The for loop is used to iterate four times, displaying different LED patterns during each iteration.

Event Handling: The input.on_gesture function is used to set up an event handler for the shake gesture, linking it to the on_gesture_shake function.


## Programming Language
   Python

## Coding environment / Text editor
   Microsoft Makecode (https://makecode.microbit.org/#editor)


## Feel free to comment or contribute
"""

## Project code / program

hits = 0  # Initialize a variable to count the number of hits

def on_gesture_shake():  # Define a function to execute when the micro:bit is shaken
    global hits  # Declare the variable as global to maintain its state
    hits += 1  # Increment the hits count
    basic.show_number(hits)  # Display the current number of hits

    if hits == 10:  # Check if the hits count reaches 10
            music._play_default_background(music.built_in_playable_melody(Melodies.DADADADUM),
            music.PlaybackMode.IN_BACKGROUND) # Play a built-in melody when 10 hits are reached

       for index in range(4):  # Show a LED pattern in a loop
            basic.show_leds("""
                . . . . .
                . . . . .
                . . . . .
                . # . # .
                . . # . .
                """)
            basic.show_leds("""
                . . . . .
                . . . . .
                # . # . #
                . # # # .
                . . # . .
                """)
            basic.show_leds("""
                # . # . #
                . . . . .
                # . # . #
                . # # # .
                . . # . .
                """)
            basic.show_leds("""
                . . . . .
                . . . . .
                # . # . #
                . # # # .
                . . # . .
                """)
 basic.show_string("Grand Master!")   # Display a message when the Grand Master achievement is reached
    datalogger.log(datalogger.create_cv("Number of Hits", hits))  # Log the number of hits
input.on_gesture(Gesture.SHAKE, on_gesture_shake) # Set up an event handler for the shake gesture
