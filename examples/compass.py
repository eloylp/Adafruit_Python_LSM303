
import time
import sys

import Adafruit_LSM303
from Adafruit_LSM303.helper import Compass

lsm303 = Adafruit_LSM303.LSM303()

# Setting magnetic gain. you can check it at http://www.magnetic-declination.com/
#lsm303.set_mag_gain(Adafruit_LSM303.LSM303_MAGGAIN_4_7)

compass = Compass(lsm303)

print('Printing heading ..')

while True:

    heading = compass.get_heading()
    data = '\rHeading (Degrees): {0} '.format(heading)
    sys.stdout.write(data)
    sys.stdout.flush()
    time.sleep(0.1)
