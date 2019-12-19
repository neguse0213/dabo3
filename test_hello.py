import unittest
import hello


class TestWellnessModoki(unittest.TestCase):

    def setUp(self):
        pass

    # WIP
    def test_showWeight(self):
        hello.WellnessModoki().show_weight().retur_value = "hoge"
        actual = hello.WellnessModoki()
        self.assertEqual("a", "a")


if __name__ == "__main__":
    unittest.main()