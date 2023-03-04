from modules import classes as cl

def average_rate_students(lst: list, course: str) -> str:
    """Подсчет средней оценки у студентов по курсу"""
    total_rate = 0
    total_len = 0
    for student in lst:
        total_rate += sum(student.grades.get(course, ''))
        total_len += len(student.grades.get(course, ''))
        if not total_len: # Можем убрать условие что курс должен быть у всех в списке предметов
            return f'Скорее всего {course} не найден у одного из студентов, подсчитать нельзя'
    if total_len: # если курс есть хотя бы у одного
        return f'Средняя оценка у {student.__class__.__name__} по предмету {course}: {round(total_rate / total_len, 2)}'
    return f'{course} не найден ни у одного из студентов'
    
    
def average_rate_lectors(lst: list, course: str) -> str:
    """Подсчет средней оценки у лекторов по курсу"""
    total_rate = 0
    total_len = 0
    for lector in lst:
        total_rate += sum(lector.grades.get(course, ''))
        total_len += len(lector.grades.get(course, ''))
        if not total_len: # Можем убрать условие что курс должен быть у всех в списке предметов
            return f'Скорее всего {course} не найден у одного из лекторов, подсчитать нельзя'
    if total_len: # если курс есть хотя бы у одного
        return f'Средняя оценка у {lector.__class__.__name__} по предмету {course}: {round(total_rate / total_len, 2)}'
    return f'{course} не найден ни у одного из лекторов'


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
    reviwer_Nikolay.add_course(['Python', 'HTML', 'C#'])
    reviwer_Anna.add_course(['Python', 'HTML', 'C#'])
    st_Aleksandr.add_course('Python')
    st_Aleksandr.add_course('C#')
    st_Aleksandra.add_course('Python')
    st_Aleksandra.add_course('HTML')
    lector_Fedor.add_course(['Python', 'C#'])
    lector_Alla.add_course(['Python', 'HTML'])
    st_Aleksandr.add_course('HTML', False) # курса пройден
    st_Aleksandra.add_course('C#', False) # курса пройден
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
    print(st_Aleksandr.__lt__(st_Aleksandra))
    print(st_Aleksandra < st_Aleksandr)
    print(lector_Fedor.__lt__(lector_Alla))
    print(lector_Alla < lector_Fedor)
    print('-' * 20)
    print('запускаем функции по подсчету средних оценок по предмету')
    course = input('Введите название курса: ')  # 
    print(average_rate_students(cl.Student.lst_name, course))
    print(average_rate_lectors(cl.Lecteur.lst_name, course))
