# put Raspberry next way:
# usb should be closer than CPU
# GPIO ports should be on the right side
# (check usb one more time, it should be closer to you)
# then look setmode:
#  1	2      - not useful
#  3	4      - use 4th port to apply 5v to servo
#  5	6      - use 6th port to connect ground to servo
#  7	8      - not useful
#  9	10     - bot useful
#  11	12     - use 11th port to setup logic


#  3   4------------------------------------5v (red)
#  5   6------------------------------------ground(black)
#  11  12
#  ^------------------------------------------logic (orange)


import RPi.GPIO as GPIO
import time

degrees = 0

def rotate(degrees):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    servo = GPIO.PWM(11, 50)
    servo.start(0)

    duty = degrees / 180 * 10.5 + 2
    servo.ChangeDutyCycle(duty)
    time.sleep(.5)
    servo.stop()
    GPIO.cleanup()

    return "Rotation sucessfull"


if __name__ == "__main__":
    while degrees != 500:
        degrees = float(input("Type degrees: "))
        if degrees != 500:
            print(rotate(degrees))

