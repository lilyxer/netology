from modules import classes as cl

def average_rate_students(lst: list, course: str) -> str:
    """Подсчет средней оценки у студентов по курсу"""
    total_rate = 0
    total_len = 0
    for student in lst:
        total_rate += sum(student.grades.get(course, 0))
        total_len += len(student.grades.get(course, 0))
    return f'Средняя оценка у {student.__class__.__name__} по предмету {course}: {round(total_rate / total_len, 2)}'
    
def average_rate_lectors(lst: list, course: str) -> str:
    """Подсчет средней оценки у лекторов по курсу"""
    total_rate = 0
    total_len = 0
    for lector in lst:
        total_rate += sum(lector.grades.get(course, 0))
        total_len += len(lector.grades.get(course, 0))
    return f'Средняя оценка у {lector.__class__.__name__} по предмету {course}: {round(total_rate / total_len, 2)}'


if __name__ == '__main__':
    print('Создадим по 2 экземпляра для каждого класса')
    st_Aleksandr = cl.Student('Aleksandr', 'Stydentov', 'Male')
    st_Aleksandra = cl.Student('Aleksandra', 'Stydentova', 'Female')
    lector_Fedor = cl.Lecteur('Fedor Mikhailovich', 'Lectorov')
    lector_Alla = cl.Lecteur('Alla Borisovna', 'Lectorova')
    reviwer_Nikolay = cl.Reviwer('Nikolay', 'Zloy')
    reviwer_Anna = cl.Reviwer('Anna', 'Zlaya')
    lst = (st_Aleksandr, st_Aleksandra, lector_Fedor, lector_Alla, 
           reviwer_Nikolay, reviwer_Anna)
    print('\nПроверим наших друзей\n')
    print(*lst, sep='\n\n')
    print('-' * 20)
    print('Добавили предметы и оценки')
    reviwer_Nikolay.courses_attached.extend(['Python', 'HTML', 'C#'])
    reviwer_Anna.courses_attached.extend(['Python', 'HTML', 'C#'])
    st_Aleksandr.courses_in_progress.append('Python')
    st_Aleksandr.courses_in_progress.append('C#')
    st_Aleksandra.courses_in_progress.append('Python')
    st_Aleksandra.courses_in_progress.append('HTML')
    lector_Fedor.courses_attached.extend(['Python', 'C#'])
    lector_Alla.courses_attached.extend(['Python', 'HTML'])
    st_Aleksandr.finished_courses.append('HTML')
    st_Aleksandra.finished_courses.append('C#')
    st_Aleksandr.rate_lecteur(lector_Fedor, 'Python', 2)
    st_Aleksandr.rate_lecteur(lector_Fedor, 'Python', 1)
    st_Aleksandr.rate_lecteur(lector_Fedor, 'C#', 9)
    st_Aleksandra.rate_lecteur(lector_Alla, 'Python', 2)
    st_Aleksandra.rate_lecteur(lector_Alla, 'HTML', 9)
    st_Aleksandra.rate_lecteur(lector_Alla, 'HTML', 6)
    reviwer_Nikolay.rate_hw(st_Aleksandr, 'Python', 2)
    reviwer_Nikolay.rate_hw(st_Aleksandr, 'Python', 7)
    reviwer_Nikolay.rate_hw(st_Aleksandr, 'Python', 6)
    reviwer_Nikolay.rate_hw(st_Aleksandr, 'HTML', 8)
    reviwer_Anna.rate_hw(st_Aleksandra, 'Python', 2)
    reviwer_Anna.rate_hw(st_Aleksandra, 'HTML', 10)
    reviwer_Anna.rate_hw(st_Aleksandra, 'Python', 4)
    reviwer_Anna.rate_hw(st_Aleksandr, 'HTML', 8)
    print('\nПроверим наших друзей после получения оценок и предметов\n')
    print(*lst, sep='\n\n')
    print('-' * 20)
    print(st_Aleksandr.__lt__(lector_Fedor))
    print(lector_Fedor < st_Aleksandr)
    print(st_Aleksandra.__lt__(lector_Alla))
    print(lector_Alla < st_Aleksandra)
    print('запускаем функции по подсчету средних оценок по предмету')
    lst_students = [st_Aleksandr, st_Aleksandra]
    lst_lectors = [lector_Alla, lector_Fedor]
    course = 'Python'
    print(average_rate_students(lst_students, course))
    print(average_rate_lectors(lst_lectors, course))