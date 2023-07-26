import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text

# Параметры подключения к PostgreSQL
db_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'loh123'
}

# Путь к файлу Excel
excel_file_path = '12.xlsx'

# Имя таблицы PostgreSQL, в которую будем импортировать данные
table_name = 'PRICE'

# Данные для создания таблицы (указать соответствующие столбцы и их типы)
table_columns = {
    'primary_key': 'character varying(50)',
    'unit': 'character varying(50)',
    'price': 'character varying(50)',
    'description': 'character varying(50)',
    # добавьте другие столбцы и их типы
}

# Создаем подключение к базе данных PostgreSQL
conn_str = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
engine = create_engine(conn_str)

# Создаем таблицу в базе данных
def create_table():
    column_definitions = ', '.join([f"{col} {data_type}" for col, data_type in table_columns.items()])
    create_table_query = f"CREATE TABLE {table_name} ({column_definitions})"
    with engine.connect() as connection:
        connection.execute(text(create_table_query))

# Импортируем данные из Excel файла в таблицу PostgreSQL
def import_data():
    df = pd.read_excel(excel_file_path)
    try:
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print("Данные успешно импортированы в PostgreSQL.")
    except Exception as e:
        print(f"Ошибка при импорте данных в PostgreSQL: {str(e)}")

if __name__ == "__main__":
    create_table()
    import_data()
