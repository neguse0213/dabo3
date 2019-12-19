import unittest
import hello

from unittest.mock import patch


class TestWellnessModoki(unittest.TestCase):

    def setUp(self):
        pass

    @patch('hello.WellnessModoki')
    def test_showWeight(self, mock_wel):
        mock_wel.show_weight.return_value = 'fuga'
        mo = hello.WellnessModoki
        no = mo.show_weight

        self.assertEqual(no, 'test')


if __name__ == "__main__":
    unittest.main()
