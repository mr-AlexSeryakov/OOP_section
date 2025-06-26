# Класс Sudent, простая система по выставлению оценок ученика (Учебное задание 4.1 
class Student:
    """
    Student - представляет студента с ФИО, группой и оценками

    Атрибуты:
        fio (str): ФИО студента
        group (str): группа
        lect_marks (List[int]): оценки за лекцию
        homework_marks (List[int]): оценки за домашнее задание

    Методы:
        add_lect_marks (mark): добавляет оценку за лекцию
        add_homework_marks (mark): добавляет оценку за домашнее задание
        __str__(): возвращает строковое представление информации о студенте
    """
    def __init__(self, fio, group):
        self.fio = fio
        self.group = group
        self.lect_marks = []
        self.homework_marks = []

    def add_lect_marks(self, mark):
        """Добавляет оценку за лекцию
        Параметр:
            mark (int): оценка за лекцию"""
        self.lect_marks.append(mark)

    def add_homework_marks(self, mark):
        """Добавляет оценку за домашнее задание
        Параметр:
            mark (int): оценка за домашнее задание"""
        self.homework_marks.append(mark)

    def __str__(self) -> str:
        """Возвращает информацию по студенту"""
        return f"Студент {self.fio}: оценки на лекциях: {str(self.lect_marks)}; оценки за д/з: {str(self.homework_marks)}"

class Mentor:
    """
    Mentor - базовый класс для преподавателей

    Атрибуты:
        fio (str): ФИО
        subject (str): Тема

    Методы:
        set_mark (student, mark): Абстрактный метод для выставления оценки студенту
    """
    def __init__(self, fio, subject):
        self.fio = fio
        self.subject = subject

    def set_mark(self, student, mark):
        """Абстрактный метод выставления оценки
        Параметры:
            student (Student): объект студента
            mark (int): выставляемая оценка

        Исключения:
            NotImplementedError: если метод не переопределён в дочернем классе
            """
        raise NotImplementedError

class Lector(Mentor):
    """
    Дочерний класс, расширяющий Mentor

    Переопределяет методы:
        set_mark (student, mark): лектор ставит оценку

    Добавляет методы:
        __str__ (): Возвращает строку с описанием лектора и предмета
    """
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        """Переопределенный метод, добавляет оценку"""
        student.add_lect_marks(mark)

    def __str__(self) -> str:
        """Возвращает строку с описанием лектора и предмета"""
        return f"Лектор {self.fio}: предмет {self.subject}"

class Reviewer(Mentor):
    """
    Дочерний класс, расширяющий Mentor

    Переопределяет методы:
        set_mark (student, mark): Эксперт ставит оценку за домашнюю работу

    Добавляет методы:
        __str__ (): Возвращает строку с описанием эксперта и предмета
    """
    def __init__(self, fio, subject):
        super().__init__(fio, subject)

    def set_mark(self, student, mark):
        """Переопределенный метод, добавляет оценку"""
        student.add_homework_marks(mark)

    def __str__(self) -> str:
        """Возвращает строку с описанием эксперта и предмета"""
        return f"Эксперт {self.fio}: предмет {self.subject}"

        

# Проверочный код
# Проверяем взаимодействие классов Lector, Reviewer и Student
lector = Lector("Gusenko D.", "Physics")
reviewer = Reviewer("Golovanod A.", "Management")
student = Student("Zyablikov D.E.", "M3o-118B")
lector.set_mark(student, 4)
reviewer.set_mark(student, 5)
print(lector)
print(reviewer)
print(student)

# Лектор Gusenko D.: предмет Physics
# Эксперт Golovanod A.: предмет Management
# Студент Zyablikov D.E.: оценки на лекциях: [4]; оценки за д/з: [5]

# Проверяем, что класс Mentor абстрактный 
# и нельзя создать объекты этого класса
try:
    mentor = Mentor("Gusenko D.", "Physics")
    mentor.set_mark(student, 4)

except NotImplementedError as e:
    print("Ошибка") # Ошибка