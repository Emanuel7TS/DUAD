
from unittest.mock import mock_open, patch
from test_funcs import read_lines
import pytest

from unittest.mock import mock_open, patch
from test_funcs import read_lines


def test_read_lines_returns_expected_lines():
    # Arrange
    fake_content = "line 1\nline 2\nline 3\n"
    mocked_open = mock_open(read_data=fake_content)

    # Act
    with patch("builtins.open", mocked_open):
        result = read_lines("fake/path/file.txt")

    # Assert
    assert result == ["line 1\n", "line 2\n", "line 3\n"]



def test_read_lines_raises_file_not_found_error():
    # Arrange
    with patch("builtins.open", side_effect=FileNotFoundError):

        # Act & Assert
        with pytest.raises(FileNotFoundError):
            read_lines("not/existing/file.txt")