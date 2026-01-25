# A

from test_funcs import bubble_sort
import random
import pytest

def test_bubble_sort_small_list_return_correct_list():
    # Arrange
    original_data = [3000, 1000, 2000]
    data = original_data.copy()                 # se crea una copia para hacer los test con una copia y no afectar asserts futuros ✅

    # Act
    result = bubble_sort(data)

    # Assert
    assert result == [1000, 2000, 3000]

# B

def test_bubble_sort_large_list_return_correct_list():
    # Arrange
    original_list = []
    for i in range(150):
        original_list.append(random.randint(1, 150))

    expected_result = sorted(original_list)
    data = original_list.copy()

    # Act
    result = bubble_sort(data)

    # Assert
    assert result == expected_result

# C

def test_bubble_sort_list_works_empty():
    # Arrange
    number_list = []
    data = number_list.copy()

    # Act
    result = bubble_sort(data)

    # Assert
    assert result == number_list

# D

def test_bubble_sort_raises_type_error_when_input_is_not_list():
    # Arrange
    data = 5

    # Act & Assert
    with pytest.raises(TypeError):
        bubble_sort(data)


# def test_demo(): # para verificar como se ve el TypeError
#     bubble_sort(5)