from Student import Student
from common import *
from random import randint

class Class:
    def __init__(self, student_count, dueDate):
        self.dueDate = dueDate  # considered to be due at 12:01 AM on the dueDate. For example, if it is due on day 10, they have days 0-9 to work on the assignment
        self.today = 0
        self.students = []

        # add the students
        for i in range(student_count):
            cheat = randint(*CHEAT_RANGE)
            procrastinate = randint(*PROCRASTINATION_RANGE)
            self.students.append(Student(i, cheat, procrastinate, dueDate))

        # set the friends
        studentsWithAllFriends = 0
        maxIterations = 10000
        counter = 0
        while (studentsWithAllFriends != NUM_STUDENTS or counter == maxIterations):
            for student in self.students:
                if student.needsFriends():
                    studentsWithAllFriends += student.makeFriends(self.students)
            counter += 1
        if counter == maxIterations:
            print("Maxed Out")
        else:
            for student in self.students:
                student.printFriendList()

    def useDay(self, report=False):
        if report:
            print('During day: ' + str(self.today))
        for student in self.students:
            student.useDay(self.today, report)
        if report:
            self.report()
        self.today += 1

    def report(self):
        print("\nAt the end of day: " + str(self.today))
        for student in self.students:
            if student.finished:
                print(f'Student {student.id} has finished')
            else:
                print(f'Student {student.id} has progress {student.progress}')
        print()
