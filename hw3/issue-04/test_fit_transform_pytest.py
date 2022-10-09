import pytest
from one_hot_encoder import fit_transform


def test_basic_fit_transform():
    words = ['Hello', 'world']

    exp_transformed_words = [
        ('Hello', [0, 1]),
        ('world', [1, 0]),
    ]

    assert fit_transform(words) == exp_transformed_words


def test_repeated_fit_transform():
    words = ['Hello', 'Hello']

    exp_transformed_words = [
        ('Hello', [1]),
        ('Hello', [1]),
    ]

    assert fit_transform(words) == exp_transformed_words


def test_passing_arguments():
    assert ('new', [0, 1, 0]) in fit_transform('Hello', 'new', 'world')


def test_argument_length():
    with pytest.raises(TypeError):
        fit_transform()
