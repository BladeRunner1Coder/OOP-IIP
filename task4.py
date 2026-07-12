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
        if not isinstance(other, Student) or type(self.average()) is str or type(other.average()) is str:
            return 'Ошибка'
        return self.average() == other.average()

    def __gt__(self, other):
        if not isinstance(other, Student) or type(self.average()) is str or type(other.average()) is str:
            return 'Ошибка'
        return self.average() > other.average()

    def __lt__(self, other):
        if not isinstance(other, Student) or type(self.average()) is str or type(other.average()) is str:
            return 'Ошибка'
        return self.average() < other.average()

    def average(self):
        all_grades = [num for sublist in self.grades.values() for num in sublist]
        if len(all_grades) > 0:
            return sum(all_grades) / len(all_grades)
        else:
            return 'Оценки отсутствуют'

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
        if not isinstance(other, Lecturer) or type(self.average()) is str or type(other.average()) is str:
            return 'Ошибка'
        return self.average() == other.average()

    def __gt__(self, other):
        if not isinstance(other, Lecturer) or type(self.average()) is str or type(other.average()) is str:
            return 'Ошибка'
        return self.average() > other.average()

    def __lt__(self, other):
        if not isinstance(other, Lecturer) or type(self.average()) is str or type(other.average()) is str:
            return 'Ошибка'
        return self.average() < other.average()

    def average(self):
        all_grades = [num for sublist in self.grades.values() for num in sublist]
        if len(all_grades) > 0:
            return sum(all_grades) / len(all_grades)
        else:
            return 'Оценки отсутствуют'

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

student1 = Student('Misha', 'Ivanov', 'M')
student2 = Student('Natasha', 'Sidorova', 'F')
mentor1 = Mentor('Viktor', 'Belov')
mentor2 = Mentor('Elena', 'Krasnova')
lecturer1 = Lecturer('Sergey', 'Kotov')
lecturer2 = Lecturer('Irina', 'Popova')
reviewer1 = Reviewer('Ivan', 'Smirnov')
reviewer2 = Reviewer('Svetlana', 'Sokolova')

student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Python']
student1.finished_courses += ['Java']
student2.finished_courses += ['Java']
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student1, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 8)

student1.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer1, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 8)

print(student1)
print(mentor1)
print(lecturer1)
print(reviewer1)
print(student1 == student2)
print(lecturer1 == lecturer2)
print(student1 < student2)
print(lecturer1 < lecturer2)
print(student1 > student2)
print(lecturer1 > lecturer2)

def average_student_grade(student_list, course):
    grade_list = []
    for student in student_list:
        if course in student.grades:
            grade_list += student.grades[course]
    if len(grade_list) > 0:
        return sum(grade_list) / len(grade_list)
    else:
        return 'Оценки по этому курсу отсутствуют'

def average_lecturer_grade(lecturer_list, course):
    grade_list = []
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            grade_list += lecturer.grades[course]
    if len(grade_list) > 0:
        return sum(grade_list) / len(grade_list)
    else:
        return 'Оценки по этому курсу отсутствуют'

student_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]

print(average_student_grade(student_list, 'Python'))
print(average_lecturer_grade(lecturer_list, 'Python'))

print(reviewer1.rate_hw(student1, 'Java', 8))
print(student1.rate_lecture(lecturer1, 'Java', 8))

student3 = Student('Maksim', 'Fedorov', 'M')
print(student3)
lecturer3 = Lecturer('Alla', 'Pankratova')
print(lecturer3)
print(student1 == student3)
print(lecturer1 == lecturer3)
print(student1 < student3)
print(lecturer1 < lecturer3)
print(student1 > student3)
print(lecturer1 > lecturer3)
student_list2 = [student3]
lecturer_list2 = [lecturer3]
print(average_student_grade(student_list2, 'Python'))
print(average_lecturer_grade(lecturer_list2, 'Python'))
