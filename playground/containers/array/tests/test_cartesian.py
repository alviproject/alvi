from playground.containers.array import cartesian
from playground.containers.tests import TestContainer
import unittest


class TestCartesian(TestContainer):
    def test_init(self):
        array = cartesian.Cartesian(self.pipe)
        array.init(10)
        assert array.size() == 10
        self.assertRaises(RuntimeError, array.init, 10)

    def test_assign_value(self):
        array = cartesian.Cartesian(self.pipe)
        array.init(10)
        array[1] = 3
        assert array[1] == 3
        array[1] = 2
        assert array[1] == 2