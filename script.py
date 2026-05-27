

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)

        if not all_grades:
            return 0
        average_grade = sum(all_grades)/len(all_grades)
        return average_grade

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
            )

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades.extend(grades)

        if len(all_grades) == 0:
            return 0
        average_grade = sum(all_grades)/len(all_grades)
        return average_grade

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        else:
            return 'Ошибка'

    def __str__(self):
        return(
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.average_grade()}'
        )

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return(
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}'
        )

def average_student_grade(students, course):
    average_grade = []
    for student in students:
        if course in student.grades:
            average_grade.extend(student.grades[course])
    if not average_grade:
        return 0
    return sum(average_grade)/len(average_grade)

def average_lecturer_grade(lecturers, course):
    average_grade = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            average_grade.extend(lecturer.grades[course])
    if not average_grade:
        return 0
    return sum(average_grade)/len(average_grade)

#лекторы
lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Виктория', 'Нерадовская')
lecturer3 = Lecturer('Дарья', 'Скобелева')
#проверяющие
reviewer1 = Reviewer('Пётр', 'Петров')
reviewer2 = Reviewer('Григорий', 'Блинов')
reviewer3 = Reviewer('Иммануил', 'Кант')
#студенты
student1 = Student('Ольга', 'Алёхина', 'Ж')
student2 = Student('Ruoy', 'Eman', 'М')
student3 = Student('Дария', 'Уращупкина', 'Ж')

student1.courses_in_progress += ['Python', 'Java']
student2.courses_in_progress += ['Python', 'C++']
student3.courses_in_progress += ['Python', 'Git']

student1.finished_courses += ['Git']
student2.finished_courses += ['Git']
student3.finished_courses += ['C++']

lecturer1.courses_attached += ['Python', 'C++']
lecturer2.courses_attached += ['Python', 'Git']
lecturer3.courses_attached += ['Python', 'C++']

reviewer1.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Python', 'Git']
reviewer3.courses_attached += ['Python', 'C++']

reviewer1.rate_hw(student1, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer3.rate_hw(student3, 'Python', 4)

print(isinstance(lecturer1, Mentor)) # True
print(isinstance(lecturer2, Mentor))
print(isinstance(lecturer3, Mentor))

print(isinstance(reviewer1, Mentor)) # True
print(isinstance(reviewer2, Mentor))
print(isinstance(reviewer3, Mentor))

print(lecturer1.courses_attached)    # []
print(lecturer2.courses_attached)
print(lecturer3.courses_attached)

print(reviewer1.courses_attached)    # []
print(reviewer2.courses_attached)
print(reviewer3.courses_attached)

print(student1.rate_lecture(lecturer1, 'Python', 7))  # None
print(student2.rate_lecture(lecturer2, 'Python', 9))  # Ошибка
print(student3.rate_lecture(lecturer3, 'Python', 6))  # Ошибка

print(lecturer1.grades) # {'Python': [7]}

print()
students = [student1, student2, student3]
print('=' * 30)
print('СТУДЕНТЫ')
print('=' * 30)
for index, student in enumerate(students):
    print(student)
    if index != len(students) - 1:
        print('-' * 30)
print()

lecturers = [lecturer1, lecturer2, lecturer3]
print('=' * 30)
print('ПРЕПОДАВАТЕЛИ')
print('=' * 30)
for index, lecturer in enumerate(lecturers):
    print(lecturer)
    if index != len(lecturers) - 1:
        print('-' * 30)
print()

reviewers = [reviewer1, reviewer2, reviewer3]
print('=' * 30)
print('ПРОВЕРЯЮЩИЕ')
print('=' * 30)
for index, reviewer in enumerate(reviewers):
    print(reviewer)
    if index != len(reviewers) - 1:
        print('-' * 30)
print()

print(student1 < student2)
print(lecturer1 < lecturer2)
print()
print(f'Средняя оценка студентов по Python: {average_student_grade(students, "Python")}')
print(f'Средняя оценка лекторов по Python: {average_lecturer_grade(lecturers, "Python")}')




