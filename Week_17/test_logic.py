from models import FinanceManager                   # pytest test_logic.py
import pytest


def test_create_correct_category():
# Arrange
    fm_test = FinanceManager()

# Act
    fm_test.add_category("FooD")

# Assert
    assert "food" in fm_test.categories

def test_check_repeat_category():

    # Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")

    # Act & Assert
    with pytest.raises(ValueError):
        fm_test.add_category("FOOD")