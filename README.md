# Raspberry Pi Ultrasonic Sensor
Basic Raspberry Pi project with HC-SR 04 Ultrasonic sensor and Python3

# Equipment
- Elegoo HC-SR04 Ultrasonic Sensor
- Raspberry Pi 3 model B
- Standard LED (any color)
- 330 ohm resistor
- Vcc for sensor is 5V from RPi

# Code & Method Description
US sensor used in this project provides output (distance) in metres. This value is used in while True loop as argument in 'time.sleep()' function.
Simple logic behind that is, the shorter the distance, the faster the LED blinks.

Many other code variations may be implemented.

# Disclaimer
Although all precautions were taken to work safely, I do not accept any responsibility for damaged equipment, nor harm to people. Safety first, be safe ...
