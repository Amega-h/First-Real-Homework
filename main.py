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

        if not ((rating > 0) and (rating <= 10)):
            print("Third argument must be between 0 and 10")
            return

        if not ((subject in self.courses_in_progress) or (subject in self.finished_courses)):
            print("Second argument must be a student`s course")
            return

        lecturer.rate_lecture(subject, rating)

    def average(self):
        all_grades = []

        for subject_grades in self.grades.values():
            all_grades.extend(subject_grades)

        if len(all_grades) == 0:
            return 0
        else:
            return sum(all_grades) / len(all_grades)

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average() == other.average()
        if isinstance(other, (int,float)):
            return self.average() == other

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average() < other.average()
        if isinstance(other, (int,float)):
            return self.average() < other

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average() > other.average()
        if isinstance(other, (int,float)):
            return self.average() > other

    def __str__(self):
        return (f'Name: {self.name}\n'
                f'Surname: {self.surname}\n'
                f'Average homeworks grade: {self.average}\n'
                f'Courses in progress: {", ".join(self.courses_in_progress)}\n'
                f'Finished courses: {", ".join(self.finished_courses)} ')



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
            if subject in self.grades:
                self.grades[subject] += [rating]
            else:
                self.grades[subject] = [rating]
        else:
            print("Lecturer must be part of the course")


    def average(self):
        all_grades = []

        for subject_grades in self.grades.values():
            all_grades.extend(subject_grades)

        if len(all_grades) == 0:
            return 0
        else:
            return sum(all_grades) / len(all_grades)

    def __str__(self):
        return  (f'Name: {self.name}\n'
                f'Surname: {self.surname}\n'
                f'Average grade: {self.average}')

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average() == other.average()
        if isinstance(other, (int,float)):
            return self.average() == other

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average() < other.average()
        if isinstance(other, (int,float)):
            return self.average() < other

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average() > other.average()
        if isinstance(other, (int,float)):
            return self.average() > other


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)


    def __str__(self):
        print(f'Name: {self.name}\nSurname: {self.surname}')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress :
            if course in student.grades:
                student.grades[course] += [grade]
            else :
                student.grades[course] = [grade]
        else:
            return "Error"


def calculate_avg_homework_grade(students,course):
    summary = 0
    length = 0
    if not len(students) == 0:
        for student in students:
            if course in student.courses_in_progress and course in student.grades:
                grades = student.grades[course]
                if grades :
                    summary += sum(grades) / len(grades)
                    length += 1
    else :
        print("List of students is empty")
        return
    return summary / length


def calculate_avg_lecture_grade(lecturers,course):
    summary = 0
    length = 0
    if not len(lecturers) == 0:
        for lecturer in lecturers:
            if course in lecturer.courses_attached and course in lecturer.grades:
                grades = lecturer.grades[course]
                if grades :
                    summary += sum(grades) / len(grades)
                    length += 1
    else :
        print("List of lecturers is empty")
        return
    return summary / length


student1 = Student('Алёхина', 'Ольга', 'Ж')

student1.grades["Python"] = [3, 2, 2]
student1.courses_in_progress = ["Python"]

student2 = Student('Алёхин', 'Виталий', 'М')

student2.grades["Python"] = [8, 6, 9]
student2.courses_in_progress = ["Python"]


lecturer1 = Lecturer('Jack','Smith')
lecturer1.courses_attached = ["Python"]
student1.rate_lecture(lecturer1, "Python", 4)
student1.rate_lecture(lecturer1, "Python", 6)


lecturer2 = Lecturer('Anton','Sokolov')
lecturer2.courses_attached = ["Python"]
student2.rate_lecture(lecturer2, "Python", 8)
student2.rate_lecture(lecturer2, "Python", 10)

print(calculate_avg_homework_grade([student1,student2],"Python"))
print(calculate_avg_lecture_grade([lecturer1,lecturer2],"Python"))
