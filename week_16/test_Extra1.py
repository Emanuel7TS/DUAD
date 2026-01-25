# 1. Cree una clase de pruebas que contenga al menos `3` funciones que operen con números (como suma, promedio, conversión, etc.) y escriba:
# - Un caso con números positivos
# - Un caso con números negativos
# - Un caso con ceros

from test_funcs import sum_numbers, calculate_average, convert_to_list


class TestNumberOperations:

    # -------- SUM --------

    def test_sum_with_positive_numbers(self):
        assert sum_numbers(5, 3) == 8

    def test_sum_with_negative_numbers(self):
        assert sum_numbers(-5, -3) == -8

    def test_sum_with_zeros(self):
        assert sum_numbers(0, 0) == 0


    # -------- AVERAGE --------

    def test_average_with_positive_numbers(self):
        assert calculate_average(10, 20) == 15

    def test_average_with_negative_numbers(self):
        assert calculate_average(-10, -20) == -15

    def test_average_with_zeros(self):
        assert calculate_average(0, 0) == 0


    # -------- CONVERSION --------

    def test_convert_to_list_with_positive_numbers(self):
        assert convert_to_list(1, 2) == [1, 2]

    def test_convert_to_list_with_negative_numbers(self):
        assert convert_to_list(-1, -2) == [-1, -2]

    def test_convert_to_list_with_zeros(self):
        assert convert_to_list(0, 0) == [0, 0]