import pandas as pd

def calculate_norm_hours(rate):
    rate = float(rate)
    hours_per_rate = 830
    return round(hours_per_rate * rate, 2)

df_rates = pd.read_excel('15 вариант.xls', sheet_name='19-20')
df_actual = pd.read_excel('15 вариант.xls', sheet_name='общее')

actual_hours = df_actual.groupby('ФИО')['Количества часов по УП'].sum()

print("Преподаватели с недогрузом (для добалансировки):")
print("-" * 60)
for i in range(2, len(df_rates)):
    fio = df_rates['Unnamed: 0'][i]
    if pd.notna(fio):
        norm = calculate_norm_hours(df_rates['Unnamed: 4'][i])
        actual = round(actual_hours.get(fio, 0), 2)
        deficiency = round(norm - actual, 2)
        if deficiency > 0:
            print(fio, 'норма:', norm, 'факт:', actual, 'недогруз:', deficiency)
