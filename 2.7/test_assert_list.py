from unittest import TestCase
from typing import List

class MyTest(TestCase):
    def test_assert_list(self):
        # type: () -> None
        list1 = list()  # type: List[None]
        list2 = list()  # type: List[None]
        self.assertListEqual(list1, list2)

