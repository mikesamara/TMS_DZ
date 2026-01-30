''' задача 4 анализ возраста

- Добавьте столбец с возрастом (случайные значения от 18 до 65).
- Разделите пользователей на возрастные группы: 18-25, 26-35, 36-50, 51+.
- Подсчитайте количество пользователей в каждой группе.
- Найдите средний возраст для каждой группы.
'''
import pandas as pd
from pandas import DataFrame
import numpy as np

df3 = pd.read_csv('/Users/maiksamarchuk/PycharmProjects/teachsills/DZ/DZ12/hw_DE_12.csv')
df3['age'] = np.random.randint(18, 66, size=len(df3))
age_bins =[18, 26, 36, 51, 120]
age_labes = ['18-25', '26-35', '36-51', '51+']
df3['age_group'] = pd.cut(df3['age'], bins=age_bins, labels=age_labes, right=False)
group_cnt = df3['age_group'].value_counts().sort_index()
print(group_cnt)
maen_age = df3.groupby('age_group')['age'].mean().round(1)
print(maen_age)
df4 = pd.read_csv['hw_DE_12.csv']