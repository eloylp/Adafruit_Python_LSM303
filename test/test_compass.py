from unittest import TestCase

from ddt import ddt, data, unpack
from mock import MagicMock

from Adafruit_LSM303.instruments import Compass


@ddt
class TestCompass(TestCase):
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
    def test_get_heading(self, x, y, expected_degrees):

        lsm303 = MagicMock()
        lsm303.read_magnetometer = MagicMock(return_value=(x, 666, y))
        compass = Compass(lsm303)
        heading = compass.get_heading()
        self.assertEqual(expected_degrees, heading)
