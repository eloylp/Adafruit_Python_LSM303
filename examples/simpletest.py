# Simple demo of of the LSM303 accelerometer & magnetometer library.
# Will print the accelerometer & magnetometer X, Y, Z axis values every half
# second.
# Author: Tony DiCola
# License: Public Domain

import time
import sys

import Adafruit_LSM303

lsm303 = Adafruit_LSM303.LSM303()

# Setting magnetic gain. you can check it at http://www.magnetic-declination.com/
# lsm303.set_mag_gain(Adafruit_LSM303.LSM303_MAGGAIN_4_7)

# Alternatively you can specify the I2C bus with a bus parameter:
# lsm303 = Adafruit_LSM303.LSM303(busum=2)

print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    accel = lsm303.read_accelerometer()
    mag = lsm303.read_magnetometer()

    # You also can get a accel + mag tuple with this function
    # total_data = lsm303.read()

    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag

    data = 'Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(accel_x, accel_y, accel_z,
                                                                                           mag_x, mag_y, mag_z)
    sys.stdout.write(data)
    sys.stdout.flush()

    time.sleep(0.1)
