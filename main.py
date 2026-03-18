class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade_count(self):
        total = 0
        total_lenght = 0
        for course in self.grades.values():
            for grade in course:
                total += grade
                total_lenght += 1
        if total_lenght != 0:
            return total / total_lenght
        else:
            return None

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за домашние задания: {self.average_grade_count()} \n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade_count() == other.average_grade_count()

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade_count() > other.average_grade_count()

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade_count() < other.average_grade_count()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade_count(self):
        total = 0
        total_lenght = 0
        for course in self.grades.values():
            for grade in course:
                total += grade
                total_lenght += 1
        if total_lenght != 0:
            return total / total_lenght
        else:
            return None

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname} \n'
                f'Средняя оценка за лекции: {self.average_grade_count()}')

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade_count() == other.average_grade_count()

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade_count() > other.average_grade_count()

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade_count() < other.average_grade_count()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}')


lecturer = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Семен', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Ольга', 'Алехина', 'Ж')
student2 = Student('Саня', 'Петров', 'М')
student.finished_courses += ['Введение в программирование']
student.courses_in_progress += ['Python', 'Java', 'C++']
student2.courses_in_progress += ['Python', 'Java', 'C++']
lecturer.courses_attached += ['Python', 'C++']
lecturer2.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

student.rate_lecture(lecturer, 'Python', 7)
student.rate_lecture(lecturer, 'C++', 5)
student2.rate_lecture(lecturer, 'Python', 9)
student2.rate_lecture(lecturer, 'C++', 8)
student2.rate_lecture(lecturer2, 'C++', 8)
reviewer.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student2, 'Python', 7)
reviewer.rate_hw(student, 'C++', 5)

print(lecturer.grades)
print(student)
print(reviewer)
print(lecturer)
print(student > student2)
print(student == student2)
print(student < student2)
print(lecturer > lecturer2)
print(lecturer == lecturer2)
print(lecturer < lecturer2)
