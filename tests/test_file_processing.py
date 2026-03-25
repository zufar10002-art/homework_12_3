"""
Тесты для модуля file_processing.
"""

from unittest.mock import MagicMock, patch

from src.file_processing import read_csv_transactions, read_excel_transactions


@patch('src.file_processing.pd.read_csv')
def test_read_csv_success(mock_read_csv):
    """Тест успешного чтения CSV файла."""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]
    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("fake_path.csv")

    assert len(result) == 2
    assert result[0]["id"] == 1
    mock_read_csv.assert_called_once()


@patch('src.file_processing.pd.read_csv')
def test_read_csv_error(mock_read_csv):
    """Тест ошибки при чтении CSV файла."""
    mock_read_csv.side_effect = Exception("File not found")

    result = read_csv_transactions("fake_path.csv")

    assert result == []
    mock_read_csv.assert_called_once()


@patch('src.file_processing.pd.read_excel')
def test_read_excel_success(mock_read_excel):
    """Тест успешного чтения Excel файла."""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": 200}
    ]
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("fake_path.xlsx")

    assert len(result) == 2
    assert result[0]["id"] == 1
    mock_read_excel.assert_called_once()


@patch('src.file_processing.pd.read_excel')
def test_read_excel_error(mock_read_excel):
    """Тест ошибки при чтении Excel файла."""
    mock_read_excel.side_effect = Exception("File not found")

    result = read_excel_transactions("fake_path.xlsx")

    assert result == []
    mock_read_excel.assert_called_once()
