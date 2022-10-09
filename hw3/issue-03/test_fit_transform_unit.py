import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_basic_fit_transform(self):
        seq = ['red', 'green', 'blue']

        exp_transformed_seq = [
            ('red', [0, 0, 1]),
            ('green', [0, 1, 0]),
            ('blue', [1, 0, 0]),
        ]

        self.assertEqual(fit_transform(seq), exp_transformed_seq)

    def test_repeated_fit_transform(self):
        seq = ['red', 'red', 'green']

        exp_transformed_seq = [
            ('red', [0, 1]),
            ('red', [0, 1]),
            ('green', [1, 0]),
        ]

        self.assertEqual(fit_transform(seq), exp_transformed_seq)

    def test_passing_arguments(self):
        self.assertIn(
            ('blue', [1, 0, 0]),
            fit_transform('red', 'green', 'blue'),
        )

    def test_argument_length(self):
        self.assertRaises(TypeError, fit_transform)
