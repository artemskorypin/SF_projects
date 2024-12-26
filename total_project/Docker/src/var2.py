import pandas as pd

# 1. Читаем test.csv, выбирая только определенные столбцы, и устанавливаем индексы
pd.read_csv("data/test.zip", usecols=[0, 2, 3])\
.set_index(['item_nbr', 'store_nbr'])\
.join(
    # 2. Читаем train.csv, выбирая определенные столбцы, преобразуя 'unit_sales' 
    #    (отрицательные или нулевые значения заменяются на 0).
    pd.read_csv(
        'data/train.zip',
        usecols=[0, 2, 3, 4],
        converters={'unit_sales': lambda u: float(u) if float(u) > 0 else 0},
        skiprows=range(1, 86672217)  # Пропускаем первые 86672217 строк
    )
    # 3. Группируем данные из train.csv по 'item_nbr' и 'store_nbr' 
    #    и считаем медиану для 'unit_sales'
    .groupby(['item_nbr', 'store_nbr'])['unit_sales'].median()
    .to_frame('unit_sales'),  # Преобразуем в DataFrame с именем столбца 'unit_sales'
    
    how='left'  # Джойним test.csv с train.csv по 'item_nbr' и 'store_nbr'
    # 4. Заполняем пропущенные значения в 'unit_sales' нулями
    # 5. Сохраняем результат в файл median.csv с двумя знаками после запятой

).fillna(0).to_csv('median.csv', float_format='%.2f', index=None)
