import unittest
from CountVectorizer import CountVectorizer


class TestCountVectorizer(unittest.TestCase):
    def test_fit_transform(self):
        test_cases = [
            {
                'corpus': [
                    'Crock Pot Pasta Never boil pasta again',
                    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
                ],
                'feature_names': ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
                                    'fresh', 'ingredients', 'parmesan', 'to', 'taste'],
                'count_matrix': [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                    [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]],
            },
            {
                'corpus': ['one Two Three four Five'],
                'feature_names': ['one', 'two', 'three', 'four', 'five'],
                'count_matrix': [[1, 1, 1, 1, 1]],
            },
        ]

        for t in test_cases:
            vectorizer = CountVectorizer()
            count_matrix = vectorizer.fit_transform(t['corpus'])

            self.assertEqual(vectorizer.get_feature_names(), t['feature_names'])
            self.assertEqual(count_matrix, t['count_matrix'])


if __name__ == '__main__':
    unittest.main()