import csv
import pandas as pd
from openpyxl import Workbook

def clean_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    cleaned_data = []
    for row in data:
        cleaned_row = []
        for item in row:
            cleaned_item = item.replace(',', '')
            cleaned_row.append(cleaned_item)
        cleaned_data.append(cleaned_row)

    # Создаем DataFrame с очищенными данными
    df = pd.DataFrame(cleaned_data)

    # Создаем новый Excel файл
    workbook = Workbook()
    sheet = workbook.active

    # Записываем значения в отдельные ячейки
    for index, row in df.iterrows():
        for col_num, value in enumerate(row):
            values = value.split(',')
            for i, val in enumerate(values):
                sheet.cell(row=index+1, column=col_num+1+i, value=val.strip())

    # Сохраняем Excel файл
    workbook.save(output_file)
    print("CSV файл успешно очищен и обработан. Результат сохранен в Excel.")

# Пример использования
input_file = r'C:\Users\shami\Desktop\dlya galieva\dga\Lewis et al 2022 DGA data\Lewis_et_al_2022_Transformer_A.csv'   # Путь к исходному файлу CSV
output_file = 'output.xlsx' # Путь к выходному файлу Excel

clean_csv(input_file, output_file)