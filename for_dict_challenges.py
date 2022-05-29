# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

def number_repetitions(students):
    count_students = {}
    for student in students:
        if count_students.get(student['first_name']):
            count_students[student['first_name']] += 1
        else:
            count_students[student['first_name']] = 1
    return count_students

print('Задание 1')
for key, value in number_repetitions(students).items():
        print(f'{key}: {value}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

def most_common_name(students):
    return sorted(number_repetitions(students).items(), key=lambda x: x[1])[-1][0]

print('\nЗадание 2')
print(f'Самое частое имя среди учеников: {most_common_name(students)}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

print('\nЗадание 3')
nom = 1
for classs in school_students:
    print(f'Самое частое имя в классе {nom}: {most_common_name(classs)}')
    nom +=1


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def gender(students,is_male):
    boy = 0
    girl = 0
    for student in students:
        if is_male[student['first_name']]:
            boy +=1
        else:
            girl +=1
    return (boy,girl)

def gender_schol(school,is_male):
    class_school = {}
    for classs in school:
        boygirl = gender(classs['students'],is_male)
        if not class_school.get(classs['class']):
                class_school[classs['class']] = {'boy':boygirl[0],'girl':boygirl[1]}
        else:
                class_school[classs['class']]['boy'] += boygirl[0]
                class_school[classs['class']]['girl'] += boygirl[1]
    return class_school

print('\nЗадание 4')
for key, value in gender_schol(school,is_male).items():
    boy = value['boy']
    girl = value['girl'] 
    # print(f'Класс {key}: девочки {value['boy']}, мальчики {value['girl'] }') Глеьб, почему нельзя так написать?
    print(f'Класс {key}: девочки {girl}, мальчики {boy}')




# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

print('\nЗадание 5')

mboy = ['-',0]
mgirl = mboy[:]
for key, value in gender_schol(school,is_male).items():
    if value['boy'] > mboy[1]:
        mboy[0] = key
        mboy[1] = value['boy']

    if value['girl'] > mgirl[1]:
        mgirl[0] = key
        mgirl[1] = value['girl']

print(f'Больше всего мальчиков в классе {mboy[0]}')
print(f'Больше всего девочек в классе {mgirl[0]}')



