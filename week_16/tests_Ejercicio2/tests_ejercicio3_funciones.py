from test_funcs import sum_number_list
import random
import pytest

def test_sum_number_list_small_list_return_total():
    # Arrange
    original_data = [4, 8, 15, 16, 23, 42, 7, 13, 29, 31]
    data = original_data.copy()                 

    # Act
    result = sum_number_list(data)

    # Assert
    assert result == 188



def test_sum_number_list_big_list_return_total():
    # Arrange
    original_list = []
    for i in range(1000):
        original_list.append(random.randint(1, 1000)) 

    # Act
    result = sum_number_list(original_list)
    check = sum(original_list)

    # Assert
    assert result == check  



def test_sum_number_list_raises_type_error_when_input_is_not_sumable():
    # Arrange
    data = "Hola mundo"                     # hola mundo pasa el ciclo pero no la suma 

    # Act & Assert
    with pytest.raises(TypeError):
        sum_number_list(data)