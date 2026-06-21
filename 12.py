import pandas as pd

# Функция расчёта нормативной нагрузки
# Норма = 830 часов × ставка преподавателя
def calculate_norm_hours(rate):
    return round(830 * float(rate), 2)

# Загрузка листов из Excel файла
df_rates = pd.read_excel("15 вариант.xls", sheet_name="19-20")  # Лист со ставками преподавателей
df_actual = pd.read_excel("15 вариант.xls", sheet_name="общее")  # Лист с фактической нагрузкой

# Группировка по ФИО: суммируем все часы преподавателя из разных дисциплин
actual_hours = df_actual.groupby("ФИО")["Количества часов по УП"].sum()

# Формируем список преподавателей и их недогруза
results = []
for i in range(2, len(df_rates)):
    fio = df_rates["Unnamed: 0"][i]
    if pd.notna(fio):
        norm = calculate_norm_hours(df_rates["Unnamed: 4"][i])
        actual = round(actual_hours.get(fio, 0), 2)
        deficiency = round(norm - actual, 2)
        results.append({
            "ФИО": fio,
            "Норма (ч)": norm,
            "Факт (ч)": actual,
            "Недогруз (ч)": deficiency
        })

# Создаём DataFrame и выводим таблицу
df_results = pd.DataFrame(results)
print(df_results.to_string(index=False))