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

# Функція для виведення середнього балу студента - виконав Чесной Владислав
def show_average_grade(data):
    student_id = int(input("Введіть ID студента: "))
    if student_id in data:
        grades = data[student_id]['subjects'].values()
        average = sum(grades) / len(grades)
        print(f"\nСередній бал студента {data[student_id]['name']}: {average:.2f}")
    else:
        print("Студента не знайдено.")

# Функція для знаходження студента з найвищим середнім балом - виконав Чесной Владислав
def find_best_student(data):
    best_id = None
    best_avg = 0
    for student_id, info in data.items():
        avg = sum(info['subjects'].values()) / len(info['subjects'])
        if avg > best_avg:
            best_avg = avg
            best_id = student_id
    print(f"\nСтудент з найвищим середнім балом:")
    print(f"ПІБ: {data[best_id]['name']}")
    print(f"Група: {data[best_id]['group']}")
    print(f"Середній бал: {best_avg:.2f}")

    # Функція для редагування оцінок студента - виконав Єрмоленко Владислав
def edit_student_grades(data):
    try:
        student_id = int(input("Введіть ID студента для редагування оцінок: "))
        if student_id not in data:
            print(f"Помилка: Студента з ID {student_id} не знайдено.")
            return
        student_info = data[student_id]
        subjects_dict = student_info['subjects']
        subject_names = list(subjects_dict.keys())
        print(f"Редагування оцінок для: {student_info['name']}")
        print("Оберіть предмет для редагування:")
        for i, subject in enumerate(subject_names):
            print(f"  {i + 1}. {subject} (поточна: {subjects_dict[subject]})")
        subject_choice = 0
        while True:
            try:
                subject_choice = int(input(f"Введіть номер предмету (1-{len(subject_names)}): "))
                if 1 <= subject_choice <= len(subject_names):
                    break
                else:
                    print(f"Номер повинен бути від 1 до {len(subject_names)}")
            except ValueError:
                print("Некоректний ввід. Введіть число.")
        subject_to_edit = subject_names[subject_choice - 1]
        new_grade = correct_count_points(subject_to_edit)
        data[student_id]['subjects'][subject_to_edit] = new_grade
        print(f"Успіх! Оцінку з предмету '{subject_to_edit}' оновлено на {new_grade}.")
    except ValueError:
        print("Некоректний ID. Введіть число.")

    # Функція для редагування курсу студента - виконав Єрмоленко Владислав
def edit_student_course(data):
    try:
        student_id = int(input("Введіть ID студента для редагування курсу: "))
        if student_id not in data:
            print(f"Помилка: Студента з ID {student_id} не знайдено.")
            return
        current_info = data[student_id]
        print(f"Редагування курсу для: {current_info['name']} ")
        print(f"Поточний курс: {current_info['course']}")
        new_course = correct_course()
        data[student_id]['course'] = new_course
        print(f"Успіх! Курс для студента {current_info['name']} оновлено на {new_course}.")
    except ValueError:
        print("Некоректний ID. Введіть число.")

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
            show_average_grade(students)
        elif choice == "5":
            find_best_student(students)
        elif choice == "6":
            show_by_group(students)
        elif choice == "7":
            show_by_course(students)
        elif choice == "8":
            edit_student_grades(students)
        elif choice == "9":
            edit_student_course(students)
        elif choice == "0":
            print("Роботу завершено.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз!")

main()
