from test_funcs import string_reverse
import pytest


def test_string_reverse_correct_input_returns_reversed_string():
    # Arrange
    data = "Developer"
    expected = data[::-1]

    # Act
    result = string_reverse(data)

    # Assert
    assert result == expected



def test_string_reverse_single_character_returns_reversed_string():
    # Arrange
    data = "a"

    # Act
    result = string_reverse(data)

    # Assert
    assert result == "a"



def test_string_reverse_when_input_is_not_string_raises_error():
    # Arrange
    data = 5                 

    # Act & Assert
    with pytest.raises(TypeError):
        string_reverse(data)