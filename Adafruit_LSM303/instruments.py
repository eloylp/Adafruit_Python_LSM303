from math import atan2, degrees


class Instrument:
    def __init__(self, lsm303_sensor):
        """
        :type lsm303_sensor : Adafruit_LSM303.LSM303.LSM303
        """
        self.lsm303_sensor = lsm303_sensor

    def vector_2_degrees(self, x, y):
        radians = atan2(y, x)
        degrees_calc = degrees(radians)
        if degrees_calc < 0:
            degrees_calc = 360 + degrees_calc
        return degrees_calc


class Compass(Instrument):
    def get_heading(self):
        magnet_axis_data = self.lsm303_sensor.read_magnetometer()
        return self.vector_2_degrees(magnet_axis_data[0], magnet_axis_data[2])


class Inclinometer(Instrument):

    def get_inclination(self):
        return self.get_inclination_respect_x(), self.get_inclination_respect_y()

    def get_inclination_respect_x(self):
        accel_axis_data = self.get_data()
        return self.vector_2_degrees(accel_axis_data[0], accel_axis_data[2])

    def get_inclination_respect_y(self):
        accel_axis_data = self.get_data()
        return self.vector_2_degrees(accel_axis_data[1], accel_axis_data[2])

    def get_data(self):
        return self.lsm303_sensor.read_accelerometer()
