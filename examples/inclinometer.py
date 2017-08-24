import time
import sys

import Adafruit_LSM303
from Adafruit_LSM303.instruments import Inclinometer

lsm303 = Adafruit_LSM303.LSM303()

# Setting magnetic gain. you can check it at http://www.magnetic-declination.com/
# lsm303.set_mag_gain(Adafruit_LSM303.LSM303_MAGGAIN_4_7)

inclinometer = Inclinometer(lsm303)

print('Printing Inclination (Degrees) based on x-y-z respective angle ...')

"""
 Information printed is adapted to positive and negative degrees per axis. From 0 to 179 and from 0 to -179
 This means that if you are on pitch down movement you will get a negative number until 
 you reach the noise of the sensor shooting again the sky.
"""
while True:
    inclination = inclinometer.get_inclination()
    data = '\rX : {0}   Y: {1}'.format(inclination[0], inclination[1])
    sys.stdout.write(data)
    sys.stdout.flush()
    time.sleep(0.1)
