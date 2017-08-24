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
        return self.vector_2_degrees(magnet_axis_data[0], magnet_axis_data[2])


class Inclinometer(Instrument):
    REFERENCE_POINT_DEGREES = 90

    def get_inclination(self):
        return self.get_inclination_respect_x(), self.get_inclination_respect_y()

    def get_inclination_respect_x(self):
        accel_axis_data = self.get_data()

        return self.adapt_measure(
            self.vector_2_degrees(accel_axis_data[0], accel_axis_data[2])
        )

    def get_inclination_respect_y(self):
        accel_axis_data = self.get_data()
        return self.adapt_measure(
            self.vector_2_degrees(accel_axis_data[1], accel_axis_data[2])
        )

    def adapt_measure(self, degrees):
        if degrees < self.REFERENCE_POINT_DEGREES:
            return self.REFERENCE_POINT_DEGREES + degrees
        elif self.REFERENCE_POINT_DEGREES <= degrees < 270:
            return (degrees - self.REFERENCE_POINT_DEGREES) * -1
        elif degrees >= 270:
            return degrees - (self.REFERENCE_POINT_DEGREES * 3)

    def get_data(self):
        return self.lsm303_sensor.read_accelerometer()
