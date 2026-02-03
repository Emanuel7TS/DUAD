from test_funcs import divide
import pytest

def test_divide_correct_input_return_correct_result():
    # Arrange
    a, b = 10, 2

    # Act
    result = divide(a, b)

    # Assert
    assert result == 5.0



def test_divide_when_input_is_zero_raises_error():
    # Arrange
    a, b = 10, 0

    # Act & Assert
    with pytest.raises(ValueError):
        divide(a,b)



def test_divide_when_input_is_string_raises_error():
    # Arrange
    a, b = 10, "0"

    # Act & Assert
    with pytest.raises(TypeError):
        divide(a,b)