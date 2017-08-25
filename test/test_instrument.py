from unittest import TestCase

from ddt import ddt, data, unpack
from mock import MagicMock

from Adafruit_LSM303.instruments import Instrument, Inclinometer


@ddt
class TestInstrument(TestCase):
    def setUp(self):
        lsm303 = MagicMock()
        self.instrument = Instrument(lsm303)

    @data(
        (0, 0, 0),
        (1, 0, 0),
        (1, 1, 45),
        (0, 1, 90),
        (-1, 0, 180),
        (-1, -1, 225),
        (0, -1, 270),
        (1, -0.0000000000000001, 360),
    )
    @unpack
    def test_vector_2_degrees(self, x, y, expected_degrees):
        degrees = self.instrument.vector_2_degrees(x, y)
        self.assertEqual(expected_degrees, degrees)


@ddt
class TestInclinometer(TestCase):
    @data(
        (10, 100),
        (89, 179),
        (90, 0),
        (180, -90),
        (269, -179),
        (270, 0),
        (271, 1),
        (360, 90),
    )
    @unpack
    def test_measure_is_adapted(self, degrees, expected_degrees):
        lsm303 = MagicMock()
        inclinometer = Inclinometer(lsm303)
        inclinometer.vector_2_degrees = MagicMock(return_value=(degrees))

        inclination_degrees_per_axis = inclinometer.get_inclination()
        self.assertEqual(expected_degrees, inclination_degrees_per_axis[0])
        self.assertEqual(expected_degrees, inclination_degrees_per_axis[1])
