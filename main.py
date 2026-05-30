from token import STRING


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, subject, rating):
        if not isinstance(lecturer, Lecturer):
            print("First argument must be a Lecturer")
            return

        if not isinstance(subject, str):
            print("Second argument must be a string")
            return

        if not ((rating > 0) and (rating < 10)):
            print("Third argument must be between 0 and 10")
            return

        if not ((subject in self.courses_in_progress) or (subject in self.finished_courses)):
            print("Second argument must be a student`s course")
            return

        lecturer.rate_lecture(subject, rating)



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_lecture(self, subject, rating):
        if subject in self.courses_attached :
            self.grades[subject] = rating
        else:
            print("Lecturer must be part of the course")





class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress :
            if course in student.grades:
                student.grades[course] += [grade]
            else :
                student.grades[course] = [grade]
        else:
            return "Error"


lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка

print(lecturer.grades)  # {'Python': [7]}