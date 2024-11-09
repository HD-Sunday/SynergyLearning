# Функция для определения дня недели по дате
def get_day_of_week(day, month, year):
    # Используем библиотеку datetime для расчета дня недели
    from datetime import datetime
    date = datetime(year, month, day)
    return date.strftime("%A")

# Функция для определения високосного года
def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# Функция для определения возраста пользователя
def get_age(current_year, birth_year):
    return current_year - birth_year

# Функция для вывода даты рождения в формате *dd mm yyyy*
def print_birthday(day, month, year):
    # Используем форматирование строки для вывода даты
    print("*" * day + " " * (2 - len(str(month))) + str(month) + " " * (4 - len(str(year))) + str(year) + "*" * 4)

# Запрашиваем у пользователя дату рождения
day = int(input("Введите день рождения: "))
month = int(input("Введите месяц рождения (число от 1 до 12): "))
year = int(input("Введите год рождения: "))

# Выводим дату рождения в формате *dd mm yyyy*
print_birthday(day, month, year)

# Определяем день недели по дате рождения
day_of_week = get_day_of_week(day, month, year)
print("Ваш день рождения приходится на", day_of_week)

# Определяем, был ли год високосным
leap_year = is_leap_year(year)
if leap_year:
    print("Год", year, "был високосным.")
else:
    print("Год", year, "не был високосным.")

# Определяем возраст пользователя
age = get_age(current_year=2024, birth_year=year)
print("Вам сейчас", age, "лет.")


stars = {
    '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
    '1': ["  *  ", " **  ", "  *  ", "  *  ", " ****"],
    '2': [" *** ", "    *", " *** ", "*    ", " *** "],
    '3': [" *** ", "    *", " *** ", "    *", " *** "],
    '4': ["*   *", "*   *", " *** ", "    *", "    *"],
    '5': [" *** ", "*    ", " *** ", "    *", " *** "],
    '6': [" *** ", "*    ", " *** ", "*   *", " *** "],
    '7': [" *** ", "    *", "   * ", "  *  ", " *   "],
    '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
    '9': [" *** ", "*   *", " *** ", "    *", " *** "]
}
for i in range(5): # Каждая цифра имеет 5 строк
   output_line = ""
   for char in f"{day:02d} {month:02d} {year}": # Добавляем пробел между частями даты
      if char in stars:
         output_line += stars[char][i] + " "
      else:
         output_line += " " # Для пробела
   print_birthday = output_line
   print(output_line)
