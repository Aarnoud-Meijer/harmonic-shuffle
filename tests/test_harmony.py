import unittest

from harmonic_shuffle.harmony import Harmony


class TestMinorDbm(unittest.TestCase):
    def setUp(self):
        self.root_key = 'Dbm'
        self.harm = Harmony(self.root_key)

    def test_Dbm_up_shift(self):
        self.assertEqual(self.harm.up_shift(), ['G#m'])

    def test_Dbm_down_shift(self):
        self.assertEqual(self.harm.down_shift(), ['Gbm', 'F#m'])

    def test_Dbm_major_shift(self):
        self.assertEqual(self.harm.minor(), ['E'])

    def test_Dbm_all_harmonies(self):
        self.assertEqual(self.harm.harmonies, ['C#m', 'Dbm', 'Gbm', 'F#m', 'G#m', 'E'])

class TestMajorE(unittest.TestCase):
    def setUp(self):
        self.root_key = 'E'
        self.harm = Harmony(self.root_key)

    def test_E_up_shift(self):
        self.assertEqual(self.harm.up_shift(), ['B'])

    def test_E_down_shift(self):
        self.assertEqual(self.harm.down_shift(), ['A'])

    def test_E_minor_shift(self):
        self.assertEqual(self.harm.minor(), ['C#m', 'Dbm'])

    def test_E_all_harmonies(self):
        self.assertEqual(self.harm.harmonies, ['E', 'A', 'B', 'C#m', 'Dbm'])


if __name__ == '__main__':
    unittest.main()
