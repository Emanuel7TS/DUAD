from models import FinanceManager, Category
from datetime import date
import persistence
import pytest

#                                                          Models            

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
    movement_test = fm_test.add_movement("pizza", 1200, "expense",fm_test.categories["food"],"20/08/2026")

# Assert
    assert movement_test in fm_test.movements
    assert movement_test.date == date(2026, 8, 20)





def test_incorrect_movement_negative_value():  # ACA ME DI CUENTA QUE LA CLASS DE MOVEMENT TENIA UN ERROR ✅
# Arrange                                                           # pytest Week_17/test_logic.py
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    
    # Act & Assert
    with pytest.raises(ValueError):
        fm_test.add_movement("pizza", -1200, "expense", fm_test.categories["food"],"20/08/2026")





def test_incorrect_movement_wrong_value():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    
    # Act & Assert
    with pytest.raises(ValueError):
        fm_test.add_movement("pizza", "Hola", "expense", fm_test.categories["food"],"20/08/2026")





def test_incorrect_movement_invalid_type():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()
    fm_test.add_category("savings")
    
    # Act & Assert
    with pytest.raises(ValueError):
        fm_test.add_movement("rest of money", 1000, "savings", fm_test.categories["savings"],"20/08/2026")





def test_nonexistent_category():                       # pytest Week_17/test_logic.py
# Arrange
    gas = Category("gas")
    fm_test = FinanceManager()

    # Act & Assert
    with pytest.raises(ValueError):
        fm_test.add_movement("gas", 1000, "expense", gas,"20/08/2026")





def test_get_correct_total():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    fm_test.add_category("salary")

# Act
    fm_test.add_movement("pizza", 1200, "expense",fm_test.categories["food"],"20/08/2026")
    fm_test.add_movement("pizza", 1600, "expense",fm_test.categories["food"],"20/08/2026")
    fm_test.add_movement("salary", 5000, "income",fm_test.categories["salary"],"20/08/2026")

# Assert
    assert fm_test.get_total_by_type("expense") == 2800





def test_raise_invalid_type_error():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    fm_test.add_category("salary")

# Act
    fm_test.add_movement("pizza", 1400, "expense",fm_test.categories["food"],"20/08/2026")
    fm_test.add_movement("pizza", 1600, "expense",fm_test.categories["food"],"20/08/2026")

# Assert
    with pytest.raises(ValueError):
        fm_test.get_total_by_type("expence")





def test_get_correct_balance():                       # pytest Week_17/test_logic.py
# Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    fm_test.add_category("salary")

# Act
    fm_test.add_movement("pizza", 1200, "expense",fm_test.categories["food"],"20/08/2026")
    fm_test.add_movement("pizza", 1600, "expense",fm_test.categories["food"],"20/08/2026")
    fm_test.add_movement("salary", 5000, "income",fm_test.categories["salary"],"20/08/2026")

# Assert
    assert fm_test.get_balance() == 2200

#                                                   Persintence





def test_store_categories(tmp_path, monkeypatch):     # pytest Week_17/test_logic.py

    # Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    fm_test.add_category("Salary")

    monkeypatch.chdir(tmp_path)

    # Act
    persistence.store_categories(fm_test.categories)

    # Assert
    file_path = tmp_path / "categories.csv"

    assert file_path.exists()

    with open(file_path, "r") as csv_file:
        content = csv_file.read()

    assert "food" in content
    assert "salary" in content





def test_load_categories(tmp_path, monkeypatch):        # pytest Week_17/test_logic.py

    # Arrange
    fm_test = FinanceManager()

    monkeypatch.chdir(tmp_path)

    categories = ["salary", "food"]

    with open("categories.csv", "w", newline="", encoding="utf-8") as new_file:
        for category_name in categories:
            new_file.write(f"{category_name}\n")

    # Act
    persistence.load_categories(fm_test)

    # Assert

    assert "salary" in fm_test.categories
    assert "food" in fm_test.categories





def test_store_movements(tmp_path, monkeypatch):        # pytest Week_17/test_logic.py

    # Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")
    fm_test.add_movement("pizza", 1200, "expense",fm_test.categories["food"],"20/08/2026")

    monkeypatch.chdir(tmp_path)

    # Act
    persistence.store_movements(fm_test.movements)

    # Assert
    file_path = tmp_path / "movements.csv"

    assert file_path.exists()

    with open(file_path, "r") as csv_file:
        content = csv_file.read()

    assert "pizza,1200.0,expense,food" in content






def test_load_movements(tmp_path, monkeypatch):         # pytest Week_17/test_logic.py

    # Arrange
    fm_test = FinanceManager()
    fm_test.add_category("Food")

    monkeypatch.chdir(tmp_path)

    with open("movements.csv", "w", newline="", encoding="utf-8") as new_file:
        new_file.write("pizza,1200,expense,food,20/08/2026\n")

    # Act
    persistence.load_movements(fm_test)

    # Assert
    movement = fm_test.movements[0]
    assert movement.name == "pizza"
    assert movement.value == 1200
    assert movement.type == "expense"
    assert movement.category.name == "food"
    assert movement.date == date(2026, 8, 20)