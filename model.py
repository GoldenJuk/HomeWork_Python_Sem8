path = ''
grade_book = {}
subject = ''
subject_list = [] 

import os.path

def set_class(input_class:str):
    global path
    path = 'Classes/' + input_class + '.txt' 

def get_subject():
    global grade_book
    global subject
    global subject_list
    for i, item in enumerate(subject_list,1):
        print(f'{i}. {item.title()}')
    while True:
        try:
            subject_number = int(input('\nВыберите предмет: '))
            if 0 < subject_number <= len(subject_list):
                for i, item in enumerate(grade_book.keys(),1):
                    if i == subject_number:
                        subject = item
                        return subject
                break
            else:
                print('Такого предмета нет')        
        except:
            print('Введите цифры')                
        
def get_gradebook_dict():
    global grade_book
    global path
    global subject
    global subject_list
    if os.path.isfile(path):
        with open (path,'r',encoding='utf-8') as file:
            data = file.readlines()
            for item in data:
                subject = item[:item.index('-')]
                subject_list.append(subject)
                students = {line.split(':')[0]:list(map(int, line.split(':')[1].strip().split(' '))) for line in item[item.index('-') + 2:].split(';')}
                grade_book[subject] = students
        return grade_book
    else:
        return False
            
def get_list_students(chosen_subject:str):
    global grade_book
    subject = chosen_subject
    student_list = {}
    for key, values in grade_book.items():
        if key == subject:
            student_list[key] = values
            break
    return student_list    

def get_a_student_who_answers(student_list:dict) -> str:
       
    while True:
        student_number = input('Кто пойдет к доске?: ')
        if student_number == 'exit':
            return 'exit'
        else:
            try:
                student_number = int(student_number)
                if 0 < student_number < 4:
                    for value in student_list.values():
                        for i, student in enumerate(list(value.keys()),1):
                            if i == student_number:
                                who_answer = student
                                return who_answer
                        break
                else:
                    print('Такого ученика нет')        
            except:
                print('Введите цифры')   

def student_grade(subject, student, grade):
    grades = grade_book[subject][student]
    grades.append(grade)
    grade_book[subject][student] = grades

def print_gradebook():
    global grade_book
    print(grade_book)

def save_grade_book_in_file():
    global grade_book
    global subject_list
    student_list = []
    new_file = ''
    grade_book_list = []
    for subj, journal in grade_book.items():
        student_list = []
        for student, grades in journal.items():
            student_list.append(student + ':' + ' '.join(list(map(str, grades))))
        grade_book_list.append(subj + '- ' + ';'.join(student_list))    
    new_file = '\n'.join(grade_book_list)
    with open (path,'w',encoding='utf-8') as file:
        file.write(new_file)