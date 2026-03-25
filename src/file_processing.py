"""
Модуль для чтения финансовых транзакций из CSV и Excel файлов.
"""

from typing import Any, Dict, List

import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        List[Dict[str, Any]]: Список словарей с данными о транзакциях.
                               Возвращает пустой список при ошибке.
    """
    try:
        df = pd.read_csv(file_path, sep=';', encoding='utf-8')
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        List[Dict[str, Any]]: Список словарей с данными о транзакциях.
                               Возвращает пустой список при ошибке.
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")
        return []
