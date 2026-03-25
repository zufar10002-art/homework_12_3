\# Домашнее задание 12.3: Работа с CSV и Excel файлами



\## Описание

Проект для чтения финансовых транзакций из CSV и Excel файлов с использованием библиотеки pandas.



\## Функциональность

\- `read\_csv\_transactions(file\_path)` — чтение CSV файла, возвращает список словарей

\- `read\_excel\_transactions(file\_path)` — чтение Excel файла, возвращает список словарей



\## Установка

1\. Создать виртуальное окружение: `python -m venv venv`

2\. Активировать: `venv\\Scripts\\activate` (Windows)

3\. Установить зависимости: `pip install -r requirements.txt`



\## Использование

```python

from src.file\_processing import read\_csv\_transactions, read\_excel\_transactions



\# Чтение CSV

transactions\_csv = read\_csv\_transactions("data/transactions.csv")



\# Чтение Excel

transactions\_excel = read\_excel\_transactions("data/transactions\_excel.xlsx")



