class Student:
    """Класс студента, получает оценки, учится, ставит оценки преподавателям"""
    def __init__(self, name: str, surname: str, gender: str) -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] # курс который закончил студент
        self.courses_in_progress = [] # котрый проходит студент
        self.grades = {} # оценки по курсам студентов
        
    def rate_lecteur(self, teacher: str, course: str, rate: int):
        """сверяемся со своими курсами и курсами лектора, если есть совпадение
        и оценка не более 10 можем поставить оценку для лектора"""
        if isinstance(teacher, Lecteur) and rate in range(11):
            if course in teacher.courses_attached:
                teacher.grades.setdefault(course, []).append(rate)
            else:
                print('Совпадений по курсам не найдено')
        else:
            print(f'Произошла ошибка, либо {teacher.name} не является лектором\n'
                  f'либо оценка {rate} не валидна')
    
    def average(self) -> float:
        """Возвращает среднюю оценку"""
        summary = 0
        len_ = 0
        for rate in self.grades.values():
            summary += sum(rate)
            len_ += len(rate)
        if len_:
            return round(summary / len_, 2)
        return 0.0
    
    def comparison(self, other):
        """Метод сравнения между классами"""
        s_avg = self.average()
        o_avg = other.average()
        if isinstance(other, Lecteur) and o_avg and s_avg:
            if s_avg > o_avg:
                return f'Студент {self.name} имеет больший балл чем у {other.name}'
            elif s_avg == o_avg:
                return f'Студент {self.name} имеет равный балл с {other.name}'
            else:
                return f'Студент {self.name} имеет меньший балл чем у {other.name}'
        return f'{other} не является лектором, сравнить нельзя'
    
    def __str__(self) -> str:
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}')
        
class Mentor:
    def __init__(self, name: str, surname: str) -> None:
        """Класс предок для учителей"""
        self.name = name
        self.surname = surname
        self.courses_attached = [] # за какими курсами закреплен
        self.grades = {}
    
    def average(self) -> float:
        """Возвращает среднюю оценку"""
        summary = 0
        len_ = 0
        for rate in self.grades.values():
            summary += sum(rate)
            len_ += len(rate)
        if len_:
            return round(summary / len_, 2)
        return 0.0
    
    def __str__(self) -> str:
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')
        
class Lecteur(Mentor):
    """Класс лектора, может получать оценки от студентов"""
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)
        
    def comparison(self, other) -> str:
        """Метод сравнения между классами"""
        s_avg = self.average()
        o_avg = other.average()
        if isinstance(other, Student) and o_avg and s_avg: # только со студентами?
            if s_avg > o_avg:
                return f'Студент {self.name} имеет больший балл чем у {other.name}'
            elif s_avg == o_avg:
                return f'Студент {self.name} имеет равный балл с {other.name}'
            else:
                return f'Студент {self.name} имеет меньший балл чем у {other.name}'
        return f'{other} не является студентом, сравнить нельзя'
        
    def __str__(self) -> str:
        return (f'{super().__str__()}\n' # как правильно перегрузить?
                f'Средняя оценка за лекции: {self.average()}')
        
class Reviwer(Mentor):
    """Класс ментора, выставляет оценки студентам"""
    def __init__(self, name: str, surname: str) -> None:
        super().__init__(name, surname)
        
    def rate_hw(self, student: str, course: str, grade: int) -> str|None:
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

if __name__ == '__main__':
    print('Создадим по 1 экземпляру для каждого класса')
    student = Student('Aleksandr', 'Stydentov', 'Male')
    lector = Lecteur('Fedor Mikhailovich', 'Lectorov')
    reviwer = Reviwer('Nikolay', 'Zloy')
    lst = (student, lector, reviwer)
    print('\nПроверим наших друзей\n')
    print(*lst, sep='\n\n')
    print('-' * 20)
    print('Добавили предметы и оценки')
    reviwer.courses_attached.extend(['Python', 'HTML', 'C#'])
    student.courses_in_progress.append('Python')
    student.courses_in_progress.append('C#')
    lector.courses_attached.extend(['Python', 'C#'])
    student.finished_courses.append('HTML')
    student.rate_lecteur(lector, 'Python', 2)
    student.rate_lecteur(lector, 'Python', 1)
    student.rate_lecteur(lector, 'C#', 9)
    reviwer.rate_hw(student, 'Python', 2)
    reviwer.rate_hw(student, 'Python', 7)
    reviwer.rate_hw(student, 'Python', 6)
    reviwer.rate_hw(student, 'HTML', 8) # нужен другой лектор ))
    print('\nПроверим наших друзей после получения оценок и предметов\n')
    print(*lst, sep='\n\n')
    print('-' * 20)
    print(student.comparison(lector))
    
    
## rev_ = Reviwer('rev', 'Ov')+
# rev_.courses_attached += ['Python+']+
# lec_ = Lecteur('ment', 'Ov')+
# lec_.courses_attached += ['Python']+
# print(rev_.courses_attached)+
# # stud = Student('stu', 'Ov', 'M')+
# stud.courses_in_progress.append('Python')+
# stud.rate_lecteur(lec_, 10)+
# print(lec_.grades)+
# rev_.rate_hw(stud, 'Python', 2)
# rev_.rate_hw(stud, 'Python', 10)
# rev_.rate_hw(stud, 'Python', 5)
# print(stud)
# print(stud.grades)
# print(lec_)
# print(rev_)

# print(stud.comparison(lec_))