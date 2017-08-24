from unittest import TestCase

from ddt import ddt, data, unpack
from mock import MagicMock

from Adafruit_LSM303.instruments import Compass, Instrument


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
