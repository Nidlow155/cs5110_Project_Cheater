from Student import Student
from configuration import *
from random import randint
from seaborn import barplot


class Class:
    def __init__(self, student_count, dueDate, verbose):
        self.dueDate = dueDate  # considered to be due at 12:01 AM on the dueDate. For example, if it is due on day 10, they have days 0-9 to work on the assignment
        self.today = 0
        self.students = []

        # build the distributions of procrastination and cheat levels
        procrastinate_levels = []
        for i in range(len(CHEAT_DISTR)):
            amountAtLevel_i = int(CHEAT_DISTR[i] * NUM_STUDENTS)
            for j in range(amountAtLevel_i):
                procrastinate_levels.append(i)

        print(f"len(procrastiante_levels) = {len(procrastinate_levels)}, NUM_STUDENTS = {NUM_STUDENTS}")


        # add the students
        for i in range(student_count):
            cheat = 2
            procrastinate = 4
            self.students.append(Student(i, cheat, procrastinate, dueDate))

        # set the friends
        needsFriends = [True] * NUM_STUDENTS
        counter = 0
        while (True in needsFriends):
            if verbose:
                print(f'\n========\nROUND {counter}\n========\n')
            for i in range(len(self.students)):
                if self.students[i].needsFriends():
                    self.students[i].makeFriends(self.students, verbose)
                needsFriends[i] = self.students[i].needsFriends()
            counter += 1
            if counter == MAX_ITERATIONS:
                break
        if counter == MAX_ITERATIONS:
            print("Maxed Out")
        else:
            if verbose:
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
