from test_funcs import sort_string
import pytest


def test_sort_string_correct_input_returns_sort_string():
    # Arrange
    data = "d-e-v-e-l-o-p-e-r"

    # Act
    result = sort_string(data)

    # Assert
    assert result == "d-e-e-e-l-r-o-p-v"



def test_sort_string_order_input_returns_sort_string():
    # Arrange
    data = "a-l-m-o-s-t"

    # Act
    result = sort_string(data)

    # Assert
    assert result == "a-l-m-o-s-t"



def test_sort_string_when_input_is_not_string_raises_error():
    # Arrange
    data = 5                 

    # Act & Assert
    with pytest.raises(TypeError):
        sort_string(data)