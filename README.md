# Домашнее задание 12.3: Работа с CSV и Excel файлами

## Описание
Проект для чтения финансовых транзакций из CSV и Excel файлов с использованием библиотеки pandas.

## Функциональность
- `read_csv_transactions(file_path)` — чтение CSV файла, принимает путь к файлу, возвращает список словарей
- `read_excel_transactions(file_path)` — чтение Excel файла, принимает путь к файлу, возвращает список словарей

## Установка
1. Создать виртуальное окружение: `python -m venv venv`
2. Активировать: `venv\Scripts\activate` (Windows)
3. Установить зависимости: `pip install -r requirements.txt`

## Использование
```python
from src.file_processing import read_csv_transactions, read_excel_transactions

# Чтение CSV
transactions_csv = read_csv_transactions("data/transactions.csv")

# Чтение Excel
transactions_excel = read_excel_transactions("data/transactions_excel.xlsx")
