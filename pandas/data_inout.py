import pandas as pd

df = pd.read_csv('C:/K-digital-python/pandas/tips.csv')

# total_bill이 20보다 큰 행들만 선택해보세요.
selected_rows = df[df['total_bill'] > 20]
print(selected_rows)
# sex가 'Female'인 행들만 선택해보세요.
selected_rows = df[df['sex'] == 'Female']
print(selected_rows)
# day가 'Sun'이고 time이 'Dinner'인 행들만 선택해보세요.
selected_rows = df[(df['day'] == 'Sun') & (df['time'] == 'Dinner')]
print(selected_rows)
# tip이 5보다 크고 size가 3 또는 4인 행들만 선택해보세요.
selected_rows = df[(df['tip'] > 5) & (df['size'].isin([3, 4]) )]
print(selected_rows)
# total_bill, tip, size 열만 선택해보세요.
selected_cols = df[['total_bill', 'tip', 'size']]
print(selected_cols)