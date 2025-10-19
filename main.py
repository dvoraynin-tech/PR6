# Словник студентів - виконав Бобошко Вадим
students = {
    101: {
        "group": "КН-45-5/1",
        "name": "Бобошко Вадим Геннадійович",
        "course": 2,
        "subjects": {
            "Чисельні методи": 85,
            "Програмування": 90,
            "Сталий розвиток": 78
        }
    },
    102: {
        "group": "КН-45-5/1",
        "name": "Єрмоленко Владислав Ігорович",
        "course": 2,
        "subjects": {
            "Чисельні методи": 92,
            "Програмування": 88,
            "Сталий розвиток": 80
        }
    },
    103: {
        "group": "КН-45-5/2",
        "name": "Пилипчук Єлизавета Миколаївна",
        "course": 2,
        "subjects": {
            "Чисельні методи": 75,
            "Програмування": 82,
            "Сталий розвиток": 91
        }
    },
    104: {
        "group": "КН-45-5/2",
        "name": "Подоляка Ярослав Віталійович",
        "course": 1,
        "subjects": {
            "Чисельні методи": 83,
            "Програмування": 79,
            "Сталий розвиток": 85
        }
    },
    105: {
        "group": "КН-45-5/2",
        "name": "Чесной Владислав Сергійович",
        "course": 1,
        "subjects": {
            "Чисельні методи": 90,
            "Програмування": 72,
            "Сталий розвиток": 84
        }
    },
}

# кількість предметів для списку студентів - виконала Пилипчук Єлизавета
COUNT_SUBJECTS = 3

subjects = ["Чисельні методи", "Програмування", "Сталий розвиток"]


# 2 Функція для додавання студента в словник - виконала Пилипчук Єлизавета
def correct_count_points(subject):
    while True:
        try:
            count_points = int(input(f"{subject}: "))
            if 1 <= count_points <= 100:
                break
            else:
                print("Кількість балів повинна належати [1, 100]")
        except:
            print("Некоректна кількість балів")
    return count_points

def correct_course():
    while True:
        try:
            course = int(input("Введіть курс:  "))
            if 1 <= course <= 6 :
                break
            else:
                print(f"Номер курсу повинен належати [1, 6]")
        except:
            print("Некоректний номер курсу")
    return course


def correct_subjects_number(subjects):
    n = len(subjects)
    while True:
        try:
            number = int(input("Введіть номер предмету:  "))
            if 1 <= number <= n:
                break
            else:
                print(f"Номер повиненн належати [1,{n}]")
        except:
            print("Некоректний номер предмету")


def correct_course():
    while True:
        try:
            n = int(input("Введіть курс:  "))
            if 1 <= n <= 6:
                break
            else:
                print(f"Номер повиненн належати [1,6]")
        except:
            print("Некоректний номер курсу")

# Функція для додавання студента в словник
def add_student(data, subjects):
    student = dict()
    student_name = input('Введіть ПІБ:  ')
    name_exists = any(info['name'] == student_name for info in data.values())
    if name_exists:
        print(f"Помилка: Студент з ПІБ '{student_name}' вже існує у словнику і не буде доданий.")
        return

    student_id = max(data.keys()) + 1

    student["group"] = input('Введіть групу:  ')
    student["name"] = student_name
    student["course"] = correct_course()
    print("Предмети : кiлькiсть балiв")
    subjects_dict = dict()
    for i in range(len(subjects)):
        count_points = correct_count_points(subjects[i])
        subjects_dict[subjects[i]] = count_points

    student['subjects'] = subjects_dict

    data[student_id] = student

# 3. Видалення студента зi словника -- виконала Пилипчук Єлизавета

def delete_student(data) :
    student_id = int(input("Введiть student_id : "))
    if student_id not in data.keys() :
        print(f"Вiдсутнiй student_id = {student_id}")
    else :
        del data[student_id]
        print(f"Студент з student_id = {student_id} видалений")

# Функція для перегляду всього вмісту словника - виконав Бобошко Вадим
def show_all(data):
    if not data:
        print("Словник порожній.")
    else:
        for student_id, info in data.items():
            print(f"\nID студента: {student_id}")
            print(f"Група: {info['group']}")
            print(f"ПІБ: {info['name']}")
            print(f"Курс: {info['course']}")
            print("Предмети та оцінки:")
            for subject, grade in info['subjects'].items():
                print(f"   {subject}: {grade}")
# Функція для перегляду студентів певного курсу - виконав Подоляка Ярослав
def show_by_course(data):
    course = int(input("Введіть номер курсу: "))
    print(f"\nСтуденти {course}-го курсу:")
    found = False
    for sid, info in data.items():
        if info["course"] == course:
            print(f"{sid}: {info['name']} — група {info['group']}")
            found = True
    if not found:
        print("Немає студентів цього курсу.")
        
# Функція для перегляду студентів певної групи - виконав Подоляка Ярослав
def show_by_group(data):
            group = input("Введіть назву групи: ")
            print(f"\nСтуденти групи {group}:")
            found = False
            for sid, info in data.items():
                if info["group"] == group:
                    print(f"{sid}: {info['name']} (курс {info['course']})")
                    found = True
            if not found:
                print("Немає студентів цієї групи.")

def main():
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Переглянути весь словник студентів")
        print("2. Додати нового студента")
        print("3. Видалити студента")
        print("4. Вивести середній бал студента")
        print("5. Знайти студента з найвищим середнім балом")
        print("6. Показати студентів певної групи")
        print("7. Показати студентів певного курсу")
        print("8. Редагувати оцінки студента")
        print("9. Редагувати курс студента")
        print("0. Вихід")



        choice = input("Ваш вибір: ")

        if choice == "1":
            show_all(students)
        elif choice == "2":
            add_student(students, subjects)
        elif choice == "3":
            delete_student(students)
        elif choice == "4":
            print("Тут має бути функція виведення середнього балу студента")
        elif choice == "5":
            print("Тут має бути функція знаходження студента з найвищим середнім балом")
        elif choice == "6":
            show_by_group(students)
        elif choice == "7":
            show_by_course(students)
        elif choice == "8":
            print("Тут має бути функція редагування оцінок студента")
        elif choice == "9":
            print("Тут має бути функція редагування курсу студента")
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз!")

main()
