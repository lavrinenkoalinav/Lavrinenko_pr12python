import random

# Завдання 1. «Швидкий пошук»
def fast_city_search():
    cities = ["Київ", "Одеса", "Львів", "Харків", "Житомир"]
    city_set = set(cities)

    for city in ["Одеса", "Полтава"]:
        if city in city_set:
            print(f"Місто {city} є у списку.")
        else:
            print(f"Місто {city} відсутнє у списку.")

# Завдання 2. «Пошук за словником»
def student_grade_search():
    students = {"Іван": 80, "Марія": 95, "Олег": 78, "Анна": 85}
    name = input("Введіть ім’я студента для пошуку оцінки: ")
    try:
        grade = students[name]
        print(f"Оцінка студента {name}: {grade}")
    except KeyError:
        print(f"Студента з іменем {name} не знайдено у словнику.")

# Завдання 3. «Оптимізація повторів»
def count_most_common_number():
    numbers = [random.randint(1, 1000) for _ in range(10000)]
    frequency = {}

    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    most_common_number = max(frequency, key=frequency.get)
    print(f"Число, що повторюється найчастіше: {most_common_number}")
    print(f"Кількість повторень: {frequency[most_common_number]}")

# Виклик функцій
if __name__ == "__main__":
    print("Завдання 1:")
    fast_city_search()
    print("\n" + "-"*40 + "\n")

    print("Завдання 2:")
    student_grade_search()
    print("\n" + "-"*40 + "\n")

    print("Завдання 3:")
    count_most_common_number()

