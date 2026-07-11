class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''

    def __eq__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average() == other.average()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average() > other.average()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Ошибка'
        return self.average() < other.average()

    def average(self):
        all_grades = [num for sublist in self.grades.values() for num in sublist]
        return sum(all_grades) / len(all_grades)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
                return None
            else:
                lecturer.grades[course] = [grade]
                return None
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average() == other.average()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average() > other.average()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Ошибка'
        return self.average() < other.average()

    def average(self):
        all_grades = [num for sublist in self.grades.values() for num in sublist]
        return sum(all_grades) / len(all_grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                return None
            else:
                student.grades[course] = [grade]
                return None
        else:
            return 'Ошибка'
