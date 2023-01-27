import view, model

def start():
    model.set_class(view.input_class())
    if not model.get_gradebook_dict():
        view.print_not_path()
        exit()
        
    view.input_subject()
    chosen_subject = model.get_subject()
    while True:

        student_list = model.get_list_students(chosen_subject)
        view.print_student_list(student_list)
        who_answer = model.get_a_student_who_answers(student_list)
        if who_answer == 'exit':
            break
        grade = view.what_grade(who_answer)
        model.student_grade(chosen_subject, who_answer, grade)
    model.save_grade_book_in_file()


    
    
    
