from math import atan2, pi


class Instrument:
    def __init__(self, lsm303_sensor):
        """
        :type lsm303_sensor : Adafruit_LSM303.LSM303.LSM303
        """
        self.lsm303_sensor = lsm303_sensor

    def vector_2_degrees(self, x, y):
        radians = atan2(y, x)
        degrees = radians * 180 / pi
        if degrees < 0:
            degrees = 360 + degrees
        return degrees


class Compass(Instrument):
    def get_heading(self):
        magnet_axis_data = self.lsm303_sensor.read_magnetometer()
        heading_radians = atan2(magnet_axis_data[2], magnet_axis_data[0])
        heading_degrees = heading_radians * 180 / pi
        if heading_degrees < 0:
            heading_degrees = 360 + heading_degrees
        return heading_degrees
