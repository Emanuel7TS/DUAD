from test_funcs import letter_case_counter
import pytest


def test_letter_case_counter_mix_input_return_counters():
    # Arrange
    data = "FuLlStAcK"

    # Act
    result = letter_case_counter(data)

    # Assert
    assert result == (5,4)



def test_letter_case_counter_input_with_spaces_correct_count():
    # Arrange
    data = "FuLl tAcK D E V"

    expected_upper = sum(1 for c in data if c.isupper())
    expected_lower = sum(1 for c in data if c.islower())

    # Act
    result = letter_case_counter(data)

    # Assert
    assert result == (expected_upper, expected_lower)



def test_letter_case_counter_raise_error_when_input_is_not_iterable():
    # Arrange
    data = True            

    # Act & Assert
    with pytest.raises(TypeError):
        letter_case_counter(data)