from test_funcs import is_prime, filter_primes
import pytest


def test_filter_primes_small_list_returns_primes():
    # Arrange
    data = [2,13,500]

    # Act
    result = filter_primes(data)

    # Assert
    assert result == [13]



def test_filter_primes_big_list_returns_primes():
    # Arrange
    data = [
    3, 17, 25, 8, 42, 19, 6, 31, 14, 27,
    9, 50, 21, 4, 36, 11, 29, 7, 45, 16,
    2, 34, 18, 23, 10, 41, 5, 28, 33, 12,
    26, 1, 39, 20, 15, 47, 24, 30, 13, 40,
    22, 48, 35, 46, 32, 44, 37, 38, 49, 43
]

    # Act
    result = filter_primes(data)

    # Assert
    assert result == [
    3, 17, 19, 31, 29, 7, 2, 23, 41, 5,
    11, 13, 47
]



def test_filter_primes_fails_when_list_contains_non_number_raise_error():
    # Arrange
    data = [2,13,500,"hola"]

    # Act & Assert
    with pytest.raises(TypeError):
        filter_primes(data)