from utility.servo import Servo

servo1 = Servo(17)
servo2 = Servo(27)
top_servo = Servo(22)

servo1.middle()
servo2.middle()
top_servo.open()
top_servo.close()