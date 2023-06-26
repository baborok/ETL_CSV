import psycopg2
import pandas as pd

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="loh123"
)

# Создание курсора для выполнения SQL-запросов
cur = conn.cursor()

# Импорт данных из Excel файла
excel_file = r"C:\Users\petuu\Desktop\DGA dataset\UK\Lewis et al 2022 DGA data\output.xlsx"  # Укажите путь к вашему Excel файлу
sheet_name = "Sheet"  # Укажите имя листа в Excel файле
excel_data = pd.read_excel(excel_file, sheet_name=sheet_name)

# Замена названий столбцов
column_names = excel_data.columns
new_column_names = [f"Газ{i}" for i in range(1, len(column_names) + 1)]
excel_data.columns = new_column_names

# Создание таблицы в базе данных
table_name = "your_table_name"

# Создание SQL-запроса для создания таблицы
columns_str = ', '.join([f'"{col}" TEXT' for col in new_column_names])
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str});"

# Выполнение SQL-запроса для создания таблицы
cur.execute(create_table_query)

# Вставка данных в таблицу
for row in excel_data.itertuples(index=False):
    placeholders = ', '.join(['%s' for _ in new_column_names])
    insert_query = f"INSERT INTO {table_name} VALUES ({placeholders});"
    cur.execute(insert_query, row)

# Закрытие курсора и сохранение изменений в базе данных
cur.close()
conn.commit()

# Закрытие соединения с базой данных PostgreSQL
conn.close()
