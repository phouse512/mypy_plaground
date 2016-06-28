import unittest


class TestFuncEquality(unittest.TestCase):

    def test_all(self) -> None:
        self.assertDictEqual({}, {})
        self.assertMultiLineEqual("", "")
        self.assertTupleEqual((2, 2), (2, 2))
        self.assertSetEqual(set([3]), set([3]))

    def test_all_w_msg(self) -> None:
        self.assertDictEqual({}, {}, msg="hi!")
        self.assertMultiLineEqual("", "", msg="yoza")
        self.assertTupleEqual((2, 2), (2, 2), msg=12)
        self.assertSetEqual(set([3]), set([3]), msg="dude")

if __name__ == "__main__":
    unittest.main()
