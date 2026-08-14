from models import FinanceManager, Category
import pytest


def test_create_correct_category():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()

# Act
    fm_test.add_category("FooD")

# Assert
    assert "food" in fm_test.categories





def test_check_repeat_category():                       # pytest Week_17/test_logic.py

    # Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")

    # Act & Assert
    with pytest.raises(ValueError):
        fm_test.add_category("FOOD")





def test_create_correct_movement():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")
# Act
    movement_test = fm_test.add_movement("pizza", 1200, "expense",fm_test.categories["food"])

# Assert
    assert movement_test in fm_test.movements





def test_incorrect_movement_negative_value():  # ACA ME DI CUENTA QUE LA CLASS DE MOVEMENT TENIA UN ERROR ✅
# Arrange                                                           # pytest Week_17/test_logic.py
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    
    # Act & Assert
    with pytest.raises(ValueError):
        fm_test.add_movement("pizza", -1200, "expense", fm_test.categories["food"])





def test_incorrect_movement_wrong_value():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    
    # Act & Assert
    with pytest.raises(ValueError):
        fm_test.add_movement("pizza", "Hola", "expense", fm_test.categories["food"])





def test_incorrect_movement_invalid_type():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()
    fm_test.add_category("savings")
    
    # Act & Assert
    with pytest.raises(ValueError):
        fm_test.add_movement("rest of money", 1000, "savings", fm_test.categories["savings"])





def test_nonexistent_category():                       # pytest Week_17/test_logic.py
# Arrange
    gas = Category("gas")
    fm_test = FinanceManager()

    # Act & Assert
    with pytest.raises(ValueError):
        fm_test.add_movement("gas", 1000, "expense", gas)





def test_get_correct_total():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    fm_test.add_category("salary")

# Act
    fm_test.add_movement("pizza", 1200, "expense",fm_test.categories["food"])
    fm_test.add_movement("pizza", 1600, "expense",fm_test.categories["food"])
    fm_test.add_movement("salary", 5000, "income",fm_test.categories["salary"])

# Assert
    assert fm_test.get_total_by_type("expense") == 2800





def test_raise_invalid_type_error():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    fm_test.add_category("salary")

# Act
    fm_test.add_movement("pizza", 1400, "expense",fm_test.categories["food"])
    fm_test.add_movement("pizza", 1600, "expense",fm_test.categories["food"])

# Assert
    with pytest.raises(ValueError):
        fm_test.get_total_by_type("expence") == 3000





def test_get_correct_balance():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    fm_test.add_category("salary")

# Act
    fm_test.add_movement("pizza", 1200, "expense",fm_test.categories["food"])
    fm_test.add_movement("pizza", 1600, "expense",fm_test.categories["food"])
    fm_test.add_movement("salary", 5000, "income",fm_test.categories["salary"])

# Assert
    assert fm_test.get_balance() == 2200
