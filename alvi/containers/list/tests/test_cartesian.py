from alvi.containers.list import cartesian
from alvi.containers.tests import TestContainer


class TestCartesian(TestContainer):
    def test_create_head(self):
        list = cartesian.Cartesian(self.pipe)
        head = list.create_head(10)
        assert head == list.head
        assert head.value == 10
        self.assertRaises(RuntimeError, list.create_head, 10)
        child = head.create_child(11)
        assert child.value == 11
        assert head.next == child
        assert child.next is None