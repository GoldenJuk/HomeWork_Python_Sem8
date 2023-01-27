def input_class():
    return input('Какой класс открываем?: ').upper()

def print_not_path():
    print('Такого класса не существует')

def input_subject():
    print('\nДоступные предметы:\n'
          '-----------------------')

def print_student_list(student_list:dict):
    print(f'\n--------------------------\n{list(student_list.keys())[0].title()}: \n'
             '--------------------------')
    print(f"{'Ученик:':23} Оценки:\n")        
    for value in student_list.values():
        for i, student in enumerate(value,1):
            print(f'{i}. {student:20} {value.get(student)}')

def what_grade(answer):
    return int(input(f'{answer} ответил на: '))
