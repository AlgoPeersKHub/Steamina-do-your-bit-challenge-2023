"""
## Introduction
   Have you ever wondered how technology can revolutionize everyday tasks, even something as simple as throwing away garbage? The Smart Bin projectcode is below to show you just that! 
   In this exciting project, you'll be combining the power of micro:bit, sensors, and a touch of innovation to create a Smart Bin that not only helps in waste disposal but also contributes to a cleaner, smarter environment.

## Micro:bit parts and External components Used
   Micro:bit Edge connector pins : Provide extra pin for the sensor and motor to be connected.

   Micro:bit LEDs : Displays the distance measured by the ultrasonic sensor.
   
   Ultrasonic sensor : Measures the distance of the person approaching the bin. It triggers the bin to open or close based on the user's proximity, ensuring a touchless and convenient disposal process.
 
   Servo motor : Facilitates automated lid opening or closing.

## Programming language
   Python

## Programming concepts
   Variables: The distance variable is used to store the distance calculated by the ultrasonic sensor.
  
   Functions: The on_forever function is a forever loop that continuously reads the distance from the ultrasonic sensor, displays it on the micro:bit LED matrix, and controls the servo motor to open or close the bin based on the distance.
   
   Conditional Statements: There are if statements checking the value of distance. If the distance is less than or equal to 30 centimeters, it opens the bin, waits for 5 seconds, and then closes it. If the distance is zero, it closes the bin.
   
   Global Variables: The global keyword is used to declare that the distance variable is a global variable, allowing it to be accessed and modified within different parts of the code.

## Coding environment / text editor
   Microsoft Makecode (https://makecode.microbit.org/#editor)

## Feel free to comment or contribute

"""

## Project code / program

distance = 0 # variable to store the distance calculated by the ultrasonic sensor.
# The emoji on line 3 will show up when the miro:bit switches on
basic.show_leds("""
    . . # . .
    . # . # .
    # . . . #
    . # . # .
    . . # . .
    """)
def on_forever():
    global distance
    distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    basic.show_number(distance)
    if distance <= 30:     
        servos.P2.set_angle(180) #Open bin
        basic.pause(5000) 
        servos.P2.set_angle(0) # Close bin
    else :
        servos.P2.set_angle(0) #close bin
    if distance == 0:
        servos.P2.set_angle(0) #Close bin
        basic.pause(1000)
basic.forever(on_forever)













